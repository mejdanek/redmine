#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

""" CSV handling script """

def readconvert_file(filepath):
    elements = []
    try:
        # open list file
        file = open(filepath, "r")
        # read every line and append to list
        for line in file:
            project, device, version = line.strip("\n").split(";")
            elements.append((project, device, version))
        # return as a list
        return elements
    except FileNotFoundError:
        print("Path to file not found!")
        return None

if __name__ == "__main__":
    print("Not directly executable")