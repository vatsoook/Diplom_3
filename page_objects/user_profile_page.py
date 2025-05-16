from page_objects.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators
import allure


class UserProfilePage(BasePage):
    @allure.step('Кликнуть по кнопке "История заказов"')
    def click_on_order_history_button(self):
        self.click_on_element(PersonalAccountPageLocators.order_history)

    @allure.step('Кликнуть по кнопке "Выйти"')
    def click_on_logout_button(self):
        self.click_on_element(PersonalAccountPageLocators.button_logout)

    @allure.step('Подождать прогрузки текста описания раздела')
    def wait_visibility_of_description(self):
        self.wait_visibility_of_element(PersonalAccountPageLocators.description_of_section)

    @allure.step('Проверить отображение описания раздела')
    def check_displaying_of_description(self):
        return self.check_displaying_of_element(PersonalAccountPageLocators.description_of_section)

    @allure.step('Подождать прогрузки кнопки "Зарегистрироваться"')
    def wait_visibility_of_button_register(self):
        self.wait_visibility_of_element(PersonalAccountPageLocators.button_register)

    @allure.step('Проверить отображение кнопки "Зарегистрироваться"')
    def check_displaying_of_button_register(self):
        return self.check_displaying_of_element(PersonalAccountPageLocators.button_register)