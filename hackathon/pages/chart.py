from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .base import BasePage
from PIL import Image
import imagehash
import time

class ChartPage(BasePage):
  CANVAS = (By.ID, 'canvas')
  ADD_DATA= (By.ID, 'addDataset')
  IMG_PATH = './hackathon/images/'
  BASELINE_1 = './hackathon/images/chart_Baseline.png'
  DIFF_1 = './hackathon/images/chart_Diff.png'
  BASELINE_2= './hackathon/images/chart_2019_Baseline.png'
  DIFF_2 = './hackathon/images/chart_2019_Diff.png'

  def capture_canvas_image(self, file='chart_Baseline.png'):
    self.driver.find_element(*self.CANVAS).screenshot(file)

  def images_match(self, baseline, current):
    base_hash = imagehash.average_hash(Image.open(baseline))
    current_hash = imagehash.average_hash(Image.open(current))
    return base_hash == current_hash

  def add_data(self):
    self.driver.find_element(*self.ADD_DATA).click()
