#!/usr/bin/env python
"""
Your task is as follows:
- To uniform the city name field by removing the redundant info (Oakland, Ca,), 
uniform the upper case and lower case issue with only capitalizing 
the first letter and correcting the misspelling issues


"""
def uniformaddress(city_name, node):
    # remove any space before and after the city name and uniform the format by capitalize. If it contains multiple fields which is sperated by ".", 
    # only output the first part
    city_name = city_name.strip().capitalize().split(".")[0]
    # correct the mainly common typo 
    if  city_name == "San Francicsco":
        city_name = "San Francisco"

    if "address" not in node:
        node['address'] = {}

    # add the uniform city name to the final address
    node["address"]["city"] = city_name
    

    return node
