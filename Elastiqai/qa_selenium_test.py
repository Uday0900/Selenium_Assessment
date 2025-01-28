from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

# Using pytest fixture for the driver
@pytest.fixture(scope="module")
def browser():
    # Setup WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown
    driver.quit()

def test_table_search_functionality(browser):
    # Navigate to the Selenium Playground Table Search Demo
    browser.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    
    # Find the search input box and enter "New York"
    search_box = browser.find_element(By.XPATH, "//*[@type='search']")
    search_box.clear()
    time.sleep(3)
    search_box.send_keys("New York")
    
    # Wait for the page to load the results
    time.sleep(3)
    
    # Validate the search results and get the rows in the table after the search
    rows = browser.find_elements(By.XPATH, "//table[@id='example']//tbody//tr")
    print(len(rows))
    
    # Assert that there are 5 results
    assert len(rows) == 5, f"Expected 5 rows, but got {len(rows)}"

    # Validate the total entries shown table result
    total_entries_text = browser.find_element(By.XPATH, "//div[@id='example_info']").text
    assert "Showing 1 to 5 of 5 entries (filtered from 24 total entries)" in total_entries_text, f"Unexpected text: {total_entries_text}"
