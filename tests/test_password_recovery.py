from selenium import webdriver
import pytest
from pages.page_password_recovery import PagePasswordRecovery
from constants import main_url, forgot_password_url, reset_password_url
import allure

class TestPasswordRecovery:
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @allure.title("Тест перехода на страницу восстановления пароля")
    @pytest.mark.usefixtures("driver")
    def test_page_password_recovery(self):
        self.driver.get(main_url)
        client = PagePasswordRecovery(self.driver)
        client.check_password_recovery_page()
        assert self.driver.current_url == forgot_password_url

    @allure.title("Тест ввода почты и нажатия на кнопку восстановить")
    @pytest.mark.usefixtures("driver")
    def test_input_email_and_button_recovery(self):
        self.driver.get(main_url)
        client = PagePasswordRecovery(self.driver)
        client.check_input_email_password_recovery_page()
        assert self.driver.current_url == reset_password_url

    @allure.title("Тест ввода почты и нажатия на кнопку восстановить")
    @pytest.mark.usefixtures("driver")
    def test_is_active_input_password(self):
        self.driver.get(main_url)
        client = PagePasswordRecovery(self.driver)
        result = client.check_focused_input_password_recovery()
        assert result == True




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()










