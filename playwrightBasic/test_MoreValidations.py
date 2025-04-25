from contextlib import nullcontext
from tabnanny import check

from playwright.sync_api import Page, expect


def test_UIchecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

def test_AlertBoxes(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    #This page.on listen to you action in that it will aske for two things event and function instead of rapping in function i have used lambda
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()

def test_MouseHover(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    #.hover() to move to till element
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

def test_FrameHandling(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    #by using page.frame_locator find frame and storing in variable and rest same
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access plan").click()
    #to_contain_text() this for validation like .contains
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")

def test_tableHandling(page : Page):
    # check the price of rice is equal to 37
    # identify the price column
    # identify rice row
    # extract the price of the rice
    priceColValue=""
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue=index
            print(f"Price Column value is {priceColValue}")
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")

