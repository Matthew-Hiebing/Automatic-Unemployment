# Automatic Unemployment Payment Request Script:desktop_computer: :briefcase:
 Automatically goes through Texas Workfoce Commision unemployment payment request workflow every other Tuesday (filing day).
 
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
