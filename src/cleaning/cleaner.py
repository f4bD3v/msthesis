import os
import sys

def check_occ(seq, district):
    val = True if (district in seq) else False
    return val

def check_window(districts, address, repeat):
    assigned_districts = []
    rgx='(?P<before>(\w+\s+){%s})\S*dist\S*(?P<after>(\s+\w+){%s})'%repeat
    # there will be a match if string is not empty
    match = re.search(rgx, address, re.IGNORECASE)
    # (" ".join(match.group('before').split()), " ".join(match.group('after').split()))
    for dist in districts_by_state:
        if check_occ(match.group('before'), dist):
            assigned_districts.append(dist)
        if check_occ(match.group('after'), dist):
            assigned_districts.append(dist)
    return assigned_districts

# call for each address (APMC + Secretary) and then do a union of results
def assign_district(districts_by_state, address):
    # check if string is empty
    if address:
        # heuristic, search for district name 
        # set window around 'dist' to 1
        assigned_districts = check_window(districts_by_state, address, 1)
        if not assigned_districts:
            # set window around 'dist' to 2
            assigned_districts = check_window(districts_by_state, address, 2)

        if not assigned_districts:
            # return districts contained in whole address
            for dist in districts_by_state:
                if dist in address:
                    assigned_districts.append(dist)

        return assigned_districts
    else:
        return ['*']

#def simplify_market_name(state, market_name):
