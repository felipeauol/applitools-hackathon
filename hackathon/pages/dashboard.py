from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .base import BasePage

class DashboardPage(BasePage):
  TABLE_HEADERS = (By.CSS_SELECTOR, '#transactionsTable thead tr')
  TABLE_ROWS = (By.CSS_SELECTOR, '#transactionsTable tbody tr')
  TABLE_DATA = (By.CSS_SELECTOR, '#transactionsTable tbody tr td')
  TRANSACTION_DATA = (By.TAG_NAME, 'td')
  AMOUNT_HEADER = (By.ID, 'amount')

  #TODO: Implement sorting method by any column
  def sort_table_by_amount(self):
    self.driver.find_element(*self.AMOUNT_HEADER).click()

  def table_is_sorted(self):
    transactions = self.driver.find_elements(*self.TABLE_ROWS)
    amounts = [self.amount_from_transaction(transaction) for transaction in transactions]
    sorted_amounts = amounts[:]
    return sorted_amounts == amounts

  @staticmethod 
  def amount_from_transaction(transaction):
    string = transaction.find_element_by_css_selector('td:last-of-type').text
    amount = float(string[2:-4].replace(',',''))
    return (amount * -1) if '-' in string else amount

  def table_state(self):
    transactions = self.driver.find_elements(*self.TABLE_ROWS)
    return [transaction.text for transaction in transactions]

  def table_is_intact(self, state_before, state_after):
    return all([original in state_after for original in state_before])