from ..pages.login import LoginPage, Login
from ..pages.dashboard import DashboardPage
from ..pages.chart import ChartPage
import time

class TestLoginPage():
  url = '/hackathon.html'

  def test_items_present(self, browser):
    login_page = LoginPage(browser, 'https://demo.applitools.com/hackathonV2.html')
    login_page.open()
    assert login_page.url_matches(), 'Page Failed to Load'

    assert 'Login Form' in login_page.form_header()
    assert 'Username' in login_page.username_label()
    assert 'Enter your username' in login_page.username_input()
    assert 'Password' in login_page.password_label()
    assert 'Enter your password' in login_page.password_input()

  def test_authorization_errors(self, browser):
    login_page = LoginPage(browser, 'https://demo.applitools.com/hackathonV2.html')
    login_page.open()
    login_page.submit()
    assert login_page.warning_text_matches('Both Username and Password must be present')
    
    login_page.open()
    login_page.set_username('admin')
    login_page.submit()
    assert login_page.warning_text_matches('Password must be present')

    login_page.open()
    login_page.set_password('admin')
    login_page.submit()
    assert login_page.warning_text_matches('Username must be present')
  
  def test_valid_login(self, browser):
    login_page = LoginPage(browser, 'https://demo.applitools.com/hackathon.html')
    login_page.open()

    login_page.set_username('admin')
    login_page.set_password('123')
    login_page.submit()
    assert 'hackathonApp.html' in browser.current_url
    assert 'Login Form' not in browser.page_source

class TestTableSort():
  url = '/hackathonApp.html'

  def test_table_sorting(self, browser):
    dashboard_page = DashboardPage(browser, 'https://demo.applitools.com/hackathonAppV2.html')
    dashboard_page.open()
    table_state_before = dashboard_page.table_state()

    dashboard_page.sort_table_by_amount()
    table_state_after = dashboard_page.table_state()

    assert dashboard_page.table_is_sorted()
    assert dashboard_page.table_is_intact(table_state_before, table_state_after)

class TestChartPage():
  url = '/hackathonChart.html'

  def test_current_year(self, browser):
    chart_page = ChartPage(browser, 'https://demo.applitools.com/hackathonChartV2.html')
    chart_page.open()
    # sleep here since Canvas animation is slow. 
    # TODO: Find alternative and remove.
    time.sleep(0.35)
    chart_page.capture_canvas_image(chart_page.DIFF_1)
    assert chart_page.images_match(chart_page.BASELINE_1, chart_page.DIFF_1)

  def test_next_year(self, browser):
    chart_page = ChartPage(browser, 'https://demo.applitools.com/hackathonChartV2.html')
    chart_page.open()
    chart_page.add_data()
    # sleep here since Canvas animation is slow. 
    # TODO: Find alternative and remove.
    time.sleep(0.35)
    chart_page.capture_canvas_image(chart_page.DIFF_2)
    assert chart_page.images_match(chart_page.BASELINE_2, chart_page.DIFF_2)