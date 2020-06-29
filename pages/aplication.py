import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.feedback_page import FeedbackPage



class Application:
    # Инициализация драйвера
    def __init__(self, browser_name, base_url):
        if browser_name == "chrome":
            self.browser = webdriver.Chrome()
            self.browser.maximize_window()
            self.browser.implicitly_wait(5)

        elif browser_name == "firefox":
            self.browser = webdriver.Firefox()
            self.browser.maximize_window()
            self.browser.implicitly_wait(5)

        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")

        self.base_url = base_url
        self.base_page = BasePage(self)
        self.feedback_page = FeedbackPage(self)



    # Открытие страницы фомы обратной связи
    def open_base_page(self):
        browser = self.browser
        browser.get(self.base_url)


    # разрушение Фикстуры
    def destroy(self):
        self.browser.quit()
