# Automatic Unemployment Payment Request App:desktop_computer: :briefcase:
With millions of people out of work and trying to file for unemployment during the Covid 19 pandemic, the Texas Workforce Commission (TWC) website became bogged down, usually crashing while you're trying to fill out the last piece of information for your payment request. If you can't fill out the form, you have to make the dreaded 'phone call' and wait for hours, and that's only if you can eventually get through.

I created a simple script to automate the process for anyone who doesn't want to risk not being able to make their bi-weekly payment requests.  I noticed that the site worked a lot better in the middle of the night or early hours of the morning.  I would recommend setting up Windows Task Schedular during these times when the site sees less traffic, you'll have the highest chance of successfully making payment requests this way.

Notes:
The script will automatically pull your two claim weeks and use them to add up the number of job searches you completed for each claim week.
See the examples .py, yml, and .xlxs files to set things up for yourself.  The .py file called, "Payment_Request" is my working file.  I included it if you want to see how I have things set up.  The script will only successfully execute if it run on the correctly payment request day.  If the script is executed outside of this day an error message will post in the console telling you which day you were supposed to make a request.
 
## Programming Language(s)

Python was used as the primary programming language.
Windows Task Schedular was used to run Python script every other Tuesday(or whichever day is your official filing day).


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages:

```bash
pip install pandas
pip install numpy
pip install selenium
pip install xlrd
pip install PyYAML
```

## Usage

```python
import pandas as pd
import numpy as np
import time
import yaml
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pd.read_excel('excel.xlsx') # returns data
pd.DataFrame(data) # returns your dataframe
yaml.load(file.yaml) # returns your stored username and password
webdriver.Firefox('path to geckodriver.exe') # starts your browser using geckodriver.exe
```

## Questions?
Send me a message on GitHub (Matthew-Hiebing) or E-mail me at: Matthew.Hiebing@gmail.com


