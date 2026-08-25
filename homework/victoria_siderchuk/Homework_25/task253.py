from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_choose_language(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    language_selector = driver.find_element(By.ID, 'id_choose_language')
    language_selector.click()
    language_data = Select(language_selector)
    language_data.select_by_value('1')
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    submit_result = driver.find_element(By.ID, 'result-text')
    assert submit_result.text == "Python"


def test_hello_world(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.TAG_NAME, 'button')
    start_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, 'finish'),
            'Hello World'
        )
    )
