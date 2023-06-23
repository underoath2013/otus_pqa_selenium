from page_objects import RegisterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_title(browser, url):
    browser.get(url + "/index.php?route=account/register")
    WebDriverWait(browser, 3).until(EC.title_is("Register Account"))


def test_input_field_firstname(browser, url):
    expected_field = ["First Name"]
    browser.get(url + "/index.php?route=account/register")
    input_field = WebDriverWait(browser, 3).until(EC.visibility_of_all_elements_located((RegisterPage.FIRSTNAME)))
    for field, input_element in zip(expected_field, input_field):
        assert input_element.is_displayed(), f"{field} is not visible."


def test_input_field_lastname(browser, url):
    expected_field = ["Last Name"]
    browser.get(url + "/index.php?route=account/register")
    input_field = WebDriverWait(browser, 3).until(EC.visibility_of_all_elements_located((RegisterPage.LASTNAME)))
    for field, input_element in zip(expected_field, input_field):
        assert input_element.is_displayed(), f"{field} is not visible."


def test_input_field_email(browser, url):
    expected_field = ["E-Mail"]
    browser.get(url + "/index.php?route=account/register")
    input_field = WebDriverWait(browser, 3).until(EC.visibility_of_all_elements_located((RegisterPage.EMAIL)))
    for field, input_element in zip(expected_field, input_field):
        assert input_element.is_displayed(), f"{field} is not visible."


def test_input_field_telephone(browser, url):
    expected_field = ["Telephone"]
    browser.get(url + "/index.php?route=account/register")
    input_field = WebDriverWait(browser, 3).until(EC.visibility_of_all_elements_located((RegisterPage.TELEPHONE)))
    for field, input_element in zip(expected_field, input_field):
        assert input_element.is_displayed(), f"{field} is not visible."


def test_input_field_password(browser, url):
    expected_field = ["Password"]
    browser.get(url + "/index.php?route=account/register")
    input_field = WebDriverWait(browser, 3).until(EC.visibility_of_all_elements_located((RegisterPage.PASSWORD)))
    for field, input_element in zip(expected_field, input_field):
        assert input_element.is_displayed(), f"{field} is not visible."


def test_input_field_password_confirm(browser, url):
    expected_field = ["Password Confirm"]
    browser.get(url + "/index.php?route=account/register")
    input_field = WebDriverWait(browser, 3).until(
        EC.visibility_of_all_elements_located((RegisterPage.PASSWORD_CONFIRM)))
    for field, input_element in zip(expected_field, input_field):
        assert input_element.is_displayed(), f"{field} is not visible."
