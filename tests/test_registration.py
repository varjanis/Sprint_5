from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from random import randint


def generate_email():
    random_numbers = randint(1, 999)

    return f'zvolinskaya_3_{random_numbers}@mail.ru'


class TestRegistration:

    def test_registration_correct_credentials_success(self, driver):
        driver.get(Locators.page_url_registration_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_registration_page_input_name).send_keys('Александра')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_registration_page_input_email).send_keys(generate_email())
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_registration_page_input_password).send_keys('1234567890')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_registration_page_registration_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.locator_login_page_login_button))

        assert driver.current_url == Locators.page_url_login_page

    def test_registration_too_short_password_fail(self, driver):
        driver.get(Locators.page_url_registration_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_registration_page_input_name).send_keys('Александра')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_registration_page_input_email).send_keys(generate_email())
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_registration_page_input_password).send_keys('1234')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_registration_page_registration_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.locator_registration_page_invalid_password))

        assert driver.find_element(*Locators.locator_registration_page_invalid_password).text == 'Некорректный пароль'

