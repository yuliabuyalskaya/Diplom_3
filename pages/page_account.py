import allure
from selenium.webdriver.common.by import By
from constants import main_url, history_orders_url, login_url
from pages.base_page import BasePage




class PageAccount(BasePage):
    button_personal_account = [By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX:nth-child(3) > p:nth-child(2)"]
    input_email = [By.NAME, 'name']
    input_password = [By.NAME, 'Пароль']
    button_sign_in = [By.CSS_SELECTOR, '.button_button__33qZ0']
    button_history_orders = [By.CSS_SELECTOR, 'li.Account_listItem__35dAP:nth-child(2) > a:nth-child(1)']
    button_sign_out = [By.CLASS_NAME, 'Account_button__14Yp3']





    @allure.step("Проверка перехода в аккаунт")
    def check_transicion_in_account(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        self.wait_url_change(main_url)
        try:
            self.click_virt_mouse(self.button_personal_account)
        except:
            self.click_virt_mouse(self.button_personal_account)




    @allure.step("Проверка кнопки истории заказов")
    def check_button_history_orders(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        self.wait_url_change(main_url)
        try:
            self.click_virt_mouse(self.button_personal_account)
        except:
            self.click_virt_mouse(self.button_personal_account)
        self.wait(self.button_history_orders)
        try:
            self.click_virt_mouse(self.button_history_orders)
        except:
            self.click_virt_mouse(self.button_history_orders)
        self.wait_url_change(history_orders_url)





    @allure.step("Проверка выхода из аккаунта")
    def check_button_sign_out(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        self.wait_url_change(main_url)
        try:
            self.click_virt_mouse(self.button_personal_account)
        except:
            self.click_virt_mouse(self.button_personal_account)
        self.click_virt_mouse(self.button_sign_out)
        try:
            self.click_virt_mouse(self.button_personal_account)
        except:
            self.click_virt_mouse(self.button_personal_account)
        self.wait_url_change(login_url)





