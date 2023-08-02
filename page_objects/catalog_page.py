from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    PATH = "/desktops"
    LOGO = (By.CSS_SELECTOR, '#logo a img')
    TOP_RIGTH_NAVIGATION_BAR = (By.CSS_SELECTOR, '.nav.pull-right li')
    FOOTER_BLOCKS = (By.CSS_SELECTOR, 'footer .container .row .col-sm-3')
    IMAGES = (By.CSS_SELECTOR, '.product-layout .image img')

    def open(self, url):
        self.driver.get(url + self.PATH)

    def find_logo(self):
        self.element(CatalogPage.LOGO)

    def find_top_right_navigation_bar(self):
        top_right_navigation_bar = self.elements_presence(CatalogPage.TOP_RIGTH_NAVIGATION_BAR)
        return top_right_navigation_bar

    def visible_elements_in_top_right_navigation_bar(self, top_right_navigation_bar):
        visible_elements = visible_elements = [
            element for element in top_right_navigation_bar if element.is_displayed()]
        return visible_elements

    def find_footer_blocks(self):
        footer_blocks = self.elements_presence(CatalogPage.FOOTER_BLOCKS)
        return footer_blocks

    def find_product_images(self):
        product_images = self.elements(CatalogPage.IMAGES)
        return product_images
