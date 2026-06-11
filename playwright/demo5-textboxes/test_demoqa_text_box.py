from playwright.sync_api import sync_playwright,expect;

def test_demo_test_box(page:Page):
    page.goto("https://demoqa.com/text-box")
    page.locator("#userName").fill("Jiten P")
    page.locator("#userEmail").fill("jiten@demoqa.com")
    page.locator("#currentAddress").fill("Trivandrum, Kerala")
    page.locator("#permanentAddress").fill("Guntur, AP")
    page.locator("#submit").click()

       # page.wait_for_timeout(2000)

    expect(page.locator("#output #name")).to_have_text("Name:Jiten P")
    expect(page.locator("#output #email")).to_have_text("Email:jiten@demoqa.com")
    expect(page.locator("#output #currentAddress")).to_contain_text("Trivandrum")
    expect(page.locator("#output #permanentAddress")).to_contain_text("Guntur")
        #caddr = page.locator("#output #currentAddress").text_content()
        #print(caddr)






# pip install pytest pytest-playwright
# playwright install

# pytest test_demoqa_text_box.py  --browser webkit --browser firefox --browser chromium
       







# pip install playwright
# playwright install