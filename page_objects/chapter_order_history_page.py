from locators.chapter_order_history_page_locators import ChapterOrderHistoryPageLocators
from page_objects.base_page import BasePage
import allure


class ChapterOrderHistoryPage(BasePage):

    @allure.step('Подождать прогрузки карточки заказа')
    def wait_visibility_of_order_card(self):
        self.wait_visibility_of_element(ChapterOrderHistoryPageLocators.order_card)

    @allure.step('Получить текст карточки заказа')
    def get_text_of_order_card_title(self):
        return self.get_text_on_element(ChapterOrderHistoryPageLocators.order_card_title)

    @allure.step('Получить номер заказа в карточке')
    def get_id_of_order_card(self):
        return self.get_text_on_element(ChapterOrderHistoryPageLocators.order_card_id)