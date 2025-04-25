
from playwright.sync_api import Page,Playwright, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dtna--ngwuat.sandbox.my.salesforce.com")

#chromium headless mode, 1 single context
def test_playwrightShortcut(page:Page):
    page.goto("https://dtna--ngwuat.sandbox.my.salesforce.com")


def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning1234")
    #If your using "get_by_role" for dropdown in the page then parameter should be "combobox"
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    # If your using "get_by_role" for button and  in the page there are many button and dom is specifed with name attribute you can use like below.
    page.get_by_role("button", name= "Sign In").click()
    #Here are two things
    # one is auto wait mechanism till 10s is it is not found throw timeout exceptions
    # two if ant text is static in nature on dom then use of this get_by_text
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_open_browser_in_Firefox(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning1234")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
