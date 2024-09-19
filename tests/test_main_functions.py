from selenium import webdriver
from pages.main_page import MainPage
from constants import main_url, account_url, history_orders_url, login_url, lenta_url
import pytest
import allure


class TestMainFunctions:
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @allure.title("Проверка кнопки конструктора")
    @pytest.mark.usefixtures("driver")
    def test_button_construction(self):
        self.driver.get(lenta_url)
        client = MainPage(self.driver)
        client.check_button_constructor()
        assert self.driver.current_url == main_url

    @allure.title("Проверка кнопки ленты заказов")
    @pytest.mark.usefixtures("driver")
    def test_button_lenta(self):
        self.driver.get(main_url)
        client = MainPage(self.driver)
        client.check_button_lenta()
        assert self.driver.current_url == lenta_url

    @allure.title("Тест открытия модального окна ингредиента")
    @pytest.mark.usefixtures("driver")
    def test_modal_open(self):
        self.driver.get(main_url)
        client = MainPage(self.driver)
        text = client.check_button_ingredient_modal()
        assert text == 'Детали ингредиента'

    @allure.title("Тест закрытия модального окна ингредиента")
    @pytest.mark.usefixtures("driver")
    def test_modal_close(self):
        self.driver.get(main_url)
        client = MainPage(self.driver)
        result = client.check_modal_close()
        assert result == 'Modal closed'

    @allure.title("Тест увеличения каунтера ингредиентов")
    @pytest.mark.usefixtures("driver")
    def test_counter_plus(self):
        self.driver.get(main_url)
        client = MainPage(self.driver)
        result = client.check_drag_and_drop_ingredient_counter()
        assert result == '2'

    @allure.title("Тест оформления заказа авторизованным юзером")
    @pytest.mark.usefixtures("driver")
    def test_auth_user_order_confirm(self):
        self.driver.get(main_url)
        client = MainPage(self.driver)
        result = client.check_auth_user_order_confirm()
        assert result == 'Ваш заказ начали готовить'



















