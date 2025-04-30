import os,pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_AccountReg:

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("*** test_001_AccountRegistration Started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*** Launching Application ***")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.regpage = AccountRegistrationPage(self.driver)
        self.logger.info("*** Clicking My Account --> Register ***")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("*** Providing Customer details for Registration ***")
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")

        self.email = randomString.random_string_generator()+"@gmail.com"
        self.regpage.setEmail(self.email)
        # self.regpage.setEmail('test654321@gmail.com')
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("*** Account Registration is Passed ***")
            assert True
        else:
            # self.driver.save_screenshot(r"C:\Users\KapuluruMadhanMohanR\PycharmProjects\SeleniumHybridFramework\screenshots\test_account_reg.png")
            self.driver.save_screenshot(os.path.abspath(os.getcwd())+"\\screenshots\\"+"test_account_reg.png")
            self.logger.error("*** Account Registration is Failed ***")
            assert False
        self.logger.info("*** test_001_AccountRegistration Finished ***")

