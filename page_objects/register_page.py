from selenium.webdriver.common.by import By


class RegisterPage:
    FIRSTNAME = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#input-confirm')
