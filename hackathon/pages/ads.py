from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .base import BasePage
from PIL import Image
import imagehash
import time

class AdsPage(BasePage):
  AD_1 = (By.ID, 'flashSale')
  AD_2 = (By.ID, 'flashSale2')
  AD_3 = (By.CSS_SELECTOR, '.balance:last-of-type')
  BASE_AD_1 = './hackathon/images/AD1_Baseline.png'
  BASE_AD_2 = './hackathon/images/AD2_Baseline.png'
  BASE_AD_3 = './hackathon/images/AD3_Baseline.png'
  CURRENT_AD_1 = './hackathon/images/AD1_Diff.png'
  CURRENT_AD_2 = './hackathon/images/AD2_Diff.png'
  CURRENT_AD_3 = './hackathon/images/AD3_Diff.png'


  def ad_1_present(self):
    self.driver.find_element(*self.AD_1)

  def ad_2_present(self):
    self.driver.find_element(*self.AD_2)

  def ad_3_present(self):
    self.driver.find_element(*self.AD_3)

  def images_match(self, baseline, current):
    base_hash = imagehash.average_hash(Image.open(baseline))
    current_hash = imagehash.average_hash(Image.open(current))
    return base_hash == current_hash

  def capture_canvas_image(self, elem, file):
    self.driver.find_element(*elem).screenshot(file)