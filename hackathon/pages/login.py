from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .base import BasePage

class LoginPage(BasePage):
  LOGO_ICON = (By.CLASS_NAME, 'logo-w')
  HEADER = (By.CLASS_NAME, 'auth-header')
  WARNING = (By.CSS_SELECTOR, '.alert-warning')
  USER_ICON = (By.CLASS_NAME, 'os-icon-user-male-circle')
  USER_INPUT = (By.CSS_SELECTOR, 'form input#username')
  PASS_ICON =(By.CLASS_NAME, 'os-icon-fingerprint')
  PASS_INPUT = (By.CSS_SELECTOR, 'form input#password')
  FORM_LABELS = (By.CSS_SELECTOR, 'div.form-group label')
  REMEMBER_ME = (By.CSS_SELECTOR, 'label.form-check-label')
  SUBMIT_BUTTON = (By.ID, 'log-in')


  def username_label(self):
    return self.driver.find_elements(*self.FORM_LABELS)[0].text

  def password_label(self):
    return self.driver.find_elements(*self.FORM_LABELS)[1].text

  def form_header(self):
    try:
      elem = self.driver.find_element(*self.HEADER)
    except:
      raise Exception("Form header not located")
    return elem.text

  def username_input(self):
    try:
      elem = self.driver.find_element(*self.USER_INPUT)
    except:
      raise Exception("Username input field not located")
    return elem.get_attribute('placeholder')

  def password_input(self):
    try:
      elem = self.driver.find_element(*self.PASS_INPUT)
    except:
      raise Exception("Password input field not located")
    return elem.get_attribute('placeholder')

  def set_username(self, value):
    self.driver.find_element(*self.USER_INPUT).send_keys(value)

  def set_password(self, value):
    self.driver.find_element(*self.PASS_INPUT).send_keys(value)

  def submit(self):
    self.driver.find_element(*self.SUBMIT_BUTTON).click()

  def warning_text_matches(self, match):
    return self.driver.find_element(*self.WARNING).text == match

