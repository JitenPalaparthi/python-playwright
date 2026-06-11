// YouTube Bulk Unsubscribe Script
// Run this on: https://www.youtube.com/feed/channels

async function unsubscribeAll() {
  let totalUnsubscribed = 0;

  while (true) {
    // Find all "Subscribed" buttons on the current view
    const buttons = [...document.querySelectorAll('ytd-subscribe-button-renderer button')]
      .filter(btn => btn.textContent.trim().toLowerCase().includes('subscribed'));

    if (buttons.length === 0) {
      console.log('No more subscription buttons found. Scrolling to load more...');
      window.scrollTo(0, document.body.scrollHeight);
      await new Promise(r => setTimeout(r, 3000));

      // Re-check after scroll
      const recheckButtons = [...document.querySelectorAll('ytd-subscribe-button-renderer button')]
        .filter(btn => btn.textContent.trim().toLowerCase().includes('subscribed'));
      if (recheckButtons.length === 0) {
        console.log(`✅ Done! Unsubscribed from ${totalUnsubscribed} channels.`);
        break;
      }
      continue;
    }

    for (const btn of buttons) {
      btn.click();
      await new Promise(r => setTimeout(r, 1000));

      // Confirm the "Unsubscribe" dialog if it appears
      const confirmBtn = document.querySelector('yt-button-renderer#confirm-button button, tp-yt-paper-button#confirm-button');
      if (confirmBtn) {
        confirmBtn.click();
        await new Promise(r => setTimeout(r, 500));
      }

      totalUnsubscribed++;
      console.log(`Unsubscribed #${totalUnsubscribed}`);
    }

    // Small pause before next batch
    await new Promise(r => setTimeout(r, 2000));
  }
}

unsubscribeAll();