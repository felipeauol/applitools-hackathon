import pytest
from selenium import webdriver
from ..pages.login import  Login

@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome()
    url = getattr(request.cls, 'url', '')
    if not '/hackathon.html' in url:
      # Perform log in process
      Login(driver)
    yield driver
    driver.quit()