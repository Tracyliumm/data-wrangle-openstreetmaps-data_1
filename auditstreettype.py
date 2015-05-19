#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from collections import defaultdict
import re

"""
# The function of this file is to get the street type of the address field
"""

osm_file = open("sample.osm", "r")

#Search special characteristics in the attribute fields
street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)

#initialize the street type
street_types = defaultdict(int)

# The main function to test each street name and pick the ones followed the rules and add them to the dictionary
def audit_street_type(street_types, street_name):
    
     # search to see the given street name contains the special characteristics
    m = street_type_re.search(street_name)
    # if the given street name contains the special characteristics
    if m:
        # obtain the street type from street name
        street_type = m.group()
        
        # add the street type to the dictionary        
        street_types[street_type] += 1


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

# test a given value follows the street and address pattern
def is_street_name(elem):
    #return (elem.tag == "tag") and (elem.attrib['k'] == "addr:street")
    return (elem.tag == "tag") and (elem.attrib['k'] == "address")

def audit():
    # # open osm file and iterate through elements
    for event, elem in ET.iterparse(osm_file):
        # test a given value follows the street and address pattern
        if is_street_name(elem):
            #test each street name and pick the ones followed the rules and add them to the dictionary
            audit_street_type(street_types, elem.attrib['v'])
            print elem.attrib['v']
    
    #output sorted dictionary        
    print_sorted_dict(street_types) 

if __name__ == '__main__':
    audit()
