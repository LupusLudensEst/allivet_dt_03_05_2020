from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    # locators
    MY_ACCNT_BTN = (By.XPATH, "//button[@class='btn btn-account one']")
    SGN_IN_BTN = (By.XPATH, "//a[@href='/signin.aspx']")
    EMAIL_FLD = (By.NAME, "EMail")
    PSWD_FLD = (By.ID, "Password")
    LGN_BTN = (By.ID, "LoginButton")
    ALRT_TEXT = (By.ID, "ErrorPanel")

    def click_my_accnt_btn(self):
        """
        Click MY ACCOUNT button
        """
        self.click(*self.MY_ACCNT_BTN)

    def click_sign_in_btn(self):
        """
        Click Sign In button
        """
        self.click(*self.SGN_IN_BTN)

    def input_email(self, text):
        """
        Input into e-mail field TestEmail@gmail.com
        """
        self.input_text(text, *self.EMAIL_FLD)

    def input_password(self, text):
        """
        Input into password field TestPassword
        """
        self.input_text(text, *self.PSWD_FLD)

    def click_lgn_btn(self):
        """
        Click login button
        """
        self.click(*self.LGN_BTN)

    def verify_alert_is_here(self, text):
         """
         Verify page has a text 'Invalid Login'
         """
         self.verify_text(text, *self.ALRT_TEXT)