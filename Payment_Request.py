import pandas as pd
import numpy as np
import time
import yaml
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

#-----------------------------------------------------------------------------#
# LOGS YOU INTO TWC WEBSITE AND BEGINS THE PAYMENT REQUEST PROCESS
driver = webdriver.Firefox(executable_path=r'D:\Users\Matt\Documents\GitHub\Executable_Files\geckodriver.exe')

conf = yaml.load(open(r'D:\Users\Matt\Documents\GitHub\YML_Files\Unemployment_Credentials.yml'))

my_username = conf['Unemployment']['username']
my_password = conf['Unemployment']['password']


def payment_request():
    # CHECKS IF ITS TOO EARLY TO FILE. IF IT IS, THE SCRIPT STOPS.
    driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/ul[1]/li[4]/a').click()
    if (driver.find_element_by_class_name('page-name').text) == 'Early Filing': driver.quit()

    # IF IT IS NOT TOO EARLY TO FILE, THE PAYMENT REQUEST CONTINUES.
    else:
        # PULLS CLAIM WEEK DATES FROM TWC WEBPAGE
        claim_week_pull = driver.find_element_by_class_name('page-header-row-value-1col').text[0:12]
        claim_week_convert_to_str = claim_week_pull.replace(',','')
        date_1 = datetime.datetime.strptime(claim_week_convert_to_str,r'%b %d %Y')

        #---------------------------------------------------------------------#
        # CREATES DATAFRAME FROM LOCAL EXCEL FILE AND READS TWO COLUMNS OF DATA.
        data = pd.read_excel(r'C:\Users\Matt\Dropbox\1 Job Search Related Items\Daily Work Log.xlsx', sheet_name='TWC Work Search Log')
        df = pd.DataFrame(data, columns= ['Date of Activity', 'Work Search Count'])

        # ADD UP WORK SEARCHES FOR WEEK 1
        end_date1 = date_1 + datetime.timedelta(days=6)
        between_two_dates1 = (df[(df['Date of Activity']>=date_1) & (df['Date of Activity']<=end_date1)])
        week1_work_searches = between_two_dates1.sum()

        # ADD UP WORK SEARCHES FOR WEEK 2
        date_2 = date_1 + datetime.timedelta(days=7)
        end_date2 = date_2 + datetime.timedelta(days=6)
        between_two_dates2 = (df[(df['Date of Activity']>=date_2) & (df['Date of Activity']<=end_date2)])
        week2_work_searches = between_two_dates2.sum()

        #---------------------------------------------------------------------#
        #CONTINUE PAYMENT REQUEST
        '''
        This series of button clicks goes through the website, fills in
        the radio buttons, and enters the work searches you've completed into
        the required fields when they come up.  After this process is complete,
        the script is stopped and the browser window closes.
        '''
        driver.find_element_by_id('addressChangeAnswer-radio.label.no').click()
        iframe = driver.find_element_by_xpath(
            "//iframe[@name='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']")
        driver.switch_to.frame(iframe)
        driver.find_elements_by_id('recaptcha-anchor').click()
        # driver.find_element_by_name('method:submit').click()
        time.sleep(5)
        driver.find_element_by_id('workOrEarnWagesWeek1-radio.label.no').click()
        driver.find_element_by_id('vacationOrHolidayPayWeek1-radio.label.no').click()
        driver.find_element_by_id('workOrEarnWagesWeek2-radio.label.no').click()
        driver.find_element_by_id('vacationOrHolidayPayWeek2-radio.label.no').click()
        driver.find_element_by_id('incomeNotAlreadyReported-radio.label.no').click()
        driver.find_element_by_name('method:submit').click()
        time.sleep(5)
        driver.find_element_by_id('ableToWork-radio.label.yes').click()
        driver.find_element_by_id('availableToAcceptWork-radio.label.yes').click()
        driver.find_element_by_id('turnDownJobOffer-radio.label.no').click()
        driver.find_element_by_id('turnDownJobReferral-radio.label.no').click()
        driver.find_element_by_id('attendSchoolOrTraining-radio.label.no').click()
        driver.find_element_by_name('method:submit').click()
        time.sleep(5)
        driver.find_element_by_id('workSearch.field.label.claimWeek1Contacts').send_keys(str(week1_work_searches)[21])
        driver.find_element_by_id('workSearch.field.label.claimWeek2Contacts').send_keys(str(week2_work_searches)[21])
        driver.find_element_by_name('method:submit').click()
        time.sleep(5)
        driver.find_element_by_id('certifyClaim-radio.label.yes').click()
        driver.find_element_by_name('method:submit').click()
        driver.quit()

def login():
    driver.get('https://login.apps.twc.state.tx.us/UBS/security/logon.do')
    time.sleep(5)
    driver.find_element_by_id('field.label.username',).send_keys(my_username)
    driver.find_element_by_id('field.label.password',).send_keys(my_password)
    driver.find_element_by_name('method:logon').click()
    time.sleep(5)
    ## Call payment_request() to start the payment request after logging in.
    payment_request()

# LOGS YOU INTO TWC WEBSITE
login()



