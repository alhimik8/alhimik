Script written in python 3.5
It`s pasrsing  some categories at elmir.ua shop and exporting results to csv and xls files, with time-date stamp in filename,
to easily compare prices from different dates.
In format:

Price from,2018-01-30 22:22,
Item Name ,Item Price,Item Url

Add your own categories to "categories"

Script also used to search and filter some items to buy - directly from console.

$ csvtool readable elmir_price_300118_2254.csv |grep 1060|grep Asus
Видеокарта PCI-E  3Gb GeForce GTX1060 (DDR5) Asus (PH-GTX1060-3G)                                    12931            https://elmir.ua/video_cards/graphics_card_pci-e_3gb_geforce_gtx1060_ddr5_asus_ph-gtx1060-3g.html                                     
Видеокарта PCI-E  6Gb GeForce GTX1060 (DDR5) Asus (EX-GTX1060-O6G)                                   15580            https://elmir.ua/video_cards/graphics_card_pci-e_6gb_geforce_gtx1060_ddr5_asus_ex-gtx1060-o6g.html                                    
Видеокарта PCI-E  6Gb GeForce GTX1060 (DDR5) Asus (DUAL-GTX1060-O6G)                                 16017            https://elmir.ua/video_cards/graphics_card_pci-e_6gb_geforce_gtx1060_ddr5_asus_dual-gtx1060-o6g.html                                  
Видеокарта PCI-E  6Gb GeForce GTX1060 (DDR5) Asus (ROG-STRIX-GTX1060-6G-GAMING)                      17904            https://elmir.ua/video_cards/graphics_card_pci-e_6gb_geforce_gtx1060_ddr5_asus_rog-strix-gtx1060-6g-gaming.html 

MODULES need to import:
lxml
irequests
re
csv
datetime
urllib3
openpyxl
time


