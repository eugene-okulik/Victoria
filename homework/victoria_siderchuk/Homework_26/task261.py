from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_add_to_cart(driver):
    driver.get("http://testshop.qa-practice.com/")
    item = driver.find_element(By.CSS_SELECTOR, '[content="Customizable Desk"]')
    ActionChains(driver).key_down(Keys.CONTROL).click(item).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    wait = WebDriverWait(driver, 10)
    add_to_cart_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, 'add_to_cart')
        )
    )
    add_to_cart_button.click()
    wait = WebDriverWait(driver, 10)
    continue_shopping_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.btn-secondary')
        )
    )
    continue_shopping_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '.my_cart_quantity'), "1")
    )
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.CSS_SELECTOR, '.o_wsale_my_cart').click()
    item_in_cart = driver.find_element(By.CSS_SELECTOR, '.d-inline')
    assert item_in_cart.text == 'Customizable Desk (Steel, White)'
