import json
import requests
from tkinter import *
from Class_FBI import FBI


real_res = None
displayElments = []
root = Tk()
root.title('Crime Summary')
root.geometry('{}x{}'.format(900, 600))
top_frame = Frame(root, bg='black',padx=3, pady=3)
name = StringVar()
entry_keyword = Entry(top_frame, textvariable = name, background="green")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# create all of the main containers
center = Frame(root, bg='cyan', padx=3, pady=3)
top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")

# create the widgets for the top frame
model_label = Label(top_frame, text='Filter Crime')

# layout the widgets in the top frame
model_label.grid(row=0, columnspan=2)
entry_keyword.grid(row=1, column=0)

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


stateAbbr = ""
def GetState(stateAbbr):
    stateAbbr = input("What state? ").upper()
    while stateAbbr not in states:
        print("invalid state, please try again")
        stateAbbr = input("What state? ").upper()
    return stateAbbr
stateAbbr = GetState(stateAbbr)
            

API = "https://api.usa.gov/crime/fbi/sapi/api/summarized/state/" + stateAbbr + "/arson/2000/2018?API_KEY=evUMwadWWaakvXMP6e4RWDtn1FHDGTEuMM01ggSw"

response = requests.get(API)
json_data = response.json()
crimes_json = json_data['results']
results = []

for crime in crimes_json:
    results.append(FBI(crime['ori'], crime['data_year'], crime['offense'], crime['state_abbr'], crime['cleared'],crime['actual']))


def reset():
    arr = center.grid_slaves()
    for elem in arr:
        elem.destroy()
    DisplaySummaryUI(results)
    root.update()

def FilterCrimes():
    filtered_text = name.get()
    real_res = [res for res in results if res.Contains(filtered_text)]
    
    arr  = center.grid_slaves()
    for elment in arr:
        elment.destroy()
    DisplaySummaryUI(real_res)
    root.update()
   
    print("The create a filtered crime UI here by keyword:", [str(res) for res in real_res]) 

button = Button(top_frame, text= "Submit", command= FilterCrimes) 
button.grid(row=1, column=1)
button2 = Button(top_frame, text="Reset", command=reset)
button2.grid(row=1, column=2)

i = 0
for result in results:
    Button(center, text="Crime Details!", command=result.DisplayDetailUI).grid(row=i, column = 0)
    Label(center, text=result, width=100, pady=3, padx=3).grid(row=i, column = 1)
    i+=1
def DisplaySummaryUI(crimes):
    i = 0
    for crime in crimes:
        Button(center, text="Crime Details!", command=crime.DisplayDetailUI).grid(row=i, column = 0)
        Label(center, text=crime.ori, width=10, pady=1, padx=1).grid(row=i, column = 1)
        Label(center, text=crime.data_year, width=10, pady=1, padx=1).grid(row=i, column = 2)
        Label(center, text=crime.offense, width=20, pady=1, padx=1).grid(row=i, column = 3)
        Label(center, text=crime.state, width=20, pady=1, padx=1).grid(row=i, column = 4)
        Label(center, text=crime.cleared, width=20, pady=1, padx=1).grid(row=i, column = 5)
        Label(center, text=crime.actual, width=20, pady=1, padx=1).grid(row=i, column = 5)
        i += 1
root.mainloop()



