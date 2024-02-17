from tests.base_test import BaseTest
from test_data.login_data import LoginData

class TestLogin(BaseTest):
    """
    Login tests
    """

    def setUp(self):
        super().setUp()
        self.test_data = LoginData()

    def test_login(self):
        """
        TC1: Test of login to the demoblaze Product Store (happy path)
        pre-conditions - User has account in store
        """
        #Steps
        #1. Select login Tab to open Login Modal
        self.home_page.select_login_tab()
        #2. User puts his login data to the appropriate fields in login form
        self.home_page.add_login_data(self.test_data.user_name,
                                      self.test_data.password)
        #3. User click on log in button to log in to the system
        self.home_page.click_on_login_button()
        #. User verify that is logged in
        self.home_page.verify_that_user_is_logged_to_the_system()

    def test_login_wrong_password(self):
        """
        TC2: Test which verify possibility logging in to the demoblaze Product Store
        with password which is not related to the dedicated Username(which is registered in the system).
        """
        #Steps
        #1. Select login Tab to open Login Modal
        self.home_page.select_login_tab()
        #2. User puts his username to the username field in login form and generate random password which
        #is not relates to dedicated username
        self.home_page.add_login_data(self.test_data.user_name,
                                      self.test_data.fake_password)
        #3. User click on log in button to log in to the system
        self.home_page.click_on_login_button()
        #4. Step verify that appropriate error message appeared when user put a wrong data to the password field
        self.home_page.verification_of_possibility_to_login_to_the_store_with_wrong_password()


