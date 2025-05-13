from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage
from conftest import *
import allure


class TestMainPageFunctionality:
    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_successful_navigate_to_constructor(self, driver):
        main_page_instance = MainPage(driver)
        main_page_instance.click_button_order_feed_in_header()
        main_page_instance.click_constructor_header()
        assert 'Соберите бургер' in main_page_instance.get_constructor_title_text()

    @allure.title('Проверка перехода по клику на "Ленту заказов"')
    def test_successful_navigate_to_order_history(self, driver):
        main_page_instance = MainPage(driver)
        order_history_page = OrderFeedPage(driver)
        main_page_instance.click_button_order_feed_in_header()
        assert order_history_page.get_orders_list_title_text() == 'Лента заказов'

    @allure.title('Проверка отображения окна "Детали ингредиента" при клике на ингредиент')
    def test_successful_display_ingredient_details_modal(self, driver):
        main_page_instance = MainPage(driver)
        main_page_instance.click_on_ingredient()
        assert main_page_instance.is_ingredient_details_modal_displayed()

    @allure.title('Проверка закрытия окна "Детали ингредиента" кликом по крестику')
    def test_successful_close_ingredient_details_modal(self, driver):
        main_page_instance = MainPage(driver)
        main_page_instance.click_on_ingredient()
        main_page_instance.close_details_modal()
        assert main_page_instance.is_ingredient_details_modal_displayed()

    @allure.title('Проверка увеличения числа на счетчике при добавлении ингредиента в заказ')
    def test_successful_increment_counter_for_order_ingredients(self, driver):
        main_page_instance = MainPage(driver)
        main_page_instance.drag_and_drop_ingredient_to_order()
        assert main_page_instance.get_ingredient_counter() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_successful_order_placement_by_authenticated_user(self, driver, set_user_tokens):
        main_page_instance = MainPage(driver)
        main_page_instance.click_login_button()
        main_page_instance.drag_and_drop_ingredient_to_order()
        main_page_instance.click_submit_order_button()
        assert main_page_instance.check_order_confirmation_modal()
