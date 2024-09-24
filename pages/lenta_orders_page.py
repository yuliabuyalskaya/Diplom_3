import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LentaPage(BasePage):
    buttons_orders = [By.CLASS_NAME, 'text_type_digits-default']
    button_costructor = [By.CLASS_NAME, 'AppHeader_header__link__3D_hX']
    modal_order = [By.CLASS_NAME, 'Modal_orderBox__1xWdi']
    text_number_order = [By.CSS_SELECTOR, '.mb-10']
    button_lenta = [By.CSS_SELECTOR, 'li.undefined > a:nth-child(1)']
    button_image_ingredient = [By.CLASS_NAME, 'BurgerIngredient_ingredient__image__3e-07']
    modal_ingredient = [By.CLASS_NAME, 'Modal_modal__contentBox__sCy8X']
    button_modal_close = [By.CLASS_NAME, 'Modal_modal__close__TnseK']
    constructor_element = [By.CLASS_NAME, 'constructor-element__row']
    number_order = [By.CSS_SELECTOR, '.Modal_modal__title_shadow__3ikwq']
    first_oder_in_lenta = [By.CLASS_NAME, 'text_type_digits-default']
    button_personal_account = [By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX:nth-child(3)"]
    input_email = [By.NAME, 'name']
    input_password = [By.NAME, 'Пароль']
    button_sign_in = [By.CSS_SELECTOR, '.button_button__33qZ0']
    button_order = [By.XPATH, '/html/body/div/div/main/section[2]/div/button']
    number_all_orders = [By.CSS_SELECTOR, 'div.undefined:nth-child(2) > p:nth-child(2)']
    number_orders_today = [By.XPATH, '/html/body/div/div/main/div/div/div/div[3]/p[2]']
    number_oder_in_work = [By.CSS_SELECTOR, 'li.text_type_main-small']

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
        self.wait_visibility(self.button_image_ingredient)
        self.drag_and_drop(self.button_image_ingredient, self.constructor_element)
        self.click_virt_mouse(self.button_order)
        self.wait_visibility(self.number_order)
        text = self.return_text(self.number_order)
        self.click_virt_mouse(self.button_modal_close)
        try:
            self.click(self.button_lenta)
        except:
            self.click_virt_mouse(self.button_lenta)
        result = self.return_text(self.first_oder_in_lenta)
        if text == result:
            return True
        else:
            return False




    @allure.step("Проверка увеличения каунтера всех заказов")
    def check_counter_all_oders(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        try:
            self.click_virt_mouse(self.button_lenta)
        except TimeoutException:
            self.click_virt_mouse(self.button_lenta)
        self.wait_visibility(self.number_all_orders)
        number = self.return_text(self.number_all_orders)
        self.click(self.button_costructor)
        self.click_virt_mouse(self.button_costructor)
        self.wait(self.button_image_ingredient)
        self.drag_and_drop(self.button_image_ingredient, self.constructor_element)
        self.click_virt_mouse(self.button_order)
        self.wait_visibility(self.button_modal_close)
        self.click(self.button_modal_close)
        self.click_virt_mouse(self.button_modal_close)
        self.wait_visibility(self.button_lenta)
        try:
            self.click_virt_mouse(self.button_lenta)
        except TimeoutException:
            self.click_virt_mouse(self.button_lenta)
        self.wait_visibility(self.number_all_orders)
        number_with_my_order = self.return_text(self.number_all_orders)
        if int(number) < int(number_with_my_order):
            return True
        else:
            return False




    @allure.step("Проверка увеличения каунтера заказов за сегодня")
    def check_orders_today(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        try:
            self.click_virt_mouse(self.button_lenta)
        except TimeoutException:
            self.click_virt_mouse(self.button_lenta)
        self.click_virt_mouse(self.button_lenta)
        self.wait_visibility(self.number_orders_today)
        number = self.return_text(self.number_orders_today)
        try:
            self.click_virt_mouse(self.button_costructor)
        except TimeoutException:
            self.click_virt_mouse(self.button_costructor)
        self.wait(self.button_image_ingredient)
        self.drag_and_drop(self.button_image_ingredient, self.constructor_element)
        self.click_virt_mouse(self.button_order)
        self.wait_visibility(self.button_modal_close)
        try:
            self.click_virt_mouse(self.button_modal_close)
        except TimeoutException:
            self.click_virt_mouse(self.button_modal_close)
        self.wait_visibility(self.button_lenta)
        try:
            self.click_virt_mouse(self.button_lenta)
        except TimeoutException:
            self.click_virt_mouse(self.button_lenta)
        self.wait_visibility(self.number_orders_today)
        number_with_my_order = self.return_text(self.number_orders_today)
        if int(number) < int(number_with_my_order):
            return True
        else:
            return False




    @allure.step("Проверка заказа в работе")
    def check_omy_order_in_work(self):
        self.click_virt_mouse(self.button_personal_account)
        self.wait(self.input_email)
        self.click(self.input_email)
        self.fill_input(self.input_email, 'nikitakuleshov1991@yandex.ru')
        self.click(self.input_password)
        self.fill_input(self.input_password, '01200120')
        self.click_virt_mouse(self.button_sign_in)
        self.wait(self.button_image_ingredient)
        self.drag_and_drop(self.button_image_ingredient, self.constructor_element)
        self.click_virt_mouse(self.button_order)
        self.wait_visibility(self.number_order)
        text = self.return_text(self.number_order)
        self.wait_visibility(self.button_modal_close)
        try:
            self.click_virt_mouse(self.button_modal_close)
        except:
            self.click_virt_mouse(self.button_modal_close)
        self.wait_visibility(self.button_lenta)
        try:
            self.click(self.button_lenta)
        except:
            self.click_virt_mouse(self.button_lenta)
        self.wait_visibility(self.number_oder_in_work)
        result = self.return_text(self.number_oder_in_work)
        if text == result:
            return True
        else:
            return False










