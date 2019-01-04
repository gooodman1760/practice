from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from onliner_uat.web_elements.time_class_constants import TimeOutConstants
from onliner_uat.web_elements.web_helpers import WebHelpers


class WebBaseElement:
    def __init__(self, by, value):
        self.by = by
        self.value = value

    def __get__(self, obj, owner):
        self.driver = obj.driver
        return self

    def get_element(self, timeout=TimeOutConstants.PAGE_LOAD_TIMEOUT):
        """
        Get element from page
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((self.by, self.value)))
        except NoSuchElementException:
            return False
        return element

    def get(self, timeout=TimeOutConstants.PAGE_LOAD_TIMEOUT):
        return self.get_element(timeout)

    def is_present(self):
        """
        Check is element present
        """
        if self.driver.find_element(self.by, self.value):
            return True
        else:
            return False

    def is_not_present(self):
        """
        Check is element not present
        """
        if not(self.driver.find_element(self.by, self.value)):
            return True
        else:
            return False

    def get_text(self):
        """
        Get text from element
        """
        return self.driver.find_element(self.by, self.value).text

    def get_text_from_amount_of_elements(self):
        """
        Get text from amount of elements
        """
        l_of_text = []
        els = self.driver.find_elements(self.by, self.value)
        for i in range(len(els)):
            el = els[i].text.lower()
            l_of_text.append(el)
        return l_of_text

    def get_attribute(self, key):
        """
        Get attribute parameter
        """
        return self.driver.find_element(self.by, self.value).get_attribute(key)

    def with_text(self, text):
        self.value = self.value.format(text)
        return self