from selenium.webdriver.common.by import By


class CardPage:
    DESKTOP_MENU = (By.LINK_TEXT, 'Desktops')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button#button-cart')
    ADD_TO_WISH_LIST = (By.CSS_SELECTOR, 'button.btn-default[onclick^="wishlist.add"]')
    NAVIGATION_TABS = (By.CSS_SELECTOR, 'ul.nav-tabs li a')