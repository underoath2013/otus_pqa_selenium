from selenium.webdriver.common.by import By


class AdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    HEADER = (By.CSS_SELECTOR, "#header")
    FOOTER = (By.CSS_SELECTOR, "#footer")
    LOGO = (By.CSS_SELECTOR, 'img[src="view/image/logo.png"]')
    PANEL_BODY_CENTERED = (By.CSS_SELECTOR, ".col-sm-offset-4.col-sm-4 .panel-body")
    BOOTSTRAP_CONTAINER_FLUID = (By.CSS_SELECTOR, ".container-fluid")

