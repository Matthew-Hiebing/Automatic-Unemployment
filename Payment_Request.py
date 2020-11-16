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
    time.sleep(3)
    driver.find_element_by_id(usernameID).send_keys(my_username)
    driver.find_element_by_id(passwordID).send_keys(my_password)
    driver.find_element_by_name(login_button).click()

login(
    'https://login.apps.twc.state.tx.us/UBS/security/logon.do',
    'field.label.username',
    'field.label.password',
    'method:logon'
)

# def payment_request(payment_request):
#     driver.find_element_by_xpath(payment_request).click()
#     if (driver.find_element_by_class_name('page-name').text) == 'Early Filing':
#         print('Try to file again on:',
#         driver.find_element_by_class_name('page-block').text[162:180])
#         driver.quit()

# payment_request(
#     '/html/body/div/div[3]/div[1]/div/ul[1]/li[4]/a',
# )

#-----------------------------------------------------------------------------#
# Read excel file and sum work searches for week 1 and week 2.
data = pd.read_excel(
    r'C:\Users\Matt\Dropbox\1 Job Search Related Items\Daily Work Log.xlsx',
    sheet_name='TWC Work Search Log'
)

df = pd.DataFrame(data, columns= ['Date of Activity', 'Work Search Count'])

week1_start_date = '11-01-2020'

date_1 = datetime.datetime.strptime(week1_start_date, r'%m-%d-%Y')
end_date1 = date_1 + datetime.timedelta(days=7)

after_week1 = (df[df['Date of Activity'] >= date_1])
before_end_date1 = (df[df['Date of Activity'] <= end_date1])
between_two_dates1 = (df[(df['Date of Activity']>=date_1) &
(df['Date of Activity']<=end_date1)])

week1_work_searches = between_two_dates1.sum()
print(week1_work_searches)

#--------Week 1--------------------#

week2_start_date = '11-09-2020'

date_2 = datetime.datetime.strptime(week2_start_date, r'%m-%d-%Y')
end_date2 = date_2 + datetime.timedelta(days=7)

after_week2 = (df[df['Date of Activity'] >= date_2])
before_end_date2 = (df[df['Date of Activity'] <= end_date2])
between_two_dates2 = (df[(df['Date of Activity']>=date_2) &
(df['Date of Activity']<=end_date2)])

week2_work_searches = between_two_dates2.sum()
print(week2_work_searches)





