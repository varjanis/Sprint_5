from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRedirectFromPersonalCabinetToConstructor():

    def test_redirect_from_personal_cabinet_to_constructor_via_constructor_button_success(self, driver):

        driver.get(Locators.page_url_login_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_email).send_keys('zvolinskaya_3@gmail.com')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_password).send_keys('1234567890')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        driver.find_element(*Locators.locator_main_page_profile_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.locator_profile_page_logout_button))

        driver.find_element(*Locators.locator_profile_page_constructor_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        assert driver.current_url == Locators.page_url_main_page

    def test_redirect_from_personal_cabinet_to_constructor_via_burger_logo(self, driver):

        driver.get(Locators.page_url_login_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_email).send_keys('zvolinskaya_3@gmail.com')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_password).send_keys('1234567890')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        driver.find_element(*Locators.locator_main_page_profile_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.locator_profile_page_logout_button))

        driver.find_element(*Locators.locator_profile_page_header_logo).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        assert driver.current_url == Locators.page_url_main_page

