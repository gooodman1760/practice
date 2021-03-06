from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLabel


class InstagramPage(BasePage):
    instagram_header = WebLabel(By.XPATH, "//div[@class = 'nZSzR']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        return self.instagram_header.get_element()
