from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorNavigation():

    def test_constructor_redirect_to_fillers_success(self, driver):

        driver.get(Locators.page_url_login_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_email).send_keys('zvolinskaya_3@gmail.com')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_password).send_keys('1234567890')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        driver.find_element(*Locators.locator_constructor_page_fillers_folder).click()
        WebDriverWait(driver, 3)

        assert driver.find_element(*Locators.locator_constructor_page_fillers_proof_element).text == 'Говяжий метеорит (отбивная)'

    def test_constructor_redirect_to_sauces_success(self, driver):

        driver.get(Locators.page_url_login_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_email).send_keys('zvolinskaya_3@gmail.com')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_password).send_keys('1234567890')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        driver.find_element(*Locators.locator_constructor_page_sauces_folder).click()
        WebDriverWait(driver, 3)

        assert driver.find_element(*Locators.locator_constructor_page_sauces_proof_element).text == 'Соус с шипами Антарианского плоскоходца'

    def test_constructor_redirect_to_buns_success(self, driver):

        driver.get(Locators.page_url_login_page)
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_email).send_keys('zvolinskaya_3@gmail.com')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_input_password).send_keys('1234567890')
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_login_page_login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.locator_main_page_order_button))

        driver.find_element(*Locators.locator_constructor_page_fillers_folder).click()
        WebDriverWait(driver, 3)

        driver.find_element(*Locators.locator_constructor_page_buns_folder).click()
        WebDriverWait(driver, 3)

        assert driver.find_element(*Locators.locator_constructor_page_buns_proof_element).text == 'Краторная булка N-200i'



