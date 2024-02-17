from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import unittest

class HomePageLocators:
    LOG_IN_TAB = (By.ID, "login2")
    LOG_IN_MODAL = (By.CSS_SELECTOR, ".modal.fade.show .modal-content")
    USERNAME_FIELD = (By.ID, "loginusername")
    PASSWORD_FIELD = (By.ID, "loginpassword")
    LOG_IN_BUTTON = (By.XPATH, "//*[@class=\"btn btn-primary\"][contains(text(),\"Log in\")]")
    WELCOME_HEADER = (By.XPATH, "//*[contains(text(),\"Welcome JoannaJachowicz\")]")
    LAPTOPS_CATEGORY_TAB = (By.XPATH, "//*[contains(text(),\"Laptops\")]")
    LAPTOP_TYPE_MACBOOK = (By.XPATH, "//*[contains(text(),\"MacBook\")]")
    PHONE_TYPE_SAMSUNG = (By.XPATH, "//*[contains(text(),\"Samsung\")]")
    MONITOR_TYPE_ASUS = (By.XPATH, "//*[contains(text(),\"ASUS\")]")
    NEXT_PAGE_BUTTON = (By.ID, "next2")



class HomePage(BasePage):
    """
    Login page object
    """
    def select_login_tab(self):
        """
        Click on Log In Tab to get Login form
        :return: Login form
        """
        self.driver.find_element(*HomePageLocators.LOG_IN_TAB).click()
        return self.driver.find_element(*HomePageLocators.LOG_IN_MODAL)

    def add_login_data(self, user_name, password):
        """
        User put his username and password relates to this username
        :return:
        """
        self.driver.find_element(*HomePageLocators.USERNAME_FIELD).send_keys(user_name)
        self.driver.find_element(*HomePageLocators.PASSWORD_FIELD).send_keys(password)

    def click_on_login_button(self):
        """
        User click on log in button to log to the system
        :return:
        """
        self.driver.find_element(*HomePageLocators.LOG_IN_BUTTON).click()

    def verify_that_user_is_logged_to_the_system(self):
        """
        User verify that she/he is logged in
        :return:
        """
        welcome_header = self.driver.find_element(*HomePageLocators.WELCOME_HEADER)
        text_from_welcome_header = welcome_header.text
        assert text_from_welcome_header == "Welcome JoannaJachowicz"

    def verification_of_possibility_to_login_to_the_store_with_wrong_password(self):
        """
        Method verify that after putting wrong password to the password field, error message about wrong password is
        visible
        """
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert = Alert(self.driver)
        alert_text = alert.text
        expected_alert_text = "Wrong password."
        assert alert_text == expected_alert_text, f"Unexpected alert text: {alert_text}"

    def select_laptops_category(self):
        """
        Method selects laptops category from the categories menu
        """
        macbook_air_locator= (By.XPATH, "//*[contains(text(),\"MacBook air\")]")
        self.driver.find_element(*HomePageLocators.LAPTOPS_CATEGORY_TAB).click()
        wait = WebDriverWait(self.driver,2)
        macbook_air = wait.until(EC.visibility_of_element_located(macbook_air_locator))

    def verification_that_appropriate_object_are_displaying_in_laptop_category(self):
        """
        Method verifies that elements which should be visible in category laptops are visible there and that elements
        which should be not visible are not displaying in laptops category
        """
        macbooks = self.driver.find_elements(*HomePageLocators.LAPTOP_TYPE_MACBOOK)
        assert len(macbooks) > 0

        phones = self.driver.find_elements(*HomePageLocators.PHONE_TYPE_SAMSUNG)
        for phone in phones:
            assert not phone.is_displayed(), "Element is visible, but it shouldn't be"

        monitors = self.driver.find_elements(*HomePageLocators.MONITOR_TYPE_ASUS)
        for monitor in monitors:
            assert not monitor.is_displayed(), "Element is visible, but it shouldn't be"













