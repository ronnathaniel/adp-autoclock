
from sys import argv
from time import sleep
from conftest import *

USERNAME = argv[1]
PASSWORD = argv[2]
OPERATION = int(argv[3])
ADP_URL = 'https://workforcenow.adp.com/theme/index.html'
USERNAME_CSS = 'input[name="user"]'
PASSWORD_CSS = 'input[name="password"]'
SIGN_IN_CSS = 'button[class="btn btn-primary ng-scope"]'
CLOCK_IN_CSS = 'span[id="revit_form_ComboButton_0_label"]'
CLOCK_OUT_CSS = 'span[id="revit_form_ComboButton_1_label"]'

def login(browser       : webdriver,
          adp_url       : str,
          username_css  : str,
          username      : str,
          password_css  : str,
          password      : str,
          sign_in_css   : str):

    browser.get(adp_url)
    browser.find_element_by_css_selector(username_css).send_keys(username)
    browser.find_element_by_css_selector(password_css).send_keys(password)
    browser.find_element_by_css_selector(sign_in_css).click()

def auto_clock(browser          : webdriver,
               clock_in_css     : str,
               clock_out_css    : str,
               operation        : int):

    browser.find_element_by_css_selector(clock_in_css if not operation else clock_out_css).click()
    sleep(1)  # sorry for the sleep


@pytest.mark.usefixtures('chrome_driver')
class Clocker:

    def clock(self):
        login(browser=self.driver, adp_url=ADP_URL, username_css=USERNAME_CSS, username=USERNAME,
              password_css=PASSWORD_CSS, password=PASSWORD, sign_in_css=SIGN_IN_CSS)
        auto_clock(browser=self.driver, clock_in_css=CLOCK_IN_CSS, clock_out_css=CLOCK_OUT_CSS, operation=OPERATION)
