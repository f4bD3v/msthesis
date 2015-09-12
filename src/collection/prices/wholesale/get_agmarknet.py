#!/usr/bin/env python2

import urllib2
import shutil
import re
import sys
import datetime
import os
from time import sleep
from optparse import OptionParser
from random import randint
from BeautifulSoup import BeautifulSoup

usage_str = """
This scripts downloads daily food prices from http://agmarknet.nic.in/cmm2_home.asp for a given commodity. Results are saved in CSV format to csv_out/ directory.

Usage:
    python2 download_agmarket_daily.py [options]

    -d DATE                 -- download data for this date
    -r STARTDATE ENDDATE    -- download all data in this date range
    -c COMMODITY            -- specify commodity (check at the website!)

Examples:

    python2 get_agmarknet.py -d 02/03/2012 -c Rice
    python2 get_agmarknet.py -r 20/01/2013 20/03/2013 -c Tea
"""

data_dir = '../../../../data/agmarknet'
csv_out_dir = os.path.join(data_dir, 'csv')
raw_out_dir = os.path.join(data_dir, 'html')

commodity = ''
family = ''


def download_data(date_string):
    """Download weekly prices in HTML and save them to file CSV"""

    main_url = "http://agmarknet.nic.in/cmm2_home.asp?comm=%s&dt=%s" % (commodity, date_string)

    req = urllib2.Request(main_url)
    response = urllib2.urlopen(req)
    result_html = response.read()
    print_csv(date_string, commodity, result_html)

def print_csv(date_string, commodity, html):
    # Remove some stuff
    html = re.sub(r'&nbsp;?', '', html)
    html = re.sub(r'</?font[^>]*>', '', html)
    soup = BeautifulSoup(html)
    tables = soup.findAll('table')
    if len(tables) < 4:
        # do not exit here, there may be data for other dates
        # sys.exit("ERROR: invalid commodity or no data")
        return
    else:
        table = tables[3]

    all_rows = []
    prev_city = ''
    cell_count = 0
    state = ''
    for row in table.findAll("tr"):
        cur_row = []
        cell_count = len(row.findAll("td"))
        print cell_count
        if cell_count == 1:
            state = row.findAll("td")[0].getText()
            print state
            continue

        for td in row.findAll("td"):   
            text = td.getText()
            cur_row.append(text)
        if len(cur_row) < 7: continue
        if cur_row[0] == 'Market': continue
        if cur_row[0] == '':
            cur_row[0] = prev_city
        else:
            prev_city = cur_row[0]
        cur_row[:0] = [state]
        cur_row = map(lambda s: re.sub(',', '_', s), cur_row)
        all_rows.append(cur_row)

    out_file_name = csv_out_dir + '/' + commodity  + '_' \
                    + re.sub('/', '_', date_string) + '.csv'
    raw_file_name = raw_out_dir + '/' + commodity  + '_' \
                    + re.sub('/', '_', date_string) + '.html'
    print "### Output file:", out_file_name
    out_file = open(out_file_name, "w")

    for r in all_rows:
        # clean out NR values
        del r[3]
        r = map(lambda x: "*" if x == "NR" else x, r)
        tonnes = r[2] #float('0' + re.sub(r'[^\d\.]', '', r[2]))
        # price per kg 
        r = map(lambda x: float(x)/100 if x.isdigit() else x, r)

        r[:0] = [date_string]
        r[3:3] = [commodity]
        del r[4]
        if not tonnes:
            tonnes = "-"
        r[5:5] = [tonnes]
        print r
        row_string = ", ".join([str(c) for c in r]) + "\n"

        # Use modal value
        #row_string = "{}, {}, {}, {}, {}, {}, {}, {}, {}".format(date_string, r[1], r[0], commodity, r[4], float(r[-3])/100, float(r[-2])/100, float(r[-1])/100, tonnes)

        out_file.write(row_string)
    out_file.close()

    # Save raw file
    table = str(table)
    raw_file = open(raw_file_name, "w")
    raw_file.write(table)
    raw_file.close()

def download_range(drange):
    srange, erange = drange
    sdate = validate_date(srange)
    edate = validate_date(erange)
    
    if sdate > edate:
        sys.exit("ERROR: start date > end date")

    curdate = sdate
    while curdate <= edate:
        print curdate
        download_data(curdate.strftime("%d/%m/%Y"))
        curdate += datetime.timedelta(days=1)
        #sleep(randint(1,3))

def validate_date(date_string):
    match = re.match(r'(\d{2})/(\d{2})/(\d{4})', date_string)
    if not match:
        sys.exit("ERROR: invalid date, " + date_string)
    day, month, year = int(match.group(1)), int(match.group(2)), int(match.group(3))
    date = datetime.date(year, month, day)
    return date

def check_out_dir():
    if not os.path.exists(csv_out_dir):
        os.makedirs(csv_out_dir)
    if not os.path.exists(raw_out_dir):
        os.makedirs(raw_out_dir)

def usage():
    print usage_str

def usage_callback(option, opt, value, parser):
    usage()
    sys.exit(1)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    parser = OptionParser(add_help_option=False)
    parser.add_option("-h", "--help",
                      action="callback", callback=usage_callback)

    parser.add_option("-r", "--range",
                      action="store", nargs=2, dest="drange")

    parser.add_option("-d", "--date",
                      action="store", nargs=1, dest="date")

    parser.add_option("-f", "--family", action="store", nargs=1, dest="family")

    parser.add_option("-c", "--commodity",
                      action="store", nargs=1, dest="commodity")
    
    (options, args) = parser.parse_args()

    if options.family:
        family = options.family
        csv_out_dir = os.path.join(csv_out_dir, family)
        raw_out_dir = os.path.join(raw_out_dir, family)

    check_out_dir()

    if not options.commodity:
        usage()
        sys.exit("No commodity given!")
    else:
        commodity = options.commodity
    if options.date:
        date_str = options.date
        date = validate_date(date_str)
        download_data(date_str)
    elif options.drange:
        download_range(options.drange)
    else:
        usage()
        sys.exit(1)
    print "### Finished."

