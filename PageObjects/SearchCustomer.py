
class SearchCust:
    SearchEmail_id = "SearchEmail"
    SearchName_id ="SearchFirstName"
    SearchLast_id = "SearchLastName"
    Search_id = "search-customers"

    CompleteTable_xpath= "//table[@id='customers-grid']"
    SearchTable_xpath=  "//table[@id='customers-grid']"
    RowofTable_xpath ="//table[@id='customers-grid']//tbody/tr"
    TableColumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"



    def __init__(self,driver):
        self.driver = driver

    def searbyemail(self,byemail):
        self.driver.find_element_by_id(self.SearchEmail_id).clear()
        self.driver.find_element_by_id(self.SearchEmail_id).send_keys(byemail)

    def searbyfirstname(self,fname):
        self.driver.find_element_by_id(self.SearchName_id).clear()
        self.driver.find_element_by_id(self.SearchName_id).send_keys(fname)

    def searbylastname(self,lname):
        self.driver.find_element_by_id(self.SearchLast_id).clear()
        self.driver.find_element_by_id(self.SearchLast_id).send_keys(lname)

    def Clicktosearch(self):
        self.driver.find_element_by_id(self.Search_id).click()

    def getNoOfRow(self):
        return len(self.driver.find_elements_by_xpath(self.RowofTable_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.TableColumn_xpath))

    def searchCustomerbyemail(self,email):
        flag =False
        for i in range(1,self.getNoOfRow()+1):
            table = self.driver.find_element_by_xpath(self.CompleteTable_xpath)
            emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(i)+"]/td[2]").text
            if emailid== email:
                flag=True
                break
        return flag

    def searchCustomerbyname(self,name):
        flag=False
        for i in range(1,self.getNoOfRow()+1):
            table = self.driver.find_element_by_xpath(self.CompleteTable_xpath)
            Name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(i)+"]/td[3]").text
            if Name== name:
                flag=True
                break
        return flag
