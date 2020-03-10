from tkinter import *
import json
import requests
from Class_WorldCup_Teams import team
from Class_WorldCup_Players import player

def RepopulateFrame(center):
    root = Tk()
    root.title('Search Results')
    root.geometry('{}x{}'.format(500, 200))
    center = Frame(root, bg='gray', padx=3, pady=3)
    center.grid(row=1, sticky="nsew")
    center.destroy() 
 

strAPI = "https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json"
response = requests.get(strAPI)
print(response)
json_data = response.json()
worldcup_data = json_data
list_worldcup = []
previous_team = ""
list_teamplayers = []


root = Tk()
root.title('World Cup Players')
root.geometry('{}x{}'.format(400, 700))

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# create all of the main containers
top_frame = Frame(root, bg='cyan',padx=3, pady=3)
center = Frame(root, bg='gray', padx=3, pady=3)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")

year = int(input("What World Cup year are you looking for? "))

for record in worldcup_data:
    if(year == record["Year"]):
        if(previous_team == ""):    
            previous_team = record["Team"]
        if(previous_team != record["Team"]):
            list_worldcup.append(team(record["Year"], previous_team, list_teamplayers))
            list_teamplayers =[]
            previous_team = record["Team"]
        if (record["FullName"] != ""):
            list_teamplayers.append(player(record["FullName"])) 
        
list_worldcup.append(team(record["Year"], previous_team, list_teamplayers))


# create the widgets for the top frame
model_label = Label(top_frame, text='Filter Example')
width_label = Label(top_frame, text='Filter by keyword:')
    
# layout the widgets in the top frame
model_label.grid(row=0, columnspan=3)
width_label.grid(row=1, column=0)


keyword = Entry(top_frame, background="pink" , font = ("Times New Roman", "14", "bold"))
keyword.grid(row=1, column=1)

button = Button(top_frame, text="Submit", command=lambda: RepopulateFrame(center))
button.grid(row=1, column=2)


i = 2
for teams in list_worldcup:
    playList = ""
    for play in teams.players:  
        playList += play.fullname + "\n"

        Button(root, text=teams.team, command = player(playList).create_window, width=18, pady=3, padx=3).grid(row=i, column = 0) 
         
    i += 1 



root.mainloop()
