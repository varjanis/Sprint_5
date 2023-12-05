from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin():
    def test_login_via_login_button_success(self, driver):
        driver.get(Locators.page_url_login_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_email).send_keys('zvolinskaya_3@gmail.com')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_password).send_keys('1234567890')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        assert driver.current_url == Locators.page_url_main_page

    def test_login_via_personal_cabinet_button_success(self, driver):

        driver.get(Locators.page_url_registration_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_registration_page_personal_cabinet_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.locator_login_page_login_button))

        driver.find_element(*Locators.locator_login_page_input_email).send_keys('zvolinskaya_3@gmail.com')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_password).send_keys('1234567890')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_login_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        assert driver.current_url == Locators.page_url_main_page

    def test_login_via_registration_form_button_success(self, driver):

        driver.get(Locators.page_url_registration_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_registration_page_already_registered_login_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.locator_login_page_login_button))

        driver.find_element(*Locators.locator_login_page_input_email).send_keys('zvolinskaya_3@gmail.com')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_password).send_keys('1234567890')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_login_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        assert driver.current_url == Locators.page_url_main_page

    def test_login_via_forgot_password_form_button_success(self, driver):

        driver.get(Locators.page_url_forgot_password_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_forgot_password_page_login_link).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.locator_login_page_login_button))

        driver.find_element(*Locators.locator_login_page_input_email).send_keys('zvolinskaya_3@gmail.com')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_password).send_keys('1234567890')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_login_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        assert driver.current_url == Locators.page_url_main_page







