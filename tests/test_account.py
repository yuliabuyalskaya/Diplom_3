from selenium import webdriver
import pytest
from pages.page_account import PageAccount
from constants import main_url, account_url, history_orders_url, login_url
import allure

class TestAccount:

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


    @allure.title("Тест перехода на страницу восстановления пароля")
    @pytest.mark.usefixtures("driver")
    def test_transition_in_account(self):
        self.driver.get(main_url)
        client = PageAccount(self.driver)
        client.check_transicion_in_account()
        assert self.driver.current_url == account_url




    @allure.title("Тест перехода в раздел истории заказов")
    @pytest.mark.usefixtures("driver")
    def test_button_history_orders(self):
        self.driver.get(main_url)
        client = PageAccount(self.driver)
        client.check_button_history_orders()
        assert self.driver.current_url == history_orders_url



    @allure.title("Тест выхода из аккаунта")
    @pytest.mark.usefixtures("driver")
    def test_sign_out(self):
        self.driver.get(main_url)
        client = PageAccount(self.driver)
        client.check_button_sign_out()
        assert self.driver.current_url == login_url


