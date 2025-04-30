from selenium.webdriver.common.by import By
class HomePage():
   #Locators
   lnk_myaccount_xpath = "//span[text()='My Account']"
   lnk_register_linktext = "Register"
   lnk_login_linktext = "Login"

   #constrcutor
   def __init__(self, driver):
       self.driver = driver

    #Action Methods
   def clickMyAccount(self):
       self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()
   def clickRegister(self):
       self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()
   def clickLogin(self):
       self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
