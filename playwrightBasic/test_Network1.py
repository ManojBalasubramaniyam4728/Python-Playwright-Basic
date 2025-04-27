import time
from threading import Thread
from time import thread_time

from playwright.sync_api import Page, expect

fakePayLoadOrderResponse = {"data":[],"message": "No Orders"}

#-> api call from browser -> api call contact server return back response to browser-> browser use response
def intercept_response(route):
    route.fulfill(
        json = fakePayLoadOrderResponse
    )


def test_Network_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    # Intercepting response
    page.route("https://rahulshettyacademy.com/api/ecom/order/delete-order/*",intercept_response)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(2)
    text_message = page.locator(".mt-4").text_content()
    print(text_message)
    assert text_message == " You have No Orders to show at this time. Please Visit Back Us "
