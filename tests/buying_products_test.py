from tests.base_test import BaseTest
from pages import home_page
from test_data.order_data import OrderData


class BuyingProductsTest(BaseTest):

    def setUp(self):
        super().setUp()

    def test_buying_products_positive(self):
        """
        This test verify possibility of adding 2 products from different categories to the cart and
        ordering them
        """
        # Steps:
        #1. Select phones category
        self.home_page.select_phones_category()
        #2. Add selected product from phones category to the cart
        self.home_page.add_selected_product_to_the_cart("Nexus 6")
        #3. Select monitors category
        self.home_page.select_monitors_category()
        #4. Add selected product from monitors category to the cart
        self.home_page.add_selected_product_to_the_cart("ASUS Full HD")
        #5. Verify that correct products are added to the cart
        self.home_page.select_cart_tab_and_verify_product_in_cart(["ASUS Full HD", "Nexus 6"])
        #6 Create order
        self.home_page.create_order()
    def test_buying_products_without_adding_card_number(self):
        """
        This test verify possibility of order products without add card number
        """
        # Steps:
        #1. Select phones category
        self.home_page.select_phones_category()
        #2. Add selected product from phones category to the cart
        self.home_page.add_selected_product_to_the_cart("Nexus 6")
        #3. Select monitors category
        self.home_page.select_monitors_category()
        #4. Add selected product from monitors category to the cart
        self.home_page.add_selected_product_to_the_cart("ASUS Full HD")
        #5. Verify that correct products are added to the cart
        self.home_page.select_cart_tab_and_verify_product_in_cart(["ASUS Full HD", "Nexus 6"])
        #6 Create order without adding card number
        self.home_page.create_order_without_card_number()
