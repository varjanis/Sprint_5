import time
from selenium.webdriver.common.by import By


def test_registration_correct_credentials_success(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[1]/div/div/input').send_keys('Александра')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[2]/div/div/input').send_keys('zvolinskaya_3_111@gmail.com')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[3]/div/div/input').send_keys('1234567890')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/button').click()
    time.sleep(5)

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()


def test_registration_too_short_password_fail(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[1]/div/div/input').send_keys('Александра')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[2]/div/div/input').send_keys('zvolinskayatest1@gmail.com')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[3]/div/div/input').send_keys('1234')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/button').click()
    time.sleep(2)

    assert driver.find_element(By.XPATH, '//main/div/form/fieldset[3]/div/p').text == 'Некорректный пароль'

    driver.quit()
