from pydoc import pager

from openpyxl.utils import rows_from_range
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser

from playwrightBasic.utils.apiBase import APIUtils


def test_e2e_web_api(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.locator("#login").click()

    #verify order id is displayed
    page.get_by_role("button",name="ORDERS").click()
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()