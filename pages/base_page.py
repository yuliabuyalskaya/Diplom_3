#
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    #@allure.step("Клик по элементу {element}")
    def click(self, element):
        self.driver.find_element(*element).click()

    #@allure.step("Ожидание кликабельности {element}")
    def wait(self,element):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))


    #@allure.step("Заполнение элемента {element} текстом {text}")
    def fill_input(self, element, text):
        self.driver.find_element(*element).send_keys(text)

    #@allure.step("Ожидание смены урла на {url}")
    def wait_url_change(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    #@allure.step("Скролл до элемента {element}")
    def scroll(self, element):
        elemente = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", elemente)

    #@allure.step("Ожидание элемента {element}")
    def wait_visibility(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))

    #@allure.step("Получение текста элемента {element}")
    def return_text(self,element):
        answer_text = self.driver.find_element(*element).text
        return answer_text


    def wait_invisibility(self, element):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(element))




    def click_virt_mouse(self, element):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(element))
        element = self.driver.find_element(*element)
        action.click(on_element=element).perform()



    def drag_and_drop(self,element,element_drop):
        source_element = self.driver.find_element(*element)
        target_element = self.driver.find_element(*element_drop)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()







    
