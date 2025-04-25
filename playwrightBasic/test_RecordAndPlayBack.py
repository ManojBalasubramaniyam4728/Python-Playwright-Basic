from playwright.sync_api import Playwright, sync_playwright, expect

# To open the recode And Play back inspector or playwright
# syntax "playwright codegen <url>"
# eg :- playwright codegen https://rahulshettyacademy.com/loginpagePractise/

def test_Run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("learning1234")
    page.get_by_role("textbox", name="Username:").press("ControlOrMeta+z")
    page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("learning1234")
    page.locator("label:nth-child(2) > .checkmark").click()
    page.get_by_role("button", name="Okay").click()
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()

    context.close()
    browser.close()