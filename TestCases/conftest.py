from selenium import webdriver
import pytest
from Utilities.readproperties import metadata

@pytest.fixture()
def setup():
    path = "C:/Users/Anwar/PycharmProjects/NOPCommerceApp/path/chromedriver.exe"
    driver= webdriver.Chrome(path)
    return driver

#_________pytest HTML Reports_________
# it is hook for adding Enviornment info to HTML

def pytest_configure():
  metadata.projectName()
  metadata.module()
  metadata.tester()

#it is hook for delete/Modify Enviornment infor in HTML Report
@pytest.mark.Optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
