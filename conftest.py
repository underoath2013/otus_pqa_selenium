from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import FirefoxOptions, ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Available browsers: firefox, chrome")
    parser.addoption("--url", default="http://192.168.0.112:8081", help="Base URL for the tests")
    parser.addoption("--maximize", action="store_true", help="Maximize browser window")
    parser.addoption("--headless", action="store_true", help="Headless mode")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    headless = request.config.getoption("--headless")

    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
    elif browser_name == "chrome":
        service = Service()
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError(f"Driver {browser_name} not supported")

    if maximize:
        driver.maximize_window()

    yield driver

    driver.quit()
