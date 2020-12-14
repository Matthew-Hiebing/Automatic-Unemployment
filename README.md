# Automatic Unemployment Payment Request Script:desktop_computer: :briefcase:
With millions of people trying to file for unemployment and peform payment requests through Texas' Workfoce Commision (TWC) website, the site has become bogged down, usually crashing while you're trying to fill out your information for a payment request. I created a simple script to automate the process.  You can use Windows Task Schedular to run this script in the middle of night, typically when there's less site-traffice. Make sure to have your task scheduler only run the script on your filing day that is provided by TWC.

Notes:
The script will automatically pull your two claim weeks and use them to add up the number of job searches you completed for each claim week.
See the examples .py, yml, and .xlxs files to set things up for yourself.  The .py file called, "Payment_Request" is my working file.  I included it if you want to see how I have things set up.
 
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
