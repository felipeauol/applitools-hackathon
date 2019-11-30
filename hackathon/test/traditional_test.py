from ..pages.login import LoginPage, Login
from ..pages.dashboard import DashboardPage

class TestLoginPage():
  url = '/hackathon.html'

  def test_items_present(self, browser):
    login_page = LoginPage(browser, 'https://demo.applitools.com/hackathon.html')
    login_page.open()
    assert login_page.url_matches(), 'Page Failed to Load'

    assert 'Login Form' in login_page.form_header()
    assert 'Username' in login_page.username_label()
    assert 'Enter your username' in login_page.username_input()
    assert 'Password' in login_page.password_label()
    assert 'Enter your password' in login_page.password_input()

  def test_authorization_errors(self, browser):
    login_page = LoginPage(browser, 'https://demo.applitools.com/hackathon.html')
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
    dashboard_page = DashboardPage(browser, 'https://demo.applitools.com/hackathonApp.html')
    dashboard_page.sort_table_by_amount()

    assert dashboard_page.table_is_sorted()
