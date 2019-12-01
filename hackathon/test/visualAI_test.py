from ..pages.login import LoginPage, Login
from ..pages.dashboard import DashboardPage
from ..pages.chart import ChartPage
from ..pages.ads import AdsPage
from applitools.selenium import Target

viewport_size_A = {'width': 1700, 'height': 880}
viewport_size_B  = {'width': 500,  'height': 800}

class TestLoginPage():
  url = '/hackathonV2.html'

  def test_login_page(self, browser, eyes):
    eyes.open(driver=browser, app_name='Hackathon', test_name='LoginUI',
      viewport_size = viewport_size_B)

    login_page = LoginPage(browser, 'https://demo.applitools.com/hackathonV2.html')
    login_page.open()

    eyes.check("LoginUI", Target.window())
    eyes.close(False)

    eyes.open(driver=browser, app_name='Hackathon', test_name='LoginData_1',
      viewport_size = viewport_size_B)

    login_page.open()
    login_page.submit()

    eyes.check("LoginData_1", Target.window())
    eyes.close(False)

    eyes.open(driver=browser, app_name='Hackathon', test_name='LoginData_2',
      viewport_size = viewport_size_B)

    login_page.open()
    login_page.set_username('admin')
    login_page.submit()
    eyes.check("LoginData_2", Target.window())
    eyes.close(False)

    eyes.open(driver=browser, app_name='Hackathon', test_name='LoginData_3',
      viewport_size = viewport_size_B)

    login_page.open()
    login_page.set_password('admin')
    login_page.submit()

    eyes.check("LoginData_3", Target.window())
    eyes.close(False)

    eyes.open(driver=browser, app_name='Hackathon', test_name='LoginData_4',
      viewport_size = viewport_size_B)

    login_page.open()
    login_page.set_username('admin')
    login_page.set_password('123')
    login_page.submit()

    eyes.check("LoginData_4", Target.window())
    eyes.close(False)

class TestTableSort():
  url = '/hackathonAppV2.html'

  def test_table_sorting(self, browser, eyes):
    eyes.open(driver=browser, app_name='Hackathon', test_name='TableSort',
      viewport_size = viewport_size_A)

    dashboard_page = DashboardPage(browser, 'https://demo.applitools.com/hackathonAppV2.html')
    dashboard_page.open()
    eyes.check("TableSort", Target.window())
    eyes.close(False)

class TestChartPage():
  url = '/hackathonChartV2.html'

  def test_current_year(self, browser, eyes):
    eyes.open(driver=browser, app_name='Hackathon', test_name='ChartCurrentYear',
      viewport_size = viewport_size_A)

    chart_page = ChartPage(browser, 'https://demo.applitools.com/hackathonChartV2.html')
    chart_page.open()

    eyes.check("ChartCurrentYear", Target.window())
    eyes.close(False)

    eyes.open(driver=browser, app_name='Hackathon', test_name='ChartNextYear',
      viewport_size = viewport_size_A)

    chart_page.open()
    chart_page.add_data()
    eyes.check("ChartCurrentYear", Target.window())
    eyes.close(False)


class TestAds():
  url = '/hackathonAppV2.html?showAd=true'

  def test_current_year(self, browser, eyes):
    eyes.open(driver=browser, app_name='Hackathon', test_name='TestAds',
      viewport_size = viewport_size_A)

    ads_page = AdsPage(browser, 'https://demo.applitools.com/hackathonAppV2.html?showAd=true')
    ads_page.open()

    eyes.check("TestAds", Target.window())
    eyes.close(False)
