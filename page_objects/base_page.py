from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def verify_title(self, title):
        try:
            return WebDriverWait(self.driver, 3).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError(f"Didn't wait for title {title}")

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element(parent_locator).find_element(*child_locator)

    def elements_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element(parent_locator).find_elements(*child_locator)

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Didn't wait for element visibility {locator}")

    def get_placeholder_value(self, element):
        placeholder = element.get_attribute("placeholder")
        return placeholder

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Didn't wait for elements visibility {locator}")

    def verify_product_item(self, product_name):
        return self.element((By.LINK_TEXT, product_name))

    def title_contains(self, title: str):
        try:
            return WebDriverWait(self.driver, 3).until(EC.title_contains(title))
        except TimeoutException:
            raise AssertionError(f"Didn't wait for title {title}")

    def elements_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Didn't wait for elements presense {locator}")

    def accept_alert(self):
        try:
            alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert.accept()
        except TimeoutException:
            raise AssertionError(f"Didn't wait for alert")

        # self.driver.switch_to.alert.accept()

    def cancel_alert(self):
        try:
            alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert.dismiss()
        except TimeoutException:
            raise AssertionError(f"Didn't wait for alert")
