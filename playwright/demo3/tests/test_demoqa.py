from playwright.sync_api import sync_playwright

import pytest 

@pytest.fixture
def browser():
    with sync_playwright() as  p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_demoqa_title(browser):
    page = browser.new_page()
    page.goto("https://demoqa.com")
    expected_title = "demosite"
    actual_title = page.title()
    print(f"page title:{actual_title}")
    assert actual_title == expected_title ## if it is true then only the test is consided as pass

def test_click_elements_card(browser):
    page = browser.new_page()
    page.goto("https://demoqa.com")
    page.locator("a[href='/elements']").click()

    assert page.url == "https://demoqa.com/elements"
    assert page.locator(".element-group .header-text",has_text="Elements").is_visible()

    ## How to run pytest 

    # To run all tests from a file
    # pytest -v scripts.py 

    # To run only one test
    # pytest -v script.py::test_click_elements_card

