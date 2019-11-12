
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def chrome_driver(request):
    options = Options()
    options.add_argument('disable-notifications')
    options.add_argument('--headless')
    web_driver = webdriver.Chrome(options=options)
    request.cls.driver = web_driver
    yield web_driver
    web_driver.close()
