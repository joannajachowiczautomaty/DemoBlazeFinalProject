class BasePage:
    """
    Base class for each Page
    """
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        return