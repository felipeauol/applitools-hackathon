from ..pages.login import LoginPage, Login
from ..pages.dashboard import DashboardPage
from ..pages.chart import ChartPage
from ..pages.ads import AdsPage
from applitools.selenium import Target

viewport_size_A = {'width': 1700, 'height': 880}
viewport_size_B  = {'width': 500,  'height': 800}

class TestLoginPage():
  url = '/hackathon.html'

  def test_login_page(self, browser, eyes):
    eyes.open(driver=browser, app_name='Hackathon', test_name='LoginUI',
      viewport_size = viewport_size_B)

    login_page = LoginPage(browser, 'https://demo.applitools.com/hackathon.html')
    login_page.open()

    eyes.check("LoginUI", Target.window())
    eyes.close()

    eyes.open(driver=browser, app_name='Hackathon', test_name='LoginData_1',
      viewport_size = viewport_size_B)

    login_page = LoginPage(browser, 'https://demo.applitools.com/hackathon.html')
    login_page.open()
    login_page.submit()

    eyes.check("LoginData_1", Target.window())
    eyes.close()

    eyes.open(driver=browser, app_name='Hackathon', test_name='LoginData_2',
      viewport_size = viewport_size_B)

    login_page.open()
    login_page.set_username('admin')
    login_page.submit()
    eyes.check("LoginData_2", Target.window())
    eyes.close()

    eyes.open(driver=browser, app_name='Hackathon', test_name='LoginData_3',
      viewport_size = viewport_size_B)

    login_page.open()
    login_page.set_password('admin')
    login_page.submit()

    eyes.check("LoginData_3", Target.window())
    eyes.close()

    eyes.open(driver=browser, app_name='Hackathon', test_name='LoginData_4',
      viewport_size = viewport_size_B)

    login_page.open()
    login_page.set_username('admin')
    login_page.set_password('123')
    login_page.submit()

    eyes.check("LoginData_4", Target.window())
    eyes.close()

class TestTableSort():
  url = '/hackathonApp.html'

  def test_table_sorting(self, browser, eyes):
    eyes.open(driver=browser, app_name='Hackathon', test_name='TableSort',
      viewport_size = viewport_size_A)

    dashboard_page = DashboardPage(browser, 'https://demo.applitools.com/hackathonApp.html')
    dashboard_page.open()
    eyes.check("TableSort", Target.window())
    eyes.close()

class TestChartPage():
  url = '/hackathonChart.html'

  def test_current_year(self, browser, eyes):
    eyes.open(driver=browser, app_name='Hackathon', test_name='ChartCurrentYear',
      viewport_size = viewport_size_A)

    chart_page = ChartPage(browser, 'https://demo.applitools.com/hackathonChart.html')
    chart_page.open()

    eyes.check("ChartCurrentYear", Target.window())
    eyes.close()

    eyes.open(driver=browser, app_name='Hackathon', test_name='ChartNextYear',
      viewport_size = viewport_size_A)

    chart_page.open()
    chart_page.add_data()
    eyes.check("ChartCurrentYear", Target.window())
    eyes.close()


class TestAds():
  url = '/hackathonApp.html?showAd=true'

  def test_current_year(self, browser, eyes):
    eyes.open(driver=browser, app_name='Hackathon', test_name='TestAds',
      viewport_size = viewport_size_A)

    ads_page = AdsPage(browser, 'https://demo.applitools.com/hackathonApp.html?showAd=true')
    ads_page.open()

    eyes.check("TestAds", Target.window())
    eyes.close()
