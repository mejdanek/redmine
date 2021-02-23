#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

""" Redmine app """

from libs.csv import readconvert_file
from libs.login import get_password, get_username
from libs.redmine import new_issue
from libs.json import loadjson
from redminelib import Redmine
import sys
import logging

logging.basicConfig(filename='logs/example.log',level=logging.DEBUG)

def main():
  """ Launcher """
  # Redmine link
  redmineobj = Redmine(loadjson()["server"], username=get_username(), password=get_password())

  # CSV fetch
  ticket_list = readconvert_file(loadjson()["inputfile"])

  for item in ticket_list:
      try:
        ticketnr = new_issue(redmineobj, item)
        print("Ticket creato: #{}".format(ticketnr))
      except:
        print("No connect")
        break

if __name__ == "__main__":
  main()