from page_objects import CardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_title(browser, url):
    browser.get(url + "/desktops/macbook")
    WebDriverWait(browser, 3).until(EC.title_is("MacBook"))


def test_check_dropdown_menu(browser, url):
    browser.get(url + "/desktops/macbook")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(CardPage.DESKTOP_MENU))


def test_add_to_cart_button(browser, url):
    browser.get(url + "/desktops/macbook")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(CardPage.ADD_TO_CART_BUTTON))


def test_add_to_wish_list(browser, url):
    browser.get(url + "/desktops/macbook")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(CardPage.ADD_TO_WISH_LIST))
    

def test_check_tabs(browser, url):
    browser.get(url + "/desktops/macbook")
    tab_elements = WebDriverWait(browser, 5).until(EC.visibility_of_all_elements_located((CardPage.NAVIGATION_TABS)))
    assert len(tab_elements) == 3
