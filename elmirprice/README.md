Script written in python 3.5
It`s pasrsing  some categories at elmir.ua shop and exporting results to csv and xls files, with time-date stamp in filename,
to easily compare prices from different dates.
In format:

Price from,2018-01-30 22:22,
Item Name ,Item Price,Item Url

Add your own categories to "categories"

Script also used to search and filter some items to buy - directly from console.

$ csvtool readable elmir_price_300118_2254.csv |grep 1060|grep Asus

MODULES need to import:
lxml
irequests
re
csv
datetime
urllib3
openpyxl
time


