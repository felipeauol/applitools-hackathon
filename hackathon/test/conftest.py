import os
import pytest
from selenium import webdriver
from ..pages.login import  Login
from applitools.selenium import Eyes, Target, BatchInfo
from dotenv import load_dotenv
load_dotenv()
batch_info = BatchInfo('Hackathon')

@pytest.fixture(scope="class")
def browser(request):
  driver = webdriver.Chrome()
  url = getattr(request.cls, 'url', '')
  if not '/hackathonV2.html' in url:
    # Perform log in process
    Login(driver)
  yield driver
  driver.quit()

@pytest.fixture(scope="module")
def eyes():
  eyes = Eyes()
  eyes.api_key = os.getenv("APPLITOOLS_API_KEY")
  eyes.batch = batch_info
  yield eyes
  eyes.abort()