import json
import requests
from tkinter import *

class FBI():
    def __init__(self, ori, data_year, offense, state, cleared, actual):
        self.ori = ori
        self.data_year = data_year
        self.offense = offense
        self.state = state
        self.cleared = cleared
        self. actual = actual

    def ToList(self):
        return [self.ori, self.data_year,self.offense, self.state,self.cleared,self.actual]

    def __eq__(self, other):        
        try:
            if(isinstance(other, FBI) and self.ToList() == other.ToList()): 
                return True
        except:
            raise ValueError("Type comparison with non-FBI object")
        
        return False

    def __repr__(self):
        raise NotImplementedError

    def __str__(self):
        return "ori: {},  data_year: {}, offense: {}, state: {}, cleared: {}, actual {}".format(str(self.ori), int(self.data_year), str(self.offense), str(self.state), int(self. cleared), int(self.actual))

    def Contains(self, value):
        for item in self.ToList():
            if str(item) == str(value):
                return True
        return False

    def DisplayDetailUI(self):
        root = Tk()
        root.title('Crime Detail Window')
        root.geometry('{}x{}'.format(400, 400))

        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # create all of the main containers
        center = Frame(root, bg='light blue', padx=3, pady=3)
        center.grid(row=0, sticky="nsew")

        strAPI = "https://api.usa.gov/crime/fbi/sapi/api/summarized/arson/states/" + self.state + "/1970/2018?API_KEY=evUMwadWWaakvXMP6e4RWDtn1FHDGTEuMM01ggSw"
        response = requests.get(strAPI)
        json_data = response.json()
        crimes_json = json_data['results']

        
        
        data_year = json_data.get("results")[0]['data_year']
        state_id =json_data.get("results")[0]['state_id']
        state_abbr =json_data.get("results")[0]['state_abbr']
        reported = json_data.get("results")[0]['reported']
        unfounded = json_data.get("results")[0]['unfounded']
        actual = json_data.get("results")[0]['actual']
        cleared = json_data.get("results")[0]['cleared']
        juvenile = json_data.get("results")[0]['juvenile_cleared']
        uninhabited = json_data.get("results")[0]['uninhabited']
        damage = json_data.get("results")[0]['est_damage_value']
            
        Label(center, text= "Year: " + str(data_year), width=20, pady=1, padx=1).grid(row=1, column = 0)
        Label(center, text= "State ID: " + str(state_id), width=20, pady=1, padx=1).grid(row=2, column = 0)
        Label(center, text= "State Abbreviation: " + str(state_abbr), width=20, pady=1, padx=1).grid(row=3, column = 0)
        Label(center, text= "Reported: " + str(reported), width=20, pady=1, padx=1).grid(row=4, column = 0)
        Label(center, text= "Unfounded: " + str(unfounded), width=20, pady=1, padx=1).grid(row=5, column = 0)
        Label(center, text= "Actual: " + str(actual), width=20, pady=1, padx=1).grid(row=6, column = 0)
        Label(center, text= "Cleared: " + str(cleared), width=20, pady=1, padx=1).grid(row=7, column = 0)
        Label(center, text= "Juvenile:" + str(juvenile), width=20, pady=1, padx=1).grid(row=8, column = 0)
        Label(center, text= "Uninhabited: " + str(uninhabited), width=20, pady=1, padx=1).grid(row=9, column = 0)
        Label(center, text= "Damage: " + str(damage), width=20, pady=1, padx=1).grid(row=10, column = 0)
    

        root.mainloop()
