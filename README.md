# Automatic Unemployment
 Automatically goes through TWC unemployment payment request workflow every other week.
 
## Programming Language(s)
```bash
Python was used as the primary programming language for this script.
Windows Task Schedular was used to run Python script every other week.
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages:

```bash

pip install pandas
pip install numpy
pip install selenium
pip install xlrd
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

pd.read_excel('excel.xlsx') #returns your data
pd.DataFrame(data) #returns your dataframe

```
