from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from constants import main_url, lenta_url
import allure
import pytest




class MainPage(BasePage):
    button_costructor = [By.CSS_SELECTOR, '.AppHeader_header__link_active__1IkJo > p:nth-child(2)']
    button_lenta = [By.CSS_SELECTOR, 'li.undefined > a:nth-child(1) > p:nth-child(2)']
    button_logo = [By.CSS_SELECTOR, '.active > svg:nth-child(1)']
    button_image_ingredient = [By.CLASS_NAME, 'BurgerIngredient_ingredient__image__3e-07']
    modal_ingredient = [By.CLASS_NAME, 'Modal_modal__contentBox__sCy8X']
    modal_text = [By.CLASS_NAME, 'Modal_modal__title__2L34m']
    button_modal_close = [By.CLASS_NAME, 'Modal_modal__close__TnseK']
    constructor_element = [By.CLASS_NAME, 'constructor-element__row']
    counter = [By.CLASS_NAME, 'counter_counter__ZNLkj']
    button_personal_account = [By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX:nth-child(3) > p:nth-child(2)"]
    input_email = [By.NAME, 'name']
    input_password = [By.NAME, 'Пароль']
    button_sign_in = [By.CSS_SELECTOR, '.button_button__33qZ0']
    button_order = [By.XPATH, '/html/body/div/div/main/section[2]/div/button']
    order_text = [By.CSS_SELECTOR, 'p.undefined:nth-child(1)']




    @allure.step("Проверка кнопки конструктор")
    def check_button_constructor(self):
        self.click_virt_mouse(self.button_costructor)
        self.wait_url_change(main_url)




    @allure.step("Проверка кнопки ленты заказов")
    def check_button_lenta(self):
        self.click_virt_mouse(self.button_lenta)
        self.wait_url_change(lenta_url)




    @allure.step("Проверка модального окна ингредиента")
    def check_button_ingredient_modal(self):
        self.click_virt_mouse(self.button_image_ingredient)
        self.wait_visibility(self.modal_ingredient)
        return self.return_text(self.modal_text)




    @allure.step("Проверка закрытия модального окна по крестику")
    def check_modal_close(self):
        self.click_virt_mouse(self.button_image_ingredient)
        self.wait_visibility(self.modal_ingredient)
        self.click_virt_mouse(self.button_modal_close)
        self.wait_invisibility(self.modal_ingredient)
        return "Modal closed"



    @allure.step("Проверка каунтера ингредиентов")
    def check_drag_and_drop_ingredient_counter(self):
        self.drag_and_drop(self.constructor_element, self.button_image_ingredient)
        return self.return_text(self.counter)




    @allure.step("Проверка оформления заказа у авторизованного пользователя")
    def check_auth_user_order_confirm(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        self.click_virt_mouse(self.button_order)
        return self.return_text(self.order_text)
















