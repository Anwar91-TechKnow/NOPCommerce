import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.customelogger import LogGen
from PageObjects.AddCustomerPage import AddCustomer

class Test_001_Login:
    #Hardcoded data
    '''baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
'''
    #commond information by using readconfig (Dynamic)
    baseURL = ReadConfig.getApplicationURL()
    username =ReadConfig.getUseremail()
    password =ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("********* test_homePageTitle *******")
        self.logger.info("********* Verifying Home page Title *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********* Home Page Title Test Case is Passed *******")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("********* Home Page Title Test Case is Failed *******")
            assert False
    @pytest.mark.skip
    def test_Login(self,setup):
        self.logger.info("********* test_Login *******")
        self.logger.info("********* Verifying Login Test *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********* Login Test Case is Passed *******")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("********* Login Test case is Failed *******")
            assert False


#New TestCases
#Adding New customer
#Search Customer by email
#Search Customer by Name





