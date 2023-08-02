from page_objects.card_page import CardPage

# refactored tests start


def test_check_title(driver, url):
    card_page = CardPage(driver)
    card_page.open(url)
    card_page.verify_title("MacBook")


def test_check_dropdown_menu(driver, url):
    card_page = CardPage(driver)
    card_page.open(url)
    card_page.find_dropdown_menu()


def test_add_to_cart_button(driver, url):
    card_page = CardPage(driver)
    card_page.open(url)
    card_page.find_add_to_cart_button()


def test_add_to_wish_list(driver, url):
    card_page = CardPage(driver)
    card_page.open(url)
    card_page.find_add_to_wish_list()


def test_check_tabs(driver, url):
    card_page = CardPage(driver)
    card_page.open(url)
    tab_elements = card_page.find_navigation_tabs()
    assert len(tab_elements) == 3
# refactored tests end
