import time
import re
from utils import config

from playwright.sync_api import Page,Playwright,sync_playwright,expect
from pages.loginPage import LoginPage
from pages.userSearchPage import UserSearchPage
from pages.userFramePage import UserFramePage
from pages.appLauncherPage import AppLauncherPage
from pages.ixtFormPage import IXTFormPage
from pages.confirmationPage import ConfirmationPage
from pages.logoutEmployeeUserPage import LogoutEmployeeUserPage
from pages.businessUserLogin import BusinessUserLoginPage
from pages.recordDetailPage import RecordDetailPage
from pages.recordTypeValidationPage import RecordTypeValidationPage






def test_loginPage(page:Page):
    baseUrl = config.BASE_URL
    userName = config.USERNAME
    userPassword = config.PASSWORD

#Naviagte to salesforce qa org
    loginPage = LoginPage(page)
    loginPage.navigate(baseUrl)

#Filling creds
    loginPage.login(userName,userPassword)
    time.sleep(5)


# Search the test employee user
    userSearchPage = UserSearchPage(page)
    userSearchPage.emp_user_search(page)

 # Switch to iframe and click login button to login as test employee user
    userFramePage = UserFramePage(page)
    userFramePage.emp_login(page)

# Launch IXT Mailbox WebForm
    appLauncherPage = AppLauncherPage(page)
    appLauncherPage.open_ixt_webform(page)

 # Fill out the IXT webform
    ixtFormPage = IXTFormPage(page)
    ixtFormPage.fill_ixt_form(page)

# Extract ixt ID
    confirmationPage = ConfirmationPage(page)
    record_id = confirmationPage.get_ixt_id(page)

# Log out test employee user
    logoutEmployeeUserPage = LogoutEmployeeUserPage(page)
    logoutEmployeeUserPage.logout_user(page)  
    
#  Login as the test business user
    businessUserLoginPage = BusinessUserLoginPage(page)
    businessUserLoginPage.business_user_login(page)
    
# open newly created IXT record  
    recordDetailPage = RecordDetailPage(page)
    recordDetailPage.record_detail(record_id)
    
# validate record type = GVD – US Outbound Record
    recordTypeValidationPage = RecordTypeValidationPage(page)
    recordTypeValidationPage.record_type_validation(page)


    



