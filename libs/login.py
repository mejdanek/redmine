#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

""" Login management script """

from getpass import getpass

def get_username():
    return input("Username: ")

def get_password():
    return getpass("Password: ")

if __name__ == "__main__":
    print("Not directly executable")