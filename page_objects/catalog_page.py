from selenium.webdriver.common.by import By


class CatalogPage:
    LOGO = (By.CSS_SELECTOR, '#logo a img')
    TOP_RIGTH_NAVIGATION_BAR = (By.CSS_SELECTOR, '.nav.pull-right li')
    FOOTER_BLOCKS = (By.CSS_SELECTOR, 'footer .container .row .col-sm-3')
    IMAGES = (By.CSS_SELECTOR, '.product-layout .image img')