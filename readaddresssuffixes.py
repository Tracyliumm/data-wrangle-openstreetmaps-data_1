#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file as gold standard for the full address list
- find and possible mapping between the address suffixes and the full name 


"""

import xlrd
#datafile = "USPS Street Suffixes.xls"



def get_address_suffixes(datafile):
    # open the excle file
    workbook = xlrd.open_workbook(datafile)
    # pick the correct worksheet
    sheet = workbook.sheet_by_index(0)
    
    data = {}
    # for each row from the second row to the end ( the first one is the header)
    for r in range(1, sheet.nrows):
        # get the Street Suffixes    
        cell_value_id =sheet.cell(r,2).value
        # get the full street name
        cell_value_value = sheet.cell(r,1).value
        
        # pick the one which contains both field and set up the mapping
        if len(cell_value_id) > 0 and len(cell_value_value) >0:
            # uniform the key and value by capitalize the letters and add it to the final mapping
            data[cell_value_id.capitalize()] = cell_value_value.capitalize()
            #add '.' to the suffixes
            # add addtional mapping with the Street Suffixes + "."
            cell_value_id = cell_value_id.capitalize() + "."
            data[cell_value_id] = cell_value_value.capitalize()
     
    #Correct the misspellings 
    data["Boulavard"] = "Boulevard"
    data["Boulavard."] = "Boulevard"
    data["Steet"] = "Street"
    data["Steet."] = "Street"
    return data


