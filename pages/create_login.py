from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class CreateLogin(Page):

    # locators
    CRT_NW_ACCNT_BTN = (By.ID, "SignUpLink")
    INPT_FRST_NAME = (By.NAME, "ProfileControl$txtFirstName")
    INPT_LRST_NAME = (By.NAME, "ProfileControl$txtLastName")
    INPT_PHN_NMBR = (By.NAME, "ProfileControl$txtContactNumber")
    INPT_MBL_NMBR = (By.NAME, "ProfileControl$txtMobile")
    INPT_ACNT_NM = (By.NAME, "ProfileControl$txtAccountName")
    INPT_EMAIL = (By.NAME, "ProfileControl$txtEmail")
    INPT_PSWD = (By.NAME, "ProfileControl$txtPassword")
    CNFRM_PSWD = (By.NAME, "ProfileControl$txtConfirmPassword")
    INPT_ADDRSS = (By.ID, "BillingAddressControl_txtStreet")
    CHOOSE_CNTR = (By.XPATH, "//option[@value='United States of America']") # (By.ID, "BillingAddressControl_drpCountry")
    INPT_ZIP = (By.ID , "BillingAddressControl_txtPostal")
    CHOOSE_STT_CTY = (By.ID, "billing-city-states")
    CLCK_CRT_ACCNT_BTN = (By.ID , "create-customer-account")
    TEXT_FIELD = (By.CSS_SELECTOR, "div.outer-inner-box") # (By.XPATH, "//div[@class='login-inner-pages']/h1")  # (By.XPATH, "//div[@class='order-info2']/h2")

    def click_on_create_new_acc_tab(self):
        """
        Click on Create an account tab
        """
        self.click(*self.CRT_NW_ACCNT_BTN)

    def inpt_frst_name(self, text):
        """
        Input First Name FirstName
        """
        self.input_text(text, *self.INPT_FRST_NAME)

    def inpt_lsst_name(self, text):
        """
        Input Last Name LastName
        """
        self.input_text(text, *self.INPT_LRST_NAME)

    def inpt_phn_nmbr(self, text):
        """
        Input Telephone 4074354433
        """
        self.input_text(text, *self.INPT_PHN_NMBR)

    def inpt_mbl_nmbr(self, text):
        """
        Input Telephone 4074354433
        """
        self.input_text(text, *self.INPT_MBL_NMBR)

    def inpt_acnt_nm(self, text):
        """
        Input Account Name LupusLudens
        """
        self.input_text(text, *self.INPT_ACNT_NM)

    def inpt_e_mail(self, text):
        """
        Input Email Address sanoy2006@mail.ru
        """
        self.input_text(text, *self.INPT_EMAIL)

    def inpt_pswd(self, text):
        """
        Input Password Password_Test
        """
        self.input_text(text, *self.INPT_PSWD)

    def cnfrm_pswd(self, text):
        """
        Confirm Password Password_Test
        """
        self.input_text(text, *self.CNFRM_PSWD)

    def inpt_addrss(self, text):
        """
        Input Address 6058 SW 18TH ST APT 4
        """
        self.input_text(text, *self.INPT_ADDRSS)

    def choose_cntr(self, text):
        """
        Choose Country United States of America
        """
        self.choose_text(text, *self.CHOOSE_CNTR)

    def inpt_zip(self, text):
        """
        Input Zipcode 33023
        """
        self.input_text(text, *self.INPT_ZIP)

    def choose_stt_cty(self, text):
        """
        Choose State/Sity Fl, Hollywood
        """
        self.choose_text(text, *self.CHOOSE_STT_CTY)

    def clck_crt_accnt_btn(self):
        """
        Click on Create Account button
        """
        self.click(*self.CLCK_CRT_ACCNT_BTN)
        sleep(8)

    def vrf_text_is_hr(self, text):
         """
         Verify that text is here: Account and Contact Information
         """
         self.verify_text(text, *self.TEXT_FIELD)





