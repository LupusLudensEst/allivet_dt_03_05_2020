from behave import *

@then("Click on Create an account tab")
def click_on_create_new_acc_tab(context):
    """
    Click on Create an account tab
    """
    context.app.create_login.click_on_create_new_acc_tab()


@then("Input First Name {first_name}")
def inpt_frst_name(context, first_name):
    """
    Input First Name FirstName
    """
    context.app.create_login.inpt_frst_name(first_name)


@then("Input Last Name {last_name}")
def inpt_lsst_name(context, last_name):
    """
    Input Last Name LastName
    """
    context.app.create_login.inpt_lsst_name(last_name)


@then("Input Telephone {phn_nmbr}")
def inpt_phn_nmbr(context, phn_nmbr):
    """
    Input Telephone 4074354433
    """
    context.app.create_login.inpt_phn_nmbr(phn_nmbr)


@then("Input Mobile {phn_nmbr}")
def inpt_mbl_nmbr(context, phn_nmbr):
    """
    Input Mobile 4074354433
    """
    context.app.create_login.inpt_mbl_nmbr(phn_nmbr)


@then("Input Account Name {acnt_nm}")
def inpt_acnt_nm(context, acnt_nm):
    """
    Input Account Name LupusLudens
    """
    context.app.create_login.inpt_acnt_nm(acnt_nm)


@then("Input Email Address {e_mail}")
def inpt_e_mail(context, e_mail):
    """
    Input Email Address sanoy2006@mail.ru
    """
    context.app.create_login.inpt_e_mail(e_mail)


@then("Input Password {pswd}")
def inpt_pswd(context, pswd):
    """
    Input Password Password_Test
    """
    context.app.create_login.inpt_pswd(pswd)


@then("Confirm Password {pswd}")
def cnfrm_pswd(context, pswd):
    """
    Confirm Password Password_Test
    """
    context.app.create_login.cnfrm_pswd(pswd)


@then("Input Address {addrss}")
def inpt_addrss(context, addrss):
    """
    Input Address 6058 SW 18TH ST APT 4
    """
    context.app.create_login.inpt_addrss(addrss)


@then("Choose Country {country}")
def choose_cntr(context, country):
    """
    Choose Country United States of America
    """
    context.app.create_login.choose_cntr(country)


@then("Input Zipcode {zip}")
def inpt_zip(context, zip):
    """
    Input Zipcode 33023
    """
    context.app.create_login.inpt_zip(zip)


@then("Choose State/Sity {state_city}")
def choose_stt_cty(context, state_city):
    """
    Choose State/Sity Fl, Hollywood
    """
    context.app.create_login.choose_stt_cty(state_city)


@then("Click on Create Account button")
def clck_crt_accnt_btn(context):
    """
    Click on Create Account button
    """
    context.app.create_login.clck_crt_accnt_btn()


@then("Verify that text is here: {text}")
def vrf_text_is_hr(context, text):
    """
    Verify that text is here: Account and Contact Information
    """
    context.app.create_login.vrf_text_is_hr(text)