import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(), options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(), options=options)

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()