"""
    .py script to consolidate data from different sources (agmarknet, fca, shapefile administrational data)

"""
import glob
from os import path
import sys
import csv
import re

import cleaner

data_dir = '../../data'
district_dict = {}

def main():
    admin = path.join(data_dir, 'state_district_taluk.csv')
    with open(admin, 'r') as admin_csv:
        admin_reader = csv.reader(admin_csv)
        for row in admin_reader:
            (state, district, taluk) = row
            if 'n.a.' in taluk:
                match = re.search(r'[0-9]+', taluk)
                taluk = match.group(0)
            if state in district_dict:
                if district in district_dict[state]:
                    if taluk not in district_dict[state][district]:
                        district_dict[state][district] = district_dict[state][district] + [taluk]
                else:
                    district_dict[state][district] = []
            else:
                district_dict[state] = {}

    print district_dict

    markets = path.join(data_dir, 'markets')
    for name in glob.glob(markets+'/*.csv'):
        geo_states = district_dict.keys()
        with open(name, 'r') as statemarkets_csv:
            csv_reader = csv.reader(statemarkets_csv)
            header = True
            for row in csv_reader:
                state = row[0] 
                if not header:
                    print row
                if not header:
                    break
                header = False
        break

if __name__ == "__main__":
    main()
