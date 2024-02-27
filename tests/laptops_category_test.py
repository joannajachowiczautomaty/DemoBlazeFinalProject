from tests.base_test import BaseTest
from pages import home_page


class TestLaptopsCategory(BaseTest):
    """
    Login tests
    """

    def setUp(self):
        super().setUp()

    def test_laptops_category(self):
        """
        TC3: Test verifies displaying category: Laptops
        """
        #Steps
        #1. Select Laptops category
        self.home_page.select_laptops_category()
        #2. Verify that correct category is displaying by finding object which we are sure that sure exist in the laptop
        #store and objects which should nov be visible there
        self.home_page.verification_that_appropriate_object_are_displaying_in_laptop_category()




