from libs.csv import readconvert_file
from libs.login import get_password, get_username
from libs.redmine import new_issue
from libs.json import loadjson
from redminelib import Redmine
import sys

# collegamento Redmine
redmineobj = Redmine(loadjson()["server"], username=get_username(), password=get_password())

# lettura CSV
ticket_list = readconvert_file(loadjson()["inputfile"])

for item in ticket_list:
    #print(item)
    try:
      ticketnr = new_issue(redmineobj, item)
      print("Ticket creato: #{}".format(ticketnr))
    except:
      print("No connect")
      break
