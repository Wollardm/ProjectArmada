import requests
from pprint import pprint
import json

# This key and token is mine, may have to use your own.
# You can find that at https://trello.com/app-key for the key
# and click the token hyperlink to get your token
KEY = "aa553a1b57161bdb848dfc981556423b"
TOKEN = "980b47252f80bb07b86cd5e8492db7ee74c7a8f345940e6047dcf171c0a2f3e4"
ARMADA_BOARD = "m2SSwukt"
SPRINT = "Sprint - 1"

card_url = ("https://api.trello.com/1/boards/"
            + ARMADA_BOARD
            + "/cards/"
            + "?key="
            + KEY
            + "&token="
            + TOKEN)

member_url = ("https://api.trello.com/1/boards/"
            + ARMADA_BOARD
            + "/members/"
            + "?key="
            + KEY
            + "&token="
            + TOKEN)
        
response = requests.request("GET", card_url)
cards = response.json()
response = requests.request("GET", member_url)
members = response.json()

id_to_member = {}
sprint_tasks = {}
for member in members:
    id_to_member[member['id']] = member['fullName']
    sprint_tasks[member['fullName']] = []

for card in cards:
    for label in card['labels']:
        if(label['name'] == SPRINT):
            for usrID in card['idMembers']:
                sprint_tasks[id_to_member[usrID]].append(card)

for member in sprint_tasks.keys():
    print(member
        + ":\n"
        + str(len(sprint_tasks[member]))
        + " Tasks - ", end='')
    esttime = 0
    acttime = 0
    for task in sprint_tasks[member]:
        desc = task['desc']
        time_strings = desc.split('###')[1:]
        esttime += int(time_strings[0].split(' ')[1])
        acttime += int(time_strings[1].split(' ')[1])
        
    print("Total Estimated Time: "
         + str(esttime)
         + " - Total Actual Time: "
         + str(acttime))
        