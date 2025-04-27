import time
from pydoc import pager

from playwright.sync_api import Page, Playwright, expect
from pytest_playwright.pytest_playwright import playwright, browser

from playwrightBasic.utils.apiBase import APIUtils


#To change the URL before sending it to the server.
def interceptRequest(route):
    route.continue_("https://rahulshettyacademy.com/api/ecom/order/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

def test_Network_2(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    # Intercepting response
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",interceptRequest)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    #it is not showing correct html page so commenting the below line
    #message =page.locator(".blink_me").text_content()
    #print(message)


def test_session_storage(playwright : Playwright):
    apiUtils = APIUtils()
    getToken =apiUtils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #scripting to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

