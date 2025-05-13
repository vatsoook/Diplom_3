from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке перехода в личный кабинет в шапке сервиса')
    def click_on_personal_account_button(self):
        self.wait_visibility_of_element(MainPageLocators.personal_account_button )
        self.click_on_element(MainPageLocators.personal_account_button )

    @allure.step('Кликнуть по кнопке "Лента заказов" в шапке сервиса')
    def click_button_order_feed_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.button_order_feed_in_header)
        self.click_on_element(MainPageLocators.button_order_feed_in_header)

    @allure.step('Переход на страницу конструктора')
    def click_constructor_header(self):
        self.wait_visibility_of_element(MainPageLocators.constructor_header)
        self.click_on_element(MainPageLocators.constructor_header)

    @allure.step('Получение главного заголовка конструктора')
    def get_constructor_title_text(self):
        return self.get_text_on_element(MainPageLocators.constructor_title)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_login_button(self):
        self.click_on_element(MainPageLocators.login_button_on_main)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        self.wait_visibility_of_element(MainPageLocators.order_number_in_confirmation_modal)
        return self.check_displaying_of_element(MainPageLocators.order_number_in_confirmation_modal)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.ingredient_1)
        self.click_on_element(MainPageLocators.ingredient_1)

    @allure.step('Проверить отображение окна "Детали ингредиента"')
    def is_ingredient_details_modal_displayed(self):
        self.wait_visibility_of_element(MainPageLocators.header_of_modal_details)
        return self.check_displaying_of_element(MainPageLocators.header_of_modal_details)

    @allure.step('Проверить, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_of_modal_details(self):
        self.wait_for_closing_of_element(MainPageLocators.header_of_modal_details)
        if not self.check_displaying_of_element(MainPageLocators.header_of_modal_details):
            return True

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_details_modal(self):
        self.wait_visibility_of_element(MainPageLocators.button_close_modal)
        self.click_on_element(MainPageLocators.button_close_modal)

    @allure.step('Добавить ингредиенты')
    def drag_and_drop_ingredient_to_order(self):
        source_element = self.find_element_with_wait(MainPageLocators.burger_ingredient)
        target_element = self.find_element_with_wait(MainPageLocators.place_for_ingredients)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_ingredient_counter(self):
        return self.get_text_on_element(MainPageLocators.ingredient_counter)

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_submit_order_button(self):
        self.click_on_element(MainPageLocators.submit_order_button)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_order_confirmation_modal(self):
        return self.check_displaying_of_element(MainPageLocators.order_confirmation_modal)

    @allure.step('Получить номер в окне о создании заказа')
    def get_order_number_in_confirmation_modal(self):
        self.wait_for_element_to_change_text(MainPageLocators.order_number_in_confirmation_modal, '9999')
        return self.get_text_on_element(MainPageLocators.order_number_in_confirmation_modal)

    @allure.step('Кликнуть на кнопку закрытия окна о создании заказа')
    def click_close_confirmation_button(self):
        self.check_element_is_clickable(MainPageLocators.close_confirmation_button)
        self.click_on_element(MainPageLocators.close_confirmation_button)