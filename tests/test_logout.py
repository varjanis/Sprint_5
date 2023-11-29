import time
from selenium.webdriver.common.by import By


def test_login_via_login_button_success(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[1]/div/div/input').send_keys('zvolinskaya_3@gmail.com')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/fieldset[2]/div/div/input').send_keys('1234567890')
    time.sleep(2)

    driver.find_element(By.XPATH, './/main/div/form/button').click()
    time.sleep(5)

    driver.find_element(By.XPATH, './/header/nav/a/p').click()
    time.sleep(5)

    driver.find_element(By.XPATH, './/main/div/nav/ul/li[3]/button').click()
    time.sleep(5)

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    driver.quit()
