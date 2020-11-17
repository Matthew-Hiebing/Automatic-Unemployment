import pandas as pd
import numpy as np
import time
import yaml
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#-----------------------------------------------------------------------------#
# Log into Texas Workforce Commission website.
driver = webdriver.Firefox(
    executable_path=
    r'D:\Users\Matt\Documents\GitHub\Executable_Files\geckodriver.exe'
)

conf = yaml.load(open(r'D:\Users\Matt\Documents\GitHub\YML_Files\Unemployment_Credentials.yml'))

my_username = conf['Unemployment']['username']
my_password = conf['Unemployment']['password']

def login(url,usernameID,passwordID,login_button):
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_id(usernameID).send_keys(my_username)
    driver.find_element_by_id(passwordID).send_keys(my_password)
    driver.find_element_by_name(login_button).click()
    time.sleep(5)

login(
    'https://login.apps.twc.state.tx.us/UBS/security/logon.do',
    'field.label.username',
    'field.label.password',
    'method:logon'
)

def payment_request():
    driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/ul[1]/li[4]/a').click()
    if (driver.find_element_by_class_name('page-name').text) == 'Early Filing':
        print('Try to file again on:',
        driver.find_element_by_class_name('page-block').text[162:180])
        driver.quit()
    else:
        claim_week_pull = driver.find_element_by_class_name('page-header-row-value-1col').text[0:12]
        claim_week_convert_to_str = claim_week_pull.replace(',','')
        date_1 = datetime.datetime.strptime(claim_week_convert_to_str,r'%b %d %Y')

        #---------------------------------------------------------------------#
        # ADD UP WORK SEARCHES FOR WEEK 1
        data = pd.read_excel(
            r'C:\Users\Matt\Dropbox\1 Job Search Related Items\Daily Work Log.xlsx',
            sheet_name='TWC Work Search Log'
        )
        df = pd.DataFrame(data, columns= ['Date of Activity', 'Work Search Count'])

        end_date1 = date_1 + datetime.timedelta(days=6)

        between_two_dates1 = (df[(df['Date of Activity']>=date_1) & (df['Date of Activity']<=end_date1)])

        week1_work_searches = between_two_dates1.sum()
        print(date_1)
        print(end_date1)
        print(week1_work_searches)

        # ADD UP WORK SEARCHES FOR WEEK 2
        date_2 = date_1 + datetime.timedelta(days=7)
        end_date2 = date_2 + datetime.timedelta(days=6)

        between_two_dates2 = (df[(df['Date of Activity']>=date_2) &
        (df['Date of Activity']<=end_date2)])

        week2_work_searches = between_two_dates2.sum()
        print(date_2)
        print(end_date2)
        print(week2_work_searches)

        #---------------------------------------------------------------------#
        #CONTINUE PAYMENT REQUEST
        driver.find_element_by_id('addressChangeAnswer-radio.label.no').click()
        driver.find_element_by_name('method:submit').click()
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


payment_request()




