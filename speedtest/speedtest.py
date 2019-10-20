from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
import requests
from itertools import count
import time
import matplotlib.pyplot as plt


class WifiSpeed:

    def __init__(self):
        pass

    def GetSpeed(self):
        appendData = open('./data', 'a')

        browser = webdriver.Chrome('./chromedriver')
        browser.get('https://fast.com')

        data = browser.find_element_by_id('speed-value')

        if data:
            time.sleep(25)
            value = data.text
            print(value, end=' -> ')

            appendData.write(value + ',')
            print('Data added')
            appendData.close()
            browser.close()

    def GetRawData(self):
        data = open('data', 'r')

        items = data.read()
        single_item = items.split(',')

        for i in range(len(single_item) - 1):
            print(single_item[i])

    def GraphData(self):

        file = open('data', 'r')
        read = file.read()
        item = read.split(',')

        x = []
        y = []
        index = count()

        for i in range(len(item) - 1):
            x.append(next(index))
            y.append(int(item[i]))
            plt.cla()
            plt.plot(x, y)
            plt.pause(1)

        plt.xlabel('No. of Data')
        plt.ylabel('Data Value')
        plt.title('Internet Speed')
        plt.show()
