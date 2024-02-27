from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import unittest
from test_data import order_data

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
    PHONES_CATEGORY = (By.XPATH, "//*[contains(text(),\"Phones\")]")
    MONITORS_CATEGORY = (By.XPATH, "//*[contains(text(),\"Monitors\")]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[contains(text(),\"Add to cart\")]")
    HOME_PAGE_TAB = (By.XPATH, "//*[contains(text(),\"Home\")]")
    CART_TAB = (By.XPATH, "//*[contains(text(),\"Cart\")]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//*[contains(text(),\"Place Order\")]")
    PLACE_ORDER_MODAL = (By.CSS_SELECTOR, ".modal-body")
    NAME_ORDER_FIELD = (By.ID, "name")
    CREDIT_CARD_ORDER_FIELD = (By.ID, "card")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "[onclick=\"purchaseOrder()\"]")
    SUCCESSFUL_ORDER_MODAL = (By.XPATH, "//*[contains(text(),\"Thank you for your purchase!\")]")



class HomePage(BasePage):
    """
    Login page object
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.order_data = order_data.OrderData()

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

    def select_phones_category(self):
        """
        Method selects phones category from the categories menu
        """
        self.driver.find_element(*HomePageLocators.PHONES_CATEGORY).click()
        wait = WebDriverWait(self.driver,2)

    def select_monitors_category(self):
        """
        Method selects phones category from the categories menu
        """
        self.driver.find_element(*HomePageLocators.MONITORS_CATEGORY).click()
        wait = WebDriverWait(self.driver,2)


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

    def add_selected_product_to_the_cart(self, product):
        """
        Method added selected product to the cart, accept process and back to the homepage
        """
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, f"//a[contains(text(), '{product}')]").click()
        self.driver.find_element(*HomePageLocators.ADD_TO_CART_BUTTON).click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert = Alert(self.driver)
        alert.accept()
        self.driver.find_element(*HomePageLocators.HOME_PAGE_TAB).click()

    def select_cart_tab_and_verify_product_in_cart(self,expected_products):
        """
        Method verify that products added to cart are the same as expected
        """
        self.driver.find_element(*HomePageLocators.CART_TAB).click()
        actual_products = []
        products_elements = self.driver.find_elements(By.XPATH, "//tbody//tr//td[2]")
        for product_element in products_elements:
            actual_products.append(product_element.text)
        for expected_product in expected_products:
            if expected_product not in actual_products:
                return False

        return True

    def create_order(self):
        """
        Verify that is possible to create order for selected product
        """
        self.driver.find_element(*HomePageLocators.CART_TAB).click()
        self.driver.find_element(*HomePageLocators.PLACE_ORDER_BUTTON).click()
        self.driver.find_element(*HomePageLocators.PLACE_ORDER_MODAL)
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(*HomePageLocators.NAME_ORDER_FIELD).send_keys(self.order_data.fake_name)
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(*HomePageLocators.CREDIT_CARD_ORDER_FIELD).send_keys(self.order_data.fake_credit_card_number)
        self.driver.find_element(*HomePageLocators.PURCHASE_BUTTON).click()
        self.driver.find_element(*HomePageLocators.SUCCESSFUL_ORDER_MODAL)























