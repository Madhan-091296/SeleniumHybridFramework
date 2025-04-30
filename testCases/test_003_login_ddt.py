import time,pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.abspath(os.getcwd()) + "\\testData\\Tutorialninja_LoginData.xlsx"

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********* starting of test_003_login_ddt *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*** Launching Application ***")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = HomePage(self.driver)  #Home Page POC
        self.lp = LoginPage(self.driver)  #Login Page POC
        self.ma = MyAccountPage(self.driver) #MyAccount Page POC

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")

        lst_status = []

        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            self.targetpage = self.lp.isMyAccountPageExists()

            if self.exp == 'Valid':
                if self.targetpage == True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')

            if self.exp == 'Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')

        if 'Fail' not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("********* Ending of test_003_login_ddt *********")
















