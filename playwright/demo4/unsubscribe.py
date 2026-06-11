# unsubscribe.py
import asyncio
import sys
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

# ── config ──────────────────────────────────────────────────────────────
HEADLESS          = False
DELAY_BETWEEN     = 600
SCROLL_PAUSE      = 2000
MAX_EMPTY_SCROLLS = 5
SESSION_DIR       = "./yt-session"
# ────────────────────────────────────────────────────────────────────────

# Injected into the browser — walks every shadow root recursively
FIND_BUTTONS_JS = """
() => {
    function walkShadow(root, collector) {
        root.querySelectorAll('*').forEach(el => {
            // Check this element itself
            if (el.tagName === 'BUTTON') {
                const text = el.textContent.trim().toLowerCase();
                if (text === 'subscribed' || text === 'subscribed ') {
                    collector.push(el);
                }
            }
            // Recurse into shadow root if present
            if (el.shadowRoot) {
                walkShadow(el.shadowRoot, collector);
            }
        });
    }

    const allButtons = [];
    walkShadow(document, allButtons);

    return allButtons.map((btn, i) => {
        // Climb the real DOM (not shadow) to find channel name
        // composedPath() crosses shadow boundaries
        let node = btn;
        let channelName = 'unknown';
        let attempts = 0;

        while (node && attempts < 30) {
            const el = node.getRootNode().host || node.parentElement;
            if (!el) break;
            node = el;
            attempts++;

            // Try to grab channel name from known containers
            const nameEl = el.querySelector
                && (el.querySelector('#channel-title') 
                || el.querySelector('#text.ytd-channel-name')
                || el.querySelector('yt-formatted-string#text'));
            if (nameEl && nameEl.textContent.trim()) {
                channelName = nameEl.textContent.trim().slice(0, 80);
                break;
            }
        }

        return { index: i, channelName };
    });
}
"""

CLICK_BUTTON_JS = """
(targetIndex) => {
    function walkShadow(root, collector) {
        root.querySelectorAll('*').forEach(el => {
            if (el.tagName === 'BUTTON') {
                const text = el.textContent.trim().toLowerCase();
                if (text === 'subscribed' || text === 'subscribed ') {
                    collector.push(el);
                }
            }
            if (el.shadowRoot) walkShadow(el.shadowRoot, collector);
        });
    }

    const allButtons = [];
    walkShadow(document, allButtons);

    const btn = allButtons[targetIndex];
    if (!btn) return 'not_found';
    btn.click();
    return 'clicked';
}
"""

CLICK_CONFIRM_JS = """
() => {
    function walkShadow(root, collector) {
        root.querySelectorAll('*').forEach(el => {
            if (el.tagName === 'BUTTON') {
                const text = el.textContent.trim().toLowerCase();
                // Unsubscribe confirm button text variants
                if (text === 'unsubscribe' || text === 'yes' || text === 'ok') {
                    collector.push(el);
                }
            }
            if (el.shadowRoot) walkShadow(el.shadowRoot, collector);
        });
    }

    const btns = [];
    walkShadow(document, btns);
    if (btns.length === 0) return 'no_confirm_found';
    btns[0].click();
    return 'confirmed';
}
"""


async def wait(ms: int):
    await asyncio.sleep(ms / 1000)


async def scroll_to_bottom(page):
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await wait(SCROLL_PAUSE)


async def unsubscribe_visible(page) -> int:
    channel_info = await page.evaluate(FIND_BUTTONS_JS)

    if not channel_info:
        return 0

    print(f"  Found {len(channel_info)} subscribed buttons")
    count = 0

    # Iterate by index — re-walk shadow DOM for each click
    # so stale references never occur
    for i in range(len(channel_info)):
        channel_name = channel_info[i]["channelName"]

        try:
            result = await page.evaluate(CLICK_BUTTON_JS, i)

            if result != "clicked":
                print(f"  Skipped {channel_name!r}: {result}")
                continue

            # Small pause for dialog to appear
            await wait(800)

            # Try Playwright selector first (faster), fall back to JS shadow walker
            confirmed = False
            try:
                confirm_btn = await page.wait_for_selector(
                    "yt-button-renderer#confirm-button button, "
                    "tp-yt-paper-button#confirm-button, "
                    "yt-button-shape#confirm-button button",
                    timeout=1500,
                    state="visible",
                )
                await confirm_btn.click()
                confirmed = True
            except PlaywrightTimeout:
                # Fall back to shadow-piercing JS confirm click
                confirm_result = await page.evaluate(CLICK_CONFIRM_JS)
                confirmed = confirm_result == "confirmed"

            await wait(DELAY_BETWEEN)
            count += 1
            print(f"  [{count}] Unsubscribed: {channel_name}  (dialog: {confirmed})")

        except Exception as e:
            print(f"  Skipped {channel_name!r}: {e}")

    return count


async def ensure_logged_in(page):
    print("Loading subscriptions page...")
    await page.goto(
        "https://www.youtube.com/feed/channels",
        wait_until="networkidle",
    )
    await wait(3000)

    channel = await page.query_selector("ytd-channel-renderer, ytd-subscribe-button-renderer")
    if not channel:
        print("\nNot logged in — complete sign-in in the browser window.")
        print("Press Enter here once you are signed in...")
        await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
        await page.goto(
            "https://www.youtube.com/feed/channels",
            wait_until="networkidle",
        )
        await wait(3000)


async def main():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            SESSION_DIR,
            headless=HEADLESS,
            viewport={"width": 1280, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )

        page = context.pages[0] if context.pages else await context.new_page()
        await ensure_logged_in(page)

        total_unsubscribed = 0
        empty_scrolls      = 0

        print("\nStarting unsubscribe loop...\n")

        while True:
            unsubscribed_this_round = await unsubscribe_visible(page)
            total_unsubscribed += unsubscribed_this_round

            if unsubscribed_this_round == 0:
                empty_scrolls += 1
                print(f"No buttons found — scrolling ({empty_scrolls}/{MAX_EMPTY_SCROLLS})...")
                if empty_scrolls >= MAX_EMPTY_SCROLLS:
                    print(f"\nDone! Total unsubscribed: {total_unsubscribed}")
                    break
                await scroll_to_bottom(page)
            else:
                empty_scrolls = 0
                await scroll_to_bottom(page)

        await context.close()


if __name__ == "__main__":
    asyncio.run(main())