import time
import os
from utils import config
from playwright.sync_api import Page,expect, Playwright
from pages.loginPage import LoginPage
from pages.cipAppPage import CipAppPage


# def test_logintochromium(playwright: Playwright):
#   with playwright.chromium.launch(headless=False) as browser:
#         context = browser.new_context()
#         page = context.new_page()

        # loginPage(page)


def test_loginPage(page:Page):
    baseUrl = config.BASE_URL
    userName = config.USERNAME
    userPassword = config.PASSWORD

#Naviagte
    loginPage = LoginPage(page)
    loginPage.navigate(baseUrl)

#Filling creds
    loginPage.login(userName,userPassword)
    time.sleep(5)

#Open CIP app in home page
    cipAppPage = CipAppPage(page)
    cipAppPage.open_cip_app()
    time.sleep(5)
    
