from pages.main_page import MainPage
from pages.create_login import CreateLogin


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.create_login = CreateLogin(self.driver)


