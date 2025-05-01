import pytest,os
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from  datetime import datetime
@pytest.fixture()
def setup(browser):
   if browser=='edge':
       options = webdriver.EdgeOptions()
       options.add_experimental_option("detach", True)
       driver = webdriver.Edge(options=options)
       print("Launching Edge browser.........")
   elif browser=='firefox':
       options = webdriver.FirefoxOptions()
       driver = webdriver.Firefox(options=options)
       print("Launching firefox browser.........")
   else:
       options = webdriver.ChromeOptions()
       options.add_experimental_option("detach", True)
       driver = webdriver.Chrome(options=options)
       print("Launching chrome browser.........")
   yield driver
   driver.quit()

def pytest_addoption(parser):    # This will get the value from CLI /hooks
   parser.addoption("--browser")
@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
   return request.config.getoption("--browser")

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
   config.stash[metadata_key]['Project Name'] = 'TutorialNinja'
   config.stash[metadata_key]['Module Name'] = 'CustRegistration'
   config.stash[metadata_key]['Tester Name'] = 'KMR'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
# @pytest.mark.optionalhook   # Deprecated
def pytest_metadata(metadata):
  metadata.pop("Python", None)
  metadata.pop("Plugins", None)

# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
   # config.option.htmlpath = (os.path.dirname(os.getcwd()) + "\\SeleniumHybridFramework\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html")
   config.option.htmlpath = (
               os.path.abspath(os.getcwd()) + "\\reports\\" + datetime.now().strftime(
           "%d-%m-%Y %H-%M-%S") + ".html")
