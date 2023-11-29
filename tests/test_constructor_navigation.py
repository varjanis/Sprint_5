import time
from selenium.webdriver.common.by import By


def test_constructor_redirect_to_fillers_success(driver):

    driver.get("https://stellarburgers.nomoreparties.site/login")
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[1]/div/div/input').send_keys('zvolinskaya_3@gmail.com')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[2]/div/div/input').send_keys('1234567890')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/button').click()
    time.sleep(5)

    driver.find_element(By.XPATH, './/main/section[1]/div/div[3]').click()
    time.sleep(5)

    driver.quit()


def test_constructor_redirect_to_sauces_success(driver):

    driver.get("https://stellarburgers.nomoreparties.site/login")
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[1]/div/div/input').send_keys('zvolinskaya_3@gmail.com')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[2]/div/div/input').send_keys('1234567890')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/button').click()
    time.sleep(5)

    driver.find_element(By.XPATH, './/main/section[1]/div/div[2]').click()
    time.sleep(5)

    driver.quit()


def test_constructor_redirect_to_buns_success(driver):

    driver.get("https://stellarburgers.nomoreparties.site/login")
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[1]/div/div/input').send_keys('zvolinskaya_3@gmail.com')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[2]/div/div/input').send_keys('1234567890')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/button').click()
    time.sleep(5)

    driver.find_element(By.XPATH, './/main/section[1]/div/div[3]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/section[1]/div/div[1]').click()
    time.sleep(5)

    driver.quit()


