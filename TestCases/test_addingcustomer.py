import time
from selenium import webdriver
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
import string
import random
from Utilities.customelogger import LogGen
from Utilities.readproperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_001_addcustomer(self,setup):
        self.logger.info("********* TestAdd new customer *******")
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

        self.logger.info(" ***** Starting Adding Customer ****** ")
        self.email= random_generator() + "@gmail.com"
        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickonCustomerMenu()
        self.addcust.ClickonCustomerSubmenu()
        self.addcust.ClickaddNew()
        self.addcust.addemail(self.email)
        self.addcust.addFirstName("ANWAR")
        self.addcust.addLastName("SHAIKH")
        self.addcust.setgender("Male")
        self.addcust.addDob("08/03/1991")
        self.addcust.provideCompany("Nuance Communication India Pune")
        self.addcust.addadmincontent("This is Testing ")
        self.addcust.Savetheform()
        self.logger.info(" Customer all information added")

        self.msg= self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'Customer has been added sucessfully.' in self.msg:
            assert True==True
            self.logger.info("******* Add Customer Test Case Passed ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"AddCustomer.png")
            self.logger.error("****** Add Customer Test Case Failed ******* ")
            assert False== False

        self.driver.close()
        self.logger.info("***** Test has been Ended *****")

def random_generator(size=8,Chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(Chars) for x in range(size))



