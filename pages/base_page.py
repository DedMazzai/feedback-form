from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, app):
        self.app = app

    # проверка что элемент пристутсвет на странице
    def is_element_present(self, how, what):
        browser = self.app.browser
        try:
            browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def fill_input_field(self, how, what, content):
        browser = self.app.browser
        field = browser.find_element(how, what)
        field.clear()
        field.send_keys(content)

    def click_element(self, how, what):
        browser = self.app.browser
        element = browser.find_element(how, what)
        element.click()

    def is_not_element_present(self, how, what, timeout=4):
        browser = self.app.browser
        try:
            WebDriverWait(browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
