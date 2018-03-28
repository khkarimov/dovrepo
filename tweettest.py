from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('/Users/owner/PycharmProjects/test1/chromedriver')
driver.set_page_load_timeout(30)
driver.get("https://www.phptravels.net/login")
driver.maximize_window()
time.sleep(3)
action = action_chains.ActionChains(driver)
wait = WebDriverWait(driver,10)

username = driver.find_element_by_xpath('//*[@id="loginfrm"]/div[1]/div[5]/div/div[1]/input')
username.send_keys('user@phptravels.com')
password = driver.find_element_by_xpath('//*[@id="loginfrm"]/div[1]/div[5]/div/div[2]/input')
password.send_keys('demouser')
loginBtn = driver.find_element_by_xpath('//*[@id="loginfrm"]/div[1]/div[5]/button')
loginBtn.click()

time.sleep(3)

body = driver.find_element_by_xpath('//*[@id="body-section"]/div/div[1]/div/div[1]/h3')

if 'DVhbCERv' in body.text:
    print('Login successful')
else:
    print('Login unsuccessful')

# booking

hotelsBtn = driver.find_element_by_xpath('//*[@id="offcanvas-menu"]/ul/li[1]/a/span[1]/img')
hotelsBtn.click()
modifySearch = driver.find_element_by_xpath('//*[@id="body-section"]/div[1]/div/div/div[5]/div/a/i')
modifySearch.click()
time.sleep(3)
# starRating = driver.find_element_by_xpath('//*[@id="collapse1"]/div[1]/div/div[9]/div/ins')
# starRating.click()
# priceRange = driver.find_element_by_xpath('//*[@id="collapse2"]/div/div/div[1]/div[3]')
# priceRange.click()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

locationInput = driver.find_element_by_xpath('//*[@id="s2id_autogen1"]')
locationInput.click()
hotelName = driver.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
hotelName.send_keys('Islam')
time.sleep(2)
hotelName.send_keys(Keys.ENTER)
time.sleep(2)
searchBtn = driver.find_element_by_xpath('//*[@id="modify"]/div[1]/div/form/div[3]/div[3]/button')
searchBtn.click()
# time.sleep(3)
hotelDescription = driver.find_element_by_xpath('//*[@id="OVERVIEW"]/div[3]/div/div/div[2]/div/div[1]/p[2]')
# time.sleep(3)
if 'Islamabad Marriott' in hotelDescription.text:
    print ('Search successful')

else:
    print('Search unsuccessful')

driver.execute_script("window.scrollTo(0, 750)")
time.sleep(2)

bookNowBtn = driver.find_element_by_css_selector('tr:nth-child(1) > td > div.col-md-8.col-xs-7.g0-left > div:nth-child(6) > div.col-md-6 > button')
bookNowBtn.click()
time.sleep(2)
bookingConfirm = driver.find_element_by_xpath('//*[@id="body-section"]/div[2]/div[1]/div/div/div[4]/button')
bookingConfirm.click()
time.sleep(6)

try:
    invoicePg = driver.find_elements_by_id('downloadInvoice')

    print ('Booking successful')
except:
    print('Booking unsuccessful')
#
#
# # payment
payBtn = driver.find_element_by_xpath('//*[@id="body-section"]/div[1]/div[2]/div[2]/center/button[2]')
payBtn.click()
time.sleep(2)
payMethod = driver.find_element_by_xpath('//*[@id="gateway"]')
payMethod.click()
creditCardOption = driver.find_element_by_xpath('//*[@id="gateway"]/option[4]')
creditCardOption.click()
time.sleep(2)
nameInput = driver.find_element_by_xpath('//*[@id="card-holder-firstname"]')
nameInput.send_keys('John')
surnameInput = driver.find_element_by_xpath('//*[@id="card-holder-lastname"]')
surnameInput.send_keys('Smith')
cardNumber = driver.find_element_by_xpath('//*[@id="card-number"]')
cardNumber.send_keys('2345654345678765')
cardExpiration = driver.find_element_by_xpath('//*[@id="expiry-month"]')
cardExpiration.click()
expirationMonth = driver.find_element_by_xpath('//*[@id="expiry-month"]/option[6]')
expirationMonth.click()
expirationYear = driver.find_element_by_xpath('//*[@id="expiry-year"]')
expirationYear.click()
yearInput = driver.find_element_by_xpath('//*[@id="expiry-year"]/option[2]')
yearInput.click()
cVVInput = driver.find_element_by_xpath('//*[@id="cvv"]')
cVVInput.send_keys('234')
time.sleep(2)
payNowBtn = driver.find_element_by_xpath('//*[@id="pay"]/div/div[2]/div[1]/div[4]/form/fieldset/div[3]/button')
payNowBtn.click()
time.sleep(2)
try:
    postPaymentPage = driver.find_element_by_xpath('//*[@id="body-section"]/div[1]/div[2]/div[1]')
    print ('Payment successful')
