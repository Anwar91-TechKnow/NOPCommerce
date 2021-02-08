import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.customelogger import LogGen
from Utilities import ExcelUtils
import time

#this is Data Driven Testing


class Test_001_DDT_login:
      # variable creation
    url = ReadConfig.getApplicationURL()
    path = ".//TestData/TestData.xlsx"
    logger=LogGen.loggen()

    def test_login_DDT_001(self,setup):
        self.logger.info("********** test_login_DDT_001 Started ************")
        self.logger.info("********** DDT Test ******")
        self.driver = setup
        self.driver.get(self.url)
        self.lp= LoginPage(self.driver)

        self.rows= ExcelUtils.getRowCount(self.path,'Sheet1')
        print("number of rows in excel",self.rows)

        lst_status=[] #will use latar empty


        for r in range (2,self.rows+1):
            self.user = ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3 )

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title= self.driver.title
            exp_title= "Dashboard / nopCommerce administration"

            if act_title ==exp_title:
                if self.exp =="Pass":
                    self.logger.info("**** Test is Passed ****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("**** Test is Failed ****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title!= exp_title:
                if self.exp=="Pass":
                    self.logger.info("**** Test is Failed ****")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("**** Test is Passed ****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info(" **** Login DDT Passed ")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT Failed ")
            self.driver.close()
            assert False

        self.logger.info("---------End of Login DDT Test-------")
        self.logger.info("----------Completed TC_001/DDT-------")