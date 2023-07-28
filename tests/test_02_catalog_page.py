from page_objects.catalog_page import CatalogPage

# refactored tests start


def test_check_title(driver, url):
    catalog_page = CatalogPage(driver)
    catalog_page.open(url)
    catalog_page.verify_title("Desktops")


def test_check_logo(driver, url):
    catalog_page = CatalogPage(driver)
    catalog_page.open(url)
    catalog_page.find_logo()


def test_elements_in_top_rigth_navigation_bar(driver, url):
    catalog_page = CatalogPage(driver)
    catalog_page.open(url)
    nav_bar = catalog_page.find_top_right_navigation_bar()
    visible_elements = catalog_page.visible_elements_in_top_right_navigation_bar(nav_bar)
    assert len(visible_elements) == 5


def test_footer_blocks(driver, url):
    catalog_page = CatalogPage(driver)
    catalog_page.open(url)
    footer_blocks = catalog_page.find_footer_blocks()
    assert len(footer_blocks) == 4, f"Expected 4 footer blocks, but found {len(footer_blocks)}"


def test_products_image_visibility(driver, url):
    catalog_page = CatalogPage(driver)
    catalog_page.open(url)
    image_elements = catalog_page.find_product_images()
    assert len(image_elements) == 12, f"Expected 12 image elements, but found {len(image_elements)}"
# refactored tests end
