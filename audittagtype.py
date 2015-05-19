#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from collections import defaultdict
import re

"""
The function of this file is to get the specific field 
(city, country,zipcode) field for each tag field
"""

# open osm file
osm_file = open("sample.osm", "r")

 # initialize data with default set data structure
tag_types = defaultdict(int)

# The function to  add the tag name to the tag_types dictionary
def audit_tag_type(tag_types, tag_name):
    tag_types[tag_name] += 1

# output sorted dictionary
def print_sorted_dict(d):
    # get the key of a dictionary    
    keys = d.keys()
    # sort the key based on dictionary    
    keys = sorted(keys, key=lambda s: s.lower())
   # loop the sorted key and output the key value pair    
    for k in keys:
        v = d[k]
        print "%s: %d" % (k, v) 

# test a given value follows the specific pattern
def is_tag_name(elem):
    #search possible city name
    #return (elem.tag == "tag") and (elem.attrib['k'] == "addr:city")

    #search possible county name
    #return (elem.tag == "tag") and (elem.attrib['k'] == "tiger:county")
    
    #search possible zipcode
    return (elem.tag == "tag") and (":zip" in elem.attrib['k'] or ":postcode" in elem.attrib['k'])
    #return (elem.tag == "tag") and (":postcode" in elem.attrib['k'])

def audit():
   # open osm file and iterate through elements     
    for event, elem in ET.iterparse(osm_file):
        # test a given value follows the street and address pattern        
        if is_tag_name(elem):
           #test each street name and pick the ones followed the rules and add them to the dictionary
            audit_tag_type(tag_types, elem.attrib['v'])

   #output sorted street_types           
    print_sorted_dict(tag_types) 

if __name__ == '__main__':
    audit()
