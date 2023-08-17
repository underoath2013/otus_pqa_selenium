from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CardPage(BasePage):
    PATH = "/desktops/macbook"
    DESKTOP_MENU = (By.LINK_TEXT, 'Desktops')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button#button-cart')
    ADD_TO_WISH_LIST = (By.CSS_SELECTOR, 'button.btn-default[onclick^="wishlist.add"]')
    NAVIGATION_TABS = (By.CSS_SELECTOR, 'ul.nav-tabs li a')

    def open(self, url):
        self.open_url(url + self.PATH)

    def find_dropdown_menu(self):
        return self.element(CardPage.DESKTOP_MENU)

    def find_add_to_cart_button(self):
        return self.element(CardPage.ADD_TO_CART_BUTTON)

    def find_add_to_wish_list(self):
        return self.element(CardPage.ADD_TO_WISH_LIST)

    def find_navigation_tabs(self):
        return self.elements(CardPage.NAVIGATION_TABS)
