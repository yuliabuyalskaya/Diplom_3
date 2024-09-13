from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from constants import main_url, lenta_url
import time




class LentaPage(BasePage):
    buttons_orders = [By.CLASS_NAME, 'text_type_digits-default']
    button_costructor = [By.XPATH, '/html/body/div/div/header/nav/ul/li[1]/a/p']
    modal_order = [By.CLASS_NAME, 'Modal_orderBox__1xWdi']
    text_number_order = [By.XPATH, '/html/body/div/div/section[2]/div[1]/div/p[1]']
    button_lenta = [By.XPATH, '/html/body/div/div/header/nav/ul/li[2]/a/p']
    button_image_ingredient = [By.CLASS_NAME, 'BurgerIngredient_ingredient__image__3e-07']
    modal_ingredient = [By.CLASS_NAME, 'Modal_modal__contentBox__sCy8X']
    button_modal_close = [By.CLASS_NAME, 'Modal_modal__close__TnseK']
    constructor_element = [By.CLASS_NAME, 'constructor-element__row']
    number_order = [By.XPATH, '/html/body/div/div/section/div[1]/div/h2']
    first_oder_in_lenta = [By.XPATH, '/html/body/div/div/main/div/div/ul/li[1]/a/div[1]/p[1]']
    button_personal_account = [By.XPATH, "/html/body/div/div/header/nav/a/p"]
    input_email = [By.NAME, 'name']
    input_password = [By.NAME, 'Пароль']
    button_sign_in = [By.XPATH, '/html/body/div/div/main/div/form/button']
    button_order = [By.XPATH, '/html/body/div/div/main/section[2]/div/button']
    number_all_orders = [By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/p[2]']
    number_orders_today = [By.XPATH, '/html/body/div/div/main/div/div/div/div[3]/p[2]']
    number_oder_in_work = [By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/ul[2]/li']

    @allure.step("Проверка модального окна заказа")
    def check_click_order_modal(self):
        self.click_virt_mouse(self.buttons_orders)
        return self.return_text(self.text_number_order)

    @allure.step("Проверка наличия заказа в ленте заказов")
    def check_orders_from_history_in_lenta(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        self.drag_and_drop(self.button_image_ingredient,self.constructor_element)
        self.click_virt_mouse(self.button_order)
        text = self.return_text(self.number_order)
        self.click_virt_mouse(self.button_modal_close)
        self.click_virt_mouse(self.button_lenta)
        result = self.return_text(self.first_oder_in_lenta)
        if text == result:
            return true
        else:
            return false




    @allure.step("Проверка увеличения каунтера всех заказов")
    def check_counter_all_oders(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        self.click_virt_mouse(self.button_lenta)
        number = self.return_text(self.number_all_orders)
        self.click_virt_mouse(self.button_costructor)
        self.drag_and_drop(self.button_image_ingredient, self.constructor_element)
        self.click_virt_mouse(self.button_order)
        self.click_virt_mouse(self.button_modal_close)
        self.click_virt_mouse(self.button_lenta)
        number_with_my_order = self.return_text(self.number_all_orders)
        if int(number) < int(number_with_my_order):
            return true
        else:
            return false

    @allure.step("Проверка увеличения каунтера заказов за сегодня")
    def check_orders_today(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        self.click_virt_mouse(self.button_lenta)
        number = self.return_text(self.number_orders_today)
        self.click_virt_mouse(self.button_costructor)
        self.drag_and_drop(self.button_image_ingredient, self.constructor_element)
        self.click_virt_mouse(self.button_order)
        self.click_virt_mouse(self.button_modal_close)
        self.click_virt_mouse(self.button_lenta)
        number_with_my_order = self.return_text(self.number_orders_today)
        if int(number) < int(number_with_my_order):
            return true
        else:
            return false





    @allure.step("Проверка заказа в работе")
    def check_omy_order_in_work(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        self.drag_and_drop(self.button_image_ingredient, self.constructor_element)
        self.click_virt_mouse(self.button_order)
        text = self.return_text(self.number_order)
        self.click_virt_mouse(self.button_modal_close)
        self.click_virt_mouse(self.button_lenta)
        result = self.return_text(self.number_oder_in_work)
        if text == result:
            return true
        else:
            return false










