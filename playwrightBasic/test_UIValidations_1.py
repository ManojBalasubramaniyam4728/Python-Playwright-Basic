from gettext import textdomain

from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("button", name="Sign In").click()
    # i am getting this using tage name and filtering by hat_text and in filter it still have has_not_text, has_not
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    #after storing element in one object  i am going inside that particular element and performing action
    iphoneProduct.get_by_role("button").click()
    NokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    NokiaProduct.get_by_role("button").click()
    page.get_by_text("checkout").click()
    #by using css i find element and using to_have_count assertion to validate
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # Capture the new tab (child window) opened when clicking the locator
    with page.expect_popup() as newPage_info:
        #step1
        #step2
        page.locator(".blinkingText").click() #new page
        # Access the new tab (child window) and extract text
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content() #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        print(text)
        #Splitting based on the word 'at'
        words=text.split("at")
        # Extracting the email address by triming the space and Splitting based on the " "
        email= words[1].strip().split(" ")[0]
        #playwrite Assertion check
        assert email == "mentor@rahulshettyacademy.com"

