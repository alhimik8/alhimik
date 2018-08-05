#!/usr/bin/python
# -*- coding: utf-8 -*-
# Search script for csv database
#

import csv
import sys
import time
import os
from os.path import abspath, exists
csv_file = abspath("database.txt")
enc = "windows-1251"
sharpline = "#######################################################"
try:
    def fio():
        with open(csv_file, "r", encoding=enc) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter="|")
            while True:
                try:
                    print(sharpline)
                    name_input = input("ПІБ             : ")
                    date_input = input("Дата народження : ")
                    strt_input = input("Вулиця          : ")
                    addr_input = input("Будинок         : ")
                    start_time = time.time()
                    if len(name_input + date_input +strt_input + addr_input) <= 0:
                        raise ValueError('empty string')
                    else:
                        print("\nШукаємо...")
                        counter = 0
                        for num, row in enumerate(csv_reader):
                            if name_input in row[2] and date_input in row[6] and strt_input in row[8] and addr_input in \
                                    row[8]:
                                counter += 1
                                print("\n", counter)
                                print("ПІБ   :", row[2])
                                print("Дата  :", row[6])
                                print("Адреса:", row[8])
                        print("\nЗагалом знайдено - ", counter, "- персон.\n")
                        print(sharpline)
                        end_time = time.time()
                        print("--- Час пошуку %s секунд ---" % (time.time() - start_time))
                    break
                except ValueError:
                        print("\nПомилка!\nУсі поля вводу пусті.\nДодайте хоч якусь інформацію для пошуку!\n")
    fio()
except FileNotFoundError:
    print("\nПомилка!. \nНе знайдено файл бази {0}.".format(csv_file))
