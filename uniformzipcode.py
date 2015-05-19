#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is as follows:
- To uniform the zipcode field by striping all leading and trailing characters 
- before and after the main 5-digit zip code, which dropped all leading state 
- characters (as in “CA 94541”) and 4-digit zip code extensions following a hyphen.
"""
import re

def uniformzip(value_name, node):
    # pick the zipcode from the zipcode list
    zipcodes = value_name.split(";")
    for zipcode in zipcodes:
        # remove the other characters before the numbers 
        m = re.search("\d", zipcode)
        zipcode = zipcode[m.start():]
        # test if the zipcode only contains numbers by removing additional space
        if isint(zipcode.strip()):
            # initlize if there is no aipcodes filed in the dictionary 
            if "address" not in node:
                node['address'] = {}
            if "zipcodes" not in node['address']:
                node["address"]["zipcodes"] = []
            
            # append the zipcode if it is not in the exisiting list            
            if zipcode.strip() not in node["address"]["zipcodes"]:
                node["address"]["zipcodes"].append(zipcode.strip())
            else:
                continue#print zipcode
        
                        

    return node

def isint(value):
  try:
    int(value)
    return True
  except:
    return False
