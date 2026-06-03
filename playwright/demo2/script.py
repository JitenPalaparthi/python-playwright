from playwright.sync_api import sync_playwright;

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://demoqa.com/buttons")

        page.wait_for_timeout(2000)

        # find and click the btton based on Xpath
       # page.click("//*[@id='root']/div/div/div/div[2]/div[1]/div[3]/button")

       # find a button thru elemnet and its text
       # page.click("//button[text()='Click Me']")
        
        # find a button and click using full Xpath
        # full Xpath is not a good practice as if there are any dynamic elemments are created , it does not work 
        # page.click("xpath=/html/body/div/div/div/div/div[2]/div[1]/div[3]/button")

        # using locator

        # element= page.locator("xpath=/html/body/div/div/div/div/div[2]/div[1]/div[3]/button")
        # element.click()


        # page.get_by_text("Click Me",exact=True).click()
        

        page.get_by_role("button",name="Click Me",exact=True).click()

        # page.get_by_role("a",name="AmazonBasics",exact=True)

        print("Button clicked successfully")

        page.wait_for_timeout(2000)

        browser.close()
       # //*[@id="root"]/div/div/div/div[2]/div[1]/div[3]/button
       # //*[@id="root"]/div/div/div/div[2]/div[1]/div[3]/button
       # /html/body/div/div/div/div/div[2]/div[1]/div[3]/button
run()






# pip install playwright
# playwright install