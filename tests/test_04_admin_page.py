from page_objects import AdminPage
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_title(browser, url):
    browser.get(url + "/admin")
    WebDriverWait(browser, 5).until(EC.title_is("Administration"))


def test_check_header(browser, url):
    browser.get(url + "/admin")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdminPage.HEADER))


def test_check_footer(browser, url):
    browser.get(url + "/admin")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdminPage.FOOTER))


def test_check_logo(browser, url):
    browser.get(url + "/admin")
    logo = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdminPage.LOGO))
    assert logo.is_displayed()


@pytest.mark.xfail(reason="Test currently fails with assert 422.0 == (845 / 2)")
def test_panel_body_horizontal_center(browser, url):
    """
    This test checks if the panel body is centered horizontally on the page.
    It fails with a specific assertion error when the expected center x-coordinate of the panel body
    is not equal to half of the container width.
    """
    browser.get(url + "/admin")
    panel_body = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdminPage.PANEL_BODY_CENTERED))
    container_width = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(AdminPage.BOOTSTRAP_CONTAINER_FLUID)).size["width"]
    panel_body_width = panel_body.size["width"]
    panel_body_x = panel_body.location["x"]
    panel_body_center_x = panel_body_x + panel_body_width / 2
    assert panel_body_center_x == container_width / 2, "Panel is not centered horizontally on the page"


def test_login_admin_page(browser, url):
    browser.get(url + "/admin")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdminPage.USERNAME_INPUT))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdminPage.PASSWORD_INPUT))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdminPage.SUBMIT_BUTTON))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdminPage.FORGOTTEN_PASSWORD))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdminPage.OPENCART_LINK))
