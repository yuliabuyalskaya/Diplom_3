import allure
import pytest
from constants import main_url, lenta_url
from pages.lenta_orders_page import LentaPage


class TestLenta:
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @allure.title("Тест модального окна заказа")
    @pytest.mark.usefixtures("driver")
    def test_modal_order(self):
        self.driver.get(lenta_url)
        client = LentaPage(self.driver)
        result = client.check_click_order_modal()
        assert len(result) > 0



    @allure.title("Тест появления заказа в ленте заказов")
    @pytest.mark.usefixtures("driver")
    def test_orders_from_history_in_lenta(self):
        self.driver.get(main_url)
        client = LentaPage(self.driver)
        result = client.check_orders_from_history_in_lenta()
        assert result == False





    @allure.title("Тест увеличения общего каунтера при оформлении заказа")
    @pytest.mark.usefixtures("driver")
    def test_counter_all_orders_with_my_order(self):
        self.driver.get(main_url)
        client = LentaPage(self.driver)
        result = client.check_counter_all_oders()
        assert result == True




    @allure.title("Тест увеличения каунтера за сегодня при оформлении заказа")
    @pytest.mark.usefixtures("driver")
    def test_counter_today_orders_with_my_order(self):
        self.driver.get(main_url)
        client = LentaPage(self.driver)
        result = client.check_orders_today()
        assert result == True



    @allure.title("Тест отображения заказа в работе")
    @pytest.mark.usefixtures("driver")
    def test_mo_order_in_work(self):
        self.driver.get(main_url)
        client = LentaPage(self.driver)
        result = client.check_omy_order_in_work()
        assert result == False











