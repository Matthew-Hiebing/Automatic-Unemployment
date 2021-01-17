# Automatic Unemployment Payment Request App:desktop_computer: :briefcase:
With millions of people out of work and trying to file for unemployment during the Covid-19 pandemic, the Texas Workforce Commission (TWC) website has become bogged down, usually crashing during the payment request process. Once the website stops working you have to make the dreaded 'phone call' and wait for hours, and that's only if you can eventually get through.

I noticed that the site works a lot better in the middle of the night or early hours of the morning.  I created a simple script to automate the process for anyone who doesn't want to risk not being able to make their bi-weekly payment request.  I recommend using Windows Task Schedular to set up a run time in the middle of the night when the site experiences less traffic, you'll have the highest chance of successfully making payment requests this way.

Notes:
The script will automatically pull your two claim weeks and use them to add up the number of job searches you completed for each claim week.
See the example .py, yml, and .xlxs files to set things up for yourself.  The .py file called, "Payment_Request" is my working file, I included it if you want to see a real-time example.  The script will only successfully execute if it run on the correct payment request day.  If the script is executed outside of this day an error message will post in the console telling you which day you were supposed to make a request.
 
## Programming Language(s)
Python was used as the primary programming language.
Windows Task Schedular was used to run the Python script every other Tuesday(or whichever day is your official filing day).


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

## Windows Task Scheduler Setup
I found Windows Task Scheduler to be a bit difficult to set up.  Here's a quick breakdown of the setup process:\

1.) Create a new task in Windows Task Scheduler.\
![Imgur](https://i.imgur.com/wCeQ3HF.jpg)

2.) Set your "Triggers".  Set this to the day you wantt the script to run and have it run every two weeks.\
![Imgur](https://i.imgur.com/NHVgAgo.png)

3.) Set your "Actions".  This part is a little tricky.\
* Set your action to "Start a program".  In "Program/script" navigate to the location where you have Python installed on your computer.
* In "Add arguments" enter the name of your Python script.  Mine is called, "Payment_Request".
* In "Start in" enter the location of the folder that holds your Python script.  In my case, its the name of the repository folder on my computer.\
![Imgur](https://i.imgur.com/WLpDRHv.png)

After you complete the above steps you should be good to go!

## Questions?
Send me a message on GitHub (Matthew-Hiebing) or E-mail me at: Matthew.Hiebing@gmail.com
