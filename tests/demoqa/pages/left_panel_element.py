from selene import browser
from selenium.webdriver.common.by import By

from tests.demoqa.pages.simple_page import SimplePage


class LeftPanelElement:
    def __init__(self):
        self.element = browser.element(".left-pannel")
        self.elements_block = browser.element(
            (By.XPATH, "(//*[@class='group-header'])[1]")
        )
        self.text_box_in_submenu = browser.element("#item-0")

    def open(self):
        browser.open(browser.config.base_url)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        self.open_page_elements_text_box()

    def open_page_elements_text_box(self):
        self.element.click()
        self.elements_block.click()
        self.text_box_in_submenu.click()
        return SimplePage
