from selenium.webdriver.common.by import By


class Locators():

    # адреса страниц сайта

    page_url_login_page = "https://stellarburgers.nomoreparties.site/login"
    page_url_registration_page = "https://stellarburgers.nomoreparties.site/register"
    page_url_profile_page = "https://stellarburgers.nomoreparties.site/account/profile"
    page_url_main_page = "https://stellarburgers.nomoreparties.site/"
    page_url_forgot_password_page = "https://stellarburgers.nomoreparties.site/forgot-password"

    # локаторы страницы восстановления пароля

    locator_forgot_password_page_login_link = (By.XPATH, './/a[@class="Auth_link__1fOlj" and @href="/login"]')

    # локаторы страницы регистрации

    locator_registration_page_input_name = (By.XPATH, './/*[text()="Имя"]/following-sibling::input')

    locator_registration_page_input_email = (By.XPATH, './/*[text()="Email"]/following-sibling::input')

    locator_registration_page_input_password = (By.XPATH, './/*[text()="Пароль"]/following-sibling::input')

    locator_registration_page_registration_button = (
        By.XPATH,
        './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Зарегистрироваться"]'
    )
    locator_registration_page_invalid_password = (By.XPATH, './/p[@class="input__error text_type_main-default"]')

    locator_registration_page_personal_cabinet_button = (
        By.XPATH, './/p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Личный Кабинет"]')

    locator_registration_page_already_registered_login_link = (By.XPATH,
                                                               './/a[@class="Auth_link__1fOlj" and @href="/login"]')

    # локаторы страницы авторизации

    locator_login_page_input_email = (By.XPATH,
                                      './/input[@class="text input__textfield text_type_main-default" and @type="text"]')

    locator_login_page_input_password = (
        By.XPATH, './/input[@class="text input__textfield text_type_main-default" and @type="password"]'
    )

    locator_login_page_login_button = (
        By.XPATH,
        './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Войти"]'
    )

    # локаторы главной страницы

    locator_main_page_order_button = (
        By.XPATH,
        './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    )
    locator_main_page_profile_button = (
        By.XPATH, './/p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Личный Кабинет"]')

    # локаторы вкладок конструктора бургеров

    locator_constructor_page_buns_folder = (
    By.XPATH, './/span[@class="text text_type_main-default" and text()="Булки"]')

    locator_constructor_page_sauces_folder = (
    By.XPATH, './/span[@class="text text_type_main-default" and text()="Соусы"]')

    locator_constructor_page_fillers_folder = (
    By.XPATH, './/span[@class="text text_type_main-default" and text()="Начинки"]')

    locator_constructor_page_fillers_proof_element = (
    By.XPATH, './/p[@class="BurgerIngredient_ingredient__text__yp3dH" and text()="Говяжий метеорит (отбивная)"]')

    locator_constructor_page_sauces_proof_element = (By.XPATH,
                                                     './/p[@class="BurgerIngredient_ingredient__text__yp3dH" and text()="Соус с шипами Антарианского плоскоходца"]')

    locator_constructor_page_buns_proof_element = (
    By.XPATH, './/p[@class="BurgerIngredient_ingredient__text__yp3dH" and text()="Краторная булка N-200i"]')


    # локаторы страницы профиля (личный кабинет пользователя)

    locator_profile_page_header_logo = (By.XPATH, './/a[@href = "/"]')

    locator_profile_page_constructor_button = (By.XPATH, './/a[@class="AppHeader_header__link__3D_hX" and @href="/"]')

    locator_profile_page_logout_button = (
        By.XPATH, './/button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]'
    )







