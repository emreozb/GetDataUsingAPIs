import json
import requests
from Cls_Stocks import Stock
from tkinter import *

stocksAPI = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol=BTC&market=CNY&apikey=2IAOHC5BR0PRRYJC"

real_res = None
displayElments =[]
root = Tk()
root.title('Model Definition')
root.geometry('{}x{}'.format(460, 350))
top_frame = Frame(root, bg='purple',padx=3, pady=3)
name = StringVar()
entry_keyword = Entry(top_frame, textvariable = name, background = "light gray")
dateType = ""

response = requests.get(stocksAPI)
json_Stocks = response.json()
currency_data = json_Stocks.get("Time Series (Digital Currency Weekly)")
results = []


for data in currency_data:
    if dateType in data:
        results.append(Stock(currency_data[data]['1b. open (USD)'], currency_data[data]['2b. high (USD)'], currency_data[data]['3b. low (USD)'], currency_data[data]['4b. close (USD)']))



# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# create all of the main containers
center = Frame(root, bg='black', padx=3, pady=3)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")

# create the widgets for the top frame
model_label = Label(top_frame, text='Filter Example')
width_label = Label(top_frame, text='Filter by keyword:')
entry_W = Entry(top_frame, background="white")
button = Button(top_frame, text="Submit")

# layout the widgets in the top frame
model_label.grid(row=0, columnspan=3)
width_label.grid(row=1, column=0)
entry_W.grid(row=1, column=1)
button.grid(row=1, column=2)

real_res = None
displayElments = []



def reset():
    arr = center.grid_slaves()
    for elem in arr:
        elem.destroy()
    DisplaySummaryUI(results)
    root.update()

def FilterCurrency():
    filtered_text = name.get()
    real_res = [res for res in results if res.Contains(filtered_text)]
    
    arr  = center.grid_slaves()
    for elment in arr:
        elment.destroy()
    DisplaySummaryUI(real_res)
    root.update()
   
    print("The create a filtered currency UI here by keyword:", [str(res) for res in real_res]) 

button = Button(top_frame, text= "Submit", command= FilterCurrency) 
button.grid(row=1, column=1)
button2 = Button(top_frame, text="Reset", command=reset)
button2.grid(row=1, column=2)

i=0
for result in results:
    Button(center, text = "Bitcoin Details", command = result.DisplayDetail).grid(row=i, column=0)
    Label(center, text=results[i], width=10, pady=5, padx=125).grid(row=i, column = 1)
    i += 1

# j=0
# for date in currency_data:
#         Label(center, text=date, width=4, pady=3, padx=25).grid(row=j, column = 0)
#         j += 1
def DisplaySummaryUI(currency):
    
    i = 0
    for c in currency:
        Button(center, text="Bitcoin Details!", command=c.DisplayDetail).grid(row=i, column = 0)
        Label(center, text=c.op, width=10, pady=1, padx=1).grid(row=i, column = 1)
        Label(center, text=c.high, width=10, pady=1, padx=1).grid(row=i, column = 2)
        Label(center, text=c.low, width=20, pady=1, padx=1).grid(row=i, column = 3)
        Label(center, text=c.close, width=20, pady=1, padx=1).grid(row=i, column = 4)
        i += 1

root.mainloop()


