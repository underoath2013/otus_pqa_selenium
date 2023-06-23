from page_objects import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_check_title(browser, url):
    browser.get(url)
    WebDriverWait(browser, 3).until(EC.title_is("Your Store"))


def test_check_logo(browser, url):
    browser.get(url)
    logo = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((MainPage.LOGO)))
    assert logo.is_displayed()


def test_items_navigation_bar(browser, url):
    navigation_bar_items = ["Desktops", "Laptops & Notebooks", "Components",
                            "Tablets", "Software", "Phones & PDAs", "Cameras", "MP3 Players"]
    browser.get(url)
    navigation_bar = WebDriverWait(browser, 3).until(EC.visibility_of_all_elements_located((MainPage.NAVIGATION_BAR)))
    assert len(navigation_bar) == 8, "Wrong items quantity in navigation bar"
    for element in navigation_bar:
        assert element.text in navigation_bar_items, f"Unexpected item in navigation bar: {element.text}"


def test_search_field_button(browser, url):
    search_input = "Macbook"
    browser.get(url)
    search_field = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((MainPage.SEARCH_INPUT)))
    search_field.click()
    search_field.clear()
    search_field.send_keys(search_input)
    search_button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((MainPage.SEARCH_BUTTON)))
    search_button.click()
    WebDriverWait(browser, 5).until(EC.title_contains(search_input))


def test_featured_items(browser, url):
    featured_item_titles = ['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']
    browser.get(url)
    featured_items = WebDriverWait(browser, 3).until(EC.visibility_of_all_elements_located(MainPage.FEATURED))
    assert len(featured_items) == 4, f"Expected 4 items in 'Featured', but found {len(featured_items)}"
    for item in featured_items:
        item_title = item.find_element(By.TAG_NAME, "h4").find_element(By.TAG_NAME, "a").text
        assert item_title in featured_item_titles, f"Unexpected item in featured: {item_title}"
