import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button.is_displayed() == True, "No 'Add to basket' button on this page"