except: print('Payment unsuccessful')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# for option in payMethod.find_elements_by_tag_name('credit_card'):
#     payMethod.click()

# # invoice = driver.find_element_by_xpath('//*[@id="body-section"]')
#
# # if 'Booking Code' in body.text:
# #     print('Booking Successful')
# #
# # else:
# #     print('Booking Unsuccessful')
#
# #
#
#
# #select2-drop > div > input
#
#
# # # try:
# #     assurance = driver.find_element_by_css_selector('div.col-md-1.offset-0 > ul > li:nth-child(2) > a > span')
# #     assurance.click()
# #     print('Login test Passed')
# # except:
# #     print('Login test failed')
# # login
# # driver.find_element_by_css_selector('div.StaticLoggedOutHomePage-getStartedBlock > div > p > a').click()
# # username = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
# # username.send_keys('ComcastUser3301')
# #
# # password = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
# # password.send_keys('Comcast@user17')
# # time.sleep(2)
# # submitBtn = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
# # submitBtn.click()
# #
# # time.sleep(3)
# #
# # try:
# #     tweetBtn = driver.find_element_by_id('global-new-tweet-button')
# #     print('Login Test Passed!')
# # except:
# #     print('Login Test Failed!')
#
#
#
#
#
# #
# # driver.implicitly_wait(4)
# #
# # items = driver.find_elements_by_xpath('//*[@id="stream-items-id"]/li')
# # print 'items list length:', len(items)
# # num = 1
# # listOfTweetStrings = []
# # listOfTweetIds = []
# #
# # for item in items:
# #     tweetString = item.get_attribute('id')
# #     tweetId = item.get_attribute('data-item-id')
# #     print num, 'Tweet Id', tweetId
# #     listOfTweetStrings.append(str(tweetString))
# #     listOfTweetIds.append(str(tweetId))
# #     num += 1
# #
# # eachTweet = 0
# #
# # for i in items:
# #     print 'first element id used to click on UI:', listOfTweetStrings[eachTweet]
# #     tweet = driver.find_element_by_id(listOfTweetStrings[eachTweet])
# #     tweet.click()
# #     elem = driver.find_element_by_class_name("TweetTextSize--jumbo")
# #     print elem.text
# #
# #     if '38.73MB' in elem.text:
# #         print eachTweet + 1, "PASS"
# #     else:
# #         print eachTweet + 1, "FAIL"
# #
# #     textBox = driver.find_element_by_css_selector('div.permalink-inner.permalink-tweet-container > div > div.content.clearfix > div > a > span.FullNameGroup > strong')
# #     textBox.click()
# #     eachTweet += 1
# #
# # time.sleep(5)
#
#
#
#
# # driver.find_element_by_xpath('//*[@id="timeline"]/div[2]/div').click()
# # driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]').send_keys('Wtf, man?')
# # time.sleep(3)
# # driver.find_element_by_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button/span[1]').click()
# # driver.find_element_by_xpath('//*[@id="stream-item-tweet-976565043390304256"]/div/div[2]/div[1]/div/div/button').click()
#
raw_input("enter anything to close browser: ")
# #
# # elem = driver.find_element_by_class_name("TweetTextSize--jumbo")
# #
# # ids = driver.find_element_by_class_name("permalink-tweet-container")
# # print ids.text
# # print elem.text
#
#
#
#
#
# # webElement = driver.find_elements_by_css_selector("div.stream ol#stream-items-id.stream-items.js-navigable-stream ")
# #
# # print(webElement)
# #
# # for row in webElement:
# #     print row
# #     cell = row.find_elements_by_css_selector("js-stream-item stream-item stream-item")
# #     print(cell.text)
# time.sleep(5)
driver.quit()


