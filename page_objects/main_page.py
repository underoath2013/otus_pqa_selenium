from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_INPUT = (By.CSS_SELECTOR, '#search input[name="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#search button[type="button"]')
    LOGO = (By.CSS_SELECTOR, '#logo a img')
    NAVIGATION_BAR = (By.CSS_SELECTOR, 'ul.navbar-nav > li')
    FEATURED = (By.CSS_SELECTOR, '.row .product-layout')
