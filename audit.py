#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
import xml.etree.ElementTree as ET
import pprint
import re
from collections import defaultdict
import json
import pymongo

"""
The function of this file is to get the tag field (key and value) of the node and way 
# element for the input osm file:
"""

#Search and filter the problem characteristics in the attribute fields
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def examine_tags(osmfile):
  
    # open osm file
    osm_file = open(osmfile, "r")

    # initialize data with default set data structure
    data = defaultdict(set)

    # iterate through elements
    for _, elem in ET.iterparse(osm_file, events=("start",)):
        # check if the element is a node or way
        if elem.tag == "node" or elem.tag == "way":
            # iterate through children matching `tag`
            for tag in elem.iter("tag"):
                key = tag.get('k')
                val = tag.get('v')
                # skip if does not contain key-value pair or the key or value contains problematic string
                if 'k' not in tag.attrib or 'v' not in tag.attrib or problemchars.search(key) or problemchars.search(val):
                    continue
                print elem.attrib
                print "tag=", tag.attrib, "key = ", key, "val =", val
                # add to set if in tag keys of interest and is below the item limit
                #if key in tag_keys and len(data[key]) < item_limit:
                #    data[key].add(val)
    return data

def test():
    # call examine_tags fucntion
    tag_data = dict(examine_tags('sample.osm'))

    

if __name__ == '__main__':
    test()
