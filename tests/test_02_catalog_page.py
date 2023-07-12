from page_objects import CatalogPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_title(browser, url):
    browser.get(url + "/desktops")
    WebDriverWait(browser, 3).until(EC.title_is("Desktops"))


def test_check_logo(browser, url):
    browser.get(url + "/desktops")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((CatalogPage.LOGO)))


def test_elements_in_top_rigth_navigation_bar(browser, url):
    browser.get(url + "/desktops")
    elements = WebDriverWait(browser, 3).until(
        EC.presence_of_all_elements_located((CatalogPage.TOP_RIGTH_NAVIGATION_BAR)))
    visible_elements = [element for element in elements if element.is_displayed()]
    assert len(visible_elements) == 5


def test_footer_blocks(browser, url):
    browser.get(url + "/desktops")
    footer_blocks = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((CatalogPage.FOOTER_BLOCKS)))
    assert len(footer_blocks) == 4, f"Expected 4 footer blocks, but found {len(footer_blocks)}"


def test_products_image_visibility(browser, url):
    browser.get(url + "/desktops")
    image_elements = WebDriverWait(browser, 3).until(EC.visibility_of_all_elements_located((CatalogPage.IMAGES)))
    assert len(image_elements) == 12, f"Expected 12 image elements, but found {len(image_elements)}"
    for image in image_elements:
        assert image.is_displayed(), "One or more images are not visible."
