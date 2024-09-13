import pytest
#
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from constants import main_url, login_url, reset_password_url


class PagePasswordRecovery(BasePage):
    button_sign_in = [By.CSS_SELECTOR, ".button_button__33qZ0"]
    button_recovery_password = [By.XPATH, "/html/body/div/div/main/div/div/p[2]/a"]
    input_email_recovery_password = [By.CLASS_NAME, "input__textfield"]
    button_recovery = [By.CLASS_NAME, "button_button__33qZ0"]
    button_see_password = [By.CSS_SELECTOR, ".input__icon > svg:nth-child(1)"]
    input_placeholder_focused = [By.CLASS_NAME, "input_placeholder_focused"]
    is_active_input = [By.CLASS_NAME, 'input_status_active']




    def __init__(self,driver):
        super().__init__(driver)

    @allure.step("Проверка перехода на странице восстановления пароля")
    def check_password_recovery_page(self):
        self.click_virt_mouse(self.button_sign_in)
        self.click_virt_mouse(self.button_recovery_password)
        self.wait(self.button_recovery)


    @allure.step("Проверка ввода почты на странице восстановлени пароля")
    def check_input_email_password_recovery_page(self):
        self.click_virt_mouse(self.button_sign_in)
        self.click_virt_mouse(self.button_recovery_password)
        self.click_virt_mouse(self.input_email_recovery_password)
        self.fill_input(self.input_email_recovery_password, '0120ree@mail.ru')
        self.click_virt_mouse(self.button_recovery)
        self.wait_url_change(reset_password_url)


    @allure.step("Проверка активности поля ввода пароля")
    def check_focused_input_password_recovery(self):
        self.click_virt_mouse(self.button_sign_in)
        self.click_virt_mouse(self.button_recovery_password)
        self.click_virt_mouse(self.input_email_recovery_password)
        self.fill_input(self.input_email_recovery_password, '0120ree@mail.ru')
        self.click_virt_mouse(self.button_recovery)
        self.wait_url_change(reset_password_url)
        self.click(self.button_see_password)
        self.wait(self.is_active_input)
        return true

        #надо доделать с подсветкой


