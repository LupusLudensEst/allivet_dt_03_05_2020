from behave import *

@given("Loginpage")
def open_homepage(context):
    context.app.main_page.open_page()

@then("Click MY ACCOUNT button")
def click_accnt_btn(context):
    context.app.main_page.click_my_accnt_btn()

@then("Click Sign In button")
def click_sgn_btn(context):
    context.app.main_page.click_sign_in_btn()

@then("Input into e-mail field {email}")
def input_email(context, email):
    context.app.main_page.input_email(email)

@then("Input into password field {password}")
def input_password(context, password):
    context.app.main_page.input_password(password)

@then("Click login button")
def click_lgn_btn(context):
    context.app.main_page.click_lgn_btn()

@then("Verify page has a text '{invld_lgn}'")
def text_is_here(context, invld_lgn):
    context.app.main_page.verify_alert_is_here(invld_lgn)
