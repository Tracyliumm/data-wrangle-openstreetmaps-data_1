#!/usr/bin/env python
"""
Your task is as follows:
- uniform the street names by translating all abbreviations into the full forms, e.g. Blvd to Boulavard and
- all “.” characters were removed. 

"""
import re

# Search and filter by special characteristics in the attribute fields
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]

def getUniformedStreetName(ori_name, mapping):
    # get the original street name and uniform it with capitalize the first letter
    ori_name = ori_name.capitalize()
    # search if the field name contains special characteristics
    m = street_type_re.search(ori_name)
    
    if m:
        street_type = m.group().capitalize()
        
        # if the street name in the original list, keep it
        if street_type in expected:
           better_name = ori_name
        # if the street name is not in the original list but in the mapping key list, find the mapping from golden standard   
        elif street_type not in expected and street_type in mapping.keys():
           better_name = update_name(ori_name, mapping)
        # else the street name is set as empty   
        else:
           better_name = ''
    else:
        better_name = ''
        
    return better_name
 
def update_name(name, mapping):

    # YOUR CODE HERE
    # remove the street name by removing the first redundant filed ( city and state) which is separated by space and niform it with capitalize the first letter
    oldaddtype = name.split(' ')[-1].capitalize()

    newname = name.replace(oldaddtype, mapping[oldaddtype])
    name = newname

    return name
