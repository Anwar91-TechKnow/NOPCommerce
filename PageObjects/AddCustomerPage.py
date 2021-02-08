import time
from selenium import webdriver

class AddCustomer():
    #Add Customer Page.
    customerMenu_xpath ="/html/body/div[3]/div[2]/div/ul/li[4]/a/span"
    customerSubmenu_xpath= "/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span"
    addnew_linktext ="Add new"
    Email_id ="Email"
    Password_id ="Password"
    Firstname_id = "FirstName"
    Lastname_id ="LastName"
    Male_id = "Gender_Male"
    Female_id = "Gender_Female"
    Dateofbirth_name = "DateOfBirth"
    Companyname_id = "Company"
    Istaxexempt_id = "IsTaxExempt"
    Customerroles_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div"
    adminstrator_role_xpath ="//li[text()='Administrators']"
    Managerofvendor_xpath = "//*[@id='VendorId']"
    AdminConent_xpath = "//textarea[@name='AdminComment']"
    Save_name ="save"


    def __init__(self,driver):
        self.driver=driver

    def ClickonCustomerMenu(self):
        self.driver.find_element_by_xpath(self.customerMenu_xpath).click()

    def ClickonCustomerSubmenu(self):
        self.driver.find_element_by_xpath(self.customerSubmenu_xpath).click()

    def ClickaddNew(self):
        self.driver.find_element_by_link_text(self.addnew_linktext).click()

    def addemail(self,email):
        self.driver.find_element_by_id(self.Email_id).send_keys(email)

    def addPassword(self,password):
        self.driver.find_element_by_id(self.Password_id).send_keys(password)

    def addFirstName(self,firstname):
        self.driver.find_element_by_id(self.Firstname_id).send_keys(firstname)

    def addLastName(self,lastname):
        self.driver.find_element_by_id(self.Lastname_id).send_keys(lastname)

    def addDob(self,dob):
        self.driver.find_element_by_name(self.Dateofbirth_name).send_keys(dob)

    def addCompany(self, company):
        self.driver.find_element_by_id(self.Companyname_id).send_keys(company)

    def setgender(self, gender):
        if gender=='Male':
            self.driver.find_element_by_id(self.Male_id).click()
        elif gender=='Female':
            self.driver.find_element_by_id(self.Female_id).click()
        else:
            self.driver.find_element_by_id(self.Male_id).click()

    def provideCompany(self, company):
        self.driver.find_element_by_id(self.Companyname_id).send_keys(company)

    def addadmincontent(self,content):
        self.driver.find_element_by_xpath(self.AdminConent_xpath).send_keys(content)

    def Savetheform(self):
        self.driver.find_element_by_name(self.Save_name).click()