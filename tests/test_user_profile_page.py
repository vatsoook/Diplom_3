from page_objects.user_profile_page import UserProfilePage
from page_objects.main_page import MainPage
from page_objects.chapter_order_history_page import ChapterOrderHistoryPage
from conftest import *
import allure


class TestUserProfilePage:
    @allure.title('Проверка переход к профилю по клику на "Личный кабинет" в шапке сервиса')
    def test_navigate_to_user_profile_successful(self, driver, set_user_tokens):
        home_page = MainPage(driver)
        user_profile_page = UserProfilePage(driver)
        home_page.click_on_personal_account_button()
        user_profile_page.wait_visibility_of_description()
        assert user_profile_page.check_displaying_of_description() is True

    @allure.title('Проверка перехода по клику в раздел «История заказов»')
    def test_navigation_to_order_history(self, driver, set_user_tokens, create_user_and_order_and_delete):
        home_page = MainPage(driver)
        user_profile_page = UserProfilePage(driver)
        chapter_order_history_page = ChapterOrderHistoryPage(driver)
        home_page.click_on_personal_account_button()
        user_profile_page.wait_visibility_of_description()
        user_profile_page.click_on_order_history_button()
        chapter_order_history_page.wait_visibility_of_order_card()
        assert 'бургер' in chapter_order_history_page.get_text_of_order_card_title()

    @allure.title('Проверка функциональности выхода из системы с помощью кнопки "Выход"')
    def test_successful_logout (self, driver, set_user_tokens):
        home_page = MainPage(driver)
        user_profile_page = UserProfilePage(driver)
        home_page.click_on_personal_account_button()
        user_profile_page.wait_visibility_of_description()
        user_profile_page.click_on_logout_button()
        user_profile_page.wait_visibility_of_button_register()
        assert user_profile_page.check_displaying_of_button_register()