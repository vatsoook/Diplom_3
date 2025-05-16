from page_objects.password_recovery_page import PasswdRecoveryPage
from page_objects.main_page import MainPage
from conftest import *
import allure


class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_navigate_to_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.going_recovery_page()
        assert recovery_page.check_email_input_displayed()

    @allure.title('Проверка перехода к восстановлению пароля при вводе валидного email и нажатии кнопки "Восстановить"')
    def test_click_recovery_button_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.going_recovery_page()
        recovery_page.send_email()
        recovery_page.click_recovery_button()
        assert recovery_page.check_displaying_of_input_password()

    @allure.title('Проверка отображения пароля в поле ввода после клика на иконку с глазом')
    def test_click_on_eye_icon_makes_passwd_visible_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.going_recovery_page()
        recovery_page.send_email()
        recovery_page.click_recovery_button()
        recovery_page.send_password()
        recovery_page.сlick_on_the_icon_screen()
        assert recovery_page.check_displaying_password_value()

    @allure.title('Проверка, что пароль замаскирован после двойного щелчка по значку глаза')
    def test_double_eye_icon_click_masks_password(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button()
        recovery_page = PasswdRecoveryPage(driver)
        recovery_page.going_recovery_page()
        recovery_page.send_email()
        recovery_page.click_recovery_button()
        recovery_page.send_password()
        recovery_page.сlick_on_the_icon_screen()
        recovery_page.сlick_on_the_icon_screen()
        assert recovery_page.check_not_displaying_password_value()


