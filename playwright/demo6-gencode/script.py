import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/text-box")
    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("Jiten")
    page.get_by_role("textbox", name="name@example.com").dblclick()
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("jitenp@outlook.com")
    page.get_by_role("textbox", name="Current Address").dblclick()
    page.get_by_role("textbox", name="Current Address").fill("Trivandrum")
    page.locator("#permanentAddress-wrapper #permanentAddress").dblclick()
    page.locator("#permanentAddress-wrapper #permanentAddress").fill("Guntur")
    page.get_by_role("button", name="Submit").click()
    page.get_by_text("Email:jitenp@outlook.com").click()
    expect(page.get_by_text("Email:jitenp@outlook.com")).to_be_visible()
    page.get_by_text("Current Address :Trivandrum").click()
    expect(page.get_by_text("Current Address :Trivandrum")).to_be_visible()
    page.get_by_text("Permananet Address :Guntur").click()
    expect(page.get_by_text("Permananet Address :Guntur")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()
    print("<<<<<< Automation has been done successfully >>>>>>>>")


with sync_playwright() as playwright:
    run(playwright)
