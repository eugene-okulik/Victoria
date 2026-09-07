from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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


def test_add_to_cart_popup(driver):
    driver.get("http://testshop.qa-practice.com/")
    item = driver.find_element(By.CSS_SELECTOR, '[alt="Customizable Desk"]')
    cart_button = driver.find_element(By.CSS_SELECTOR, '[title="Shopping cart"]')
    actions = ActionChains(driver)
    actions.move_to_element(item)
    actions.move_to_element(cart_button)
    actions.click()
    actions.perform()
    wait = WebDriverWait(driver, 10)
    add_to_cart_modal = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.product_display_name')
        )
    )
    assert "Customizable Desk" in add_to_cart_modal.text
