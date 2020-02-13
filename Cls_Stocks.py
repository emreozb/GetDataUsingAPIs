import json
import requests
from tkinter import *

class Stock():
    def __init__(self, op, high, low, close):
        self.op = op
        self.high = high
        self.low = low
        self.close = close

    def ToList(self):
        return[self.op, self.high, self.low, self.close]

    def __eq__(self, other):        
        try:
            if(isinstance(other, Stock) and self.ToList() == other.ToList()): 
                return True
        except:
            raise ValueError("Type comparison with non-Stock object")
        
        return False

    def __repr__(self):
        raise NotImplementedError

    def __str__(self):
        return "Open: {},  High: {}, Low: {}, Close: {}".format(float(self.op), float(self.high),float(self.low), float(self.close))

    def Contains(self, value):
        for item in self.ToList():
            if str(item) == str(value):
                return True
        return False

    def DisplayDetail(self):
        root = Tk()
        root.title('Bitcoin Detail Window')
        root.geometry('{}x{}'.format(400, 400))

        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # create all of the main containers
        center = Frame(root, bg='light blue', padx=3, pady=3)
        center.grid(row=0, sticky="nsew")

        dailyAPI = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=R44HOS5CRU8ARE08"
        response = requests.get(dailyAPI)
        json_Stocks = response.json()
        currency_data = json_Stocks.get("Time Series (Digital Currency Daily)")
        
        dateType =""
        ## Details in Chinese Yuan 
        i = 0
        for i in range(len(currency_data)):
            open1 = currency_data.get("2020-02-02")["1a. open (CNY)"]
            high1 = currency_data.get("2020-02-02")["2a. high (CNY)"]
            low1 = currency_data.get("2020-02-02")["3a. low (CNY)"]
            close1 = currency_data.get("2020-02-02")["4a. close (CNY)"]


            Label(center, text= "Open: " + str(open1), width=20, pady=1, padx=1).grid(row=1, column = 0)
            Label(center, text= "High: " + str(high1), width=20, pady=1, padx=1).grid(row=2, column = 0)
            Label(center, text= "Low: " + str(low1), width=20, pady=1, padx=1).grid(row=3, column = 0)
            Label(center, text= "Close: " + str(close1), width=20, pady=1, padx=1).grid(row=4, column = 0)

        root.mainloop()