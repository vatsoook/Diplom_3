from page_objects.order_feed_page import OrderFeedPage
from page_objects.main_page import MainPage
from page_objects.chapter_order_history_page import ChapterOrderHistoryPage
from page_objects.user_profile_page import UserProfilePage
from conftest import *
import allure


class TestOrderFeedPage:

    @allure.title('Проверка того что при клике на заказ открывается всплывающее окно с деталями')
    def test_displaying_modal_order_details_success(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_button_order_feed_in_header()
        order_feed_page.click_on_order_card()
        assert 'бургер' in order_feed_page.get_text_on_title_of_modal_order()

    @allure.title('Проверка отображения заказа пользователя из раздела «История заказов» в ленте заказов')
    def test_displaying_in_feed_new_order_user_from_history_success(self, driver, create_user_and_order_and_delete,
                                                               set_user_tokens):
        main_page = MainPage(driver)
        personal_account_page = UserProfilePage(driver)
        chapter_order_history_page = ChapterOrderHistoryPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_on_personal_account_button()
        personal_account_page.click_on_order_history_button()
        order_id = chapter_order_history_page.get_id_of_order_card()
        main_page.click_button_order_feed_in_header()
        assert order_feed_page.check_id_order_in_feed(order_id)

    @allure.title('Проверка увеличения числа на счетчике выполненных за все время заказов')
    def test_changes_counter_for_quantity_of_all_orders_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_button_order_feed_in_header()
        orders_count_1 = order_feed_page.get_quantity_of_orders()
        main_page.click_constructor_header()
        main_page.click_login_button()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_submit_order_button()
        main_page.click_close_confirmation_button()
        main_page.click_button_order_feed_in_header()
        orders_count_2 = order_feed_page.get_quantity_of_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка увеличения числа на счетчике выполненных за сегодня заказов')
    def test_changes_counter_for_daily_quantity_of_orders_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_button_order_feed_in_header()
        orders_count_1 = order_feed_page.get_daily_quantity_of_orders()
        main_page.click_constructor_header()
        main_page.click_login_button()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_submit_order_button()
        main_page.click_close_confirmation_button()
        main_page.click_button_order_feed_in_header()
        orders_count_2 = order_feed_page.get_daily_quantity_of_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка появления номера заказа в разделе "В работе"')
    def test_displaying_new_order_in_progress_section_work_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_login_button()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_submit_order_button()
        new_order_id = main_page.get_order_number_in_confirmation_modal()
        main_page.click_close_confirmation_button()
        main_page.click_button_order_feed_in_header()
        assert order_feed_page.get_order_number_in_feed_progress_section() == '0'+new_order_id