from ..pages.login_page import LoginPage

class TestLoginPage:
  def test_items_present(self, browser):
    login_page = LoginPage(browser, 'https://demo.applitools.com/hackathon.html')
    login_page.open()
    assert login_page.url_matches(), 'Page Failed to Load'

    assert 'Login Form' in login_page.form_header()
    assert 'Username' in login_page.username_label()
    assert 'Enter your username' in login_page.username_input()
    assert 'Password' in login_page.password_label()
    assert 'Enter your password' in login_page.password_input()
