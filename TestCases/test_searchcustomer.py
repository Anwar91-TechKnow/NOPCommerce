import time
from selenium import webdriver
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.SearchCustomer import SearchCust
from PageObjects.AddCustomerPage import AddCustomer
from Utilities.customelogger import LogGen
from Utilities.readproperties import ReadConfig

class Test_004_SearchCustmer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.skip
    def test_001_searchcustomer(self,setup):
        self.logger.info("********* Test Search Customer *******")
        self.logger.info("********* Verifying The Test Cases *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info(" ********* Login Successfull ********")

        self.logger.info(" ***** Starting Search Customer Test Case ****** ")
        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickonCustomerMenu()
        self.addcust.ClickonCustomerSubmenu()

        ser=SearchCust(self.driver)
        ser.searbyemail("victoria_victoria@nopCommerce.com")
        ser.Clicktosearch()
        time.sleep(5)
        status= ser.searchCustomerbyemail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("***** Test has been Ended *****")
        self.driver.close()

    def test_001_nmesearchcustomer(self,setup):
        self.logger.info("********* Test Search Customer *******")
        self.logger.info("********* Verifying The Test Cases *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info(" ********* Login Successfull ********")

        self.logger.info(" ***** Starting Search Customer Test Case ****** ")
        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickonCustomerMenu()
        self.addcust.ClickonCustomerSubmenu()

        ser = SearchCust(self.driver)
        ser.searbylastname("Terces")
        ser.searbyfirstname("victoria")
        ser.Clicktosearch()
        time.sleep(5)
        status = ser.searchCustomerbyname("Victoria Terces")
        assert True == status
        self.logger.info("***** Test has been Ended *****")
        self.driver.close()