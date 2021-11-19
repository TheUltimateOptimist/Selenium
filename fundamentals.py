# import webdriver that allows you to interact with web programmatically
from selenium import webdriver

# import needed for typing things and pressing enter
from selenium.webdriver.common.keys import Keys

# location of the chrome webdriver
PATH = "/Users/jonathandueck/Desktop/chromedriver"

# instantiation of webdriver
driver = webdriver.Chrome(PATH)

# open any website:


def openAnyWebsite(url):
    driver.get(url)

# return title of current webpage:


def currentWebPageTitle():
    return driver.title

# close current tab:


def closeCurrentTab():
    driver.close()

# quit browser:


def quitBrowser():
    driver.quit()

#########
# for element identification counts id before name before class name
#########


def findElement(argument, wayOfFinding):
    if wayOfFinding == "id":
        return driver.find_element_by_id(argument)
    elif wayOfFinding == "name":
        return driver.find_element_by_name(argument)
    elif wayOfFinding == "class-name":
        return driver.find_element_by_class_name(argument)
    elif wayOfFinding == "x-path":
        return driver.find_element_by_xpath(argument)
    else:
        return "other ways of finding an element are possible"


def enterSomethingInSearchbar(element, text):
    # enter the text
    element.send_keys(text)

    # press enter
    element.send_keys(Keys.RETURN)


def getPageSourceCode():
    return driver.page_source
