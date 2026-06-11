import re
from playwright.sync_api import Page, expect


def test_demnoqa_textbox(page: Page) -> None:
    page.goto("https://demoqa.com/text-box")
    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("Jiten")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("Jitenp@Outlook.Com")
    page.get_by_role("textbox", name="Current Address").click()
    page.get_by_role("textbox", name="Current Address").fill("Trivandrum")
    page.locator("#permanentAddress").click()
    page.locator("#permanentAddress").fill("Guntur")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Email:Jitenp@Outlook.Com")).to_be_visible()
    expect(page.get_by_text("Current Address :Trivandrum")).to_be_visible()
    expect(page.get_by_text("Name:Jiten")).to_be_visible()
    expect(page.get_by_text("Permananet Address :Guntur")).to_be_visible()

def test_amazon_search_iphone17(page: Page) -> None:
    page.goto("https://www.amazon.in/")
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill("i")
    page.get_by_role("button", name="iphone 17 pro", exact=True).click()
    page.get_by_role("button", name="Go", exact=True).click()
    expect(page.get_by_text("Apple").nth(2)).to_be_visible()
    expect(page.get_by_text("Apple").nth(2)).to_be_visible()
    expect(page.get_by_role("link", name="iPhone 16 Plus 256 GB: 5G")).to_be_visible()
    expect(page.get_by_role("heading", name="Apple").nth(1)).to_be_visible()
    expect(page.get_by_role("heading", name="Apple").nth(1)).to_be_visible()

