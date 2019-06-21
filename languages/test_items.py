from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
button_locator = (By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")


def test_button_availability(browser):
    browser.get(link)
    button = browser.find_element(*button_locator)
    assert button.is_displayed() and button.is_enabled(), "The item on the locator [%s] is not available" % button_locator
