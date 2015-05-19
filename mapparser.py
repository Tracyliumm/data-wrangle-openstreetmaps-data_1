#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.ElementTree as ET
import pprint
import operator

def count_tags(filename):
        # YOUR CODE HERE
        tag_count = {}
        tag_key_count = {}
        # open osm file and iterate through elements     
        for _, element in ET.iterparse(filename, events=("start",)):
            # count the number of tag and the key of tag
            add_tag(element.tag, tag_count)
        
            # count the key of each tag and add the key to the dictionary 
            if element.tag == 'tag' and 'k' in element.attrib:
                tag_key = element.get('k')
                add_tag(tag_key, tag_key_count)
        
        #sorted_tag_key_count= sorted(tag_key_count.items(), key=lambda x: x[1])[::-1]
        sorted_tag_key_count= sorted(tag_key_count.items(), key=operator.itemgetter(1), reverse=1)
        #sorted_tag_key_count= sorted(tag_key_count.values(), reverse=1)[:3]
        
        return tag_count, sorted_tag_key_count

        
def add_tag(tag, tag_count):
    """ adds a tag to tag_count, or initializes at 0 if does not yet exist """
    if tag in tag_count:
        tag_count[tag] += 1
    else:
        tag_count[tag] = 1
        
        
def test():

    #tags = count_tags('san-francisco_california.osm')
    tags, tagkeys = count_tags('sample.osm')
    pprint.pprint(tags)
    pprint.pprint(tagkeys[:30])
    
   # assert tags == {'bounds': 1,
   #                  'member': 3,
   #                  'nd': 4,
   #                  'node': 20,
   #                  'osm': 1,
   #                  'relation': 1,
   #                  'tag': 7,
   #                  'way': 1}

    

if __name__ == "__main__":
    test()
