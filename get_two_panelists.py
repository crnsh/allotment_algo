"""
Author - Karan Handa
Purpose - Allotment Algorithm for Interviews

Setup - 
1.  Ignore all files other than
    a.  get_two_panelists.py
    b.  responses.csv
    c.  output.txt
2.  In responses.csv, Export the Google Sheet in CSV format (https://docs.google.com/spreadsheets/d/1xitxlVP94su_itUcgdxbc7x9asFnrUC-0ziESBQsHhs/edit#gid=1588020992)
3.  Run "python3 get_two_panelists.py"
4.  The output will be will in "output.txt" containing allotment of 3-person-interview-groups
    with corresponding interviewees.
5.  At the bottom of "output.txt", the number of interviewees assigned to each 3-person-group
    will be given.
6.  Answer contains the most balanced answer achieved so far.
"""

from secrets import choice
import pandas as pd
import sys
import random
from collections import Counter

panelist_groups = ( 
    ("Neha Sheik (UG'23)","Arjun Khanna (UG'23)","Rajvee Parikh (UG'23)"), 
    ("Miloni Shah (UG'23)", "Yasashvi Parakh (UG'23)", "Harsh Gupta (UG '23)"), 
    ("RochaN Mohapatra (UG'23)", "Vrinda Bhardwaj (UG'22)", "Niyati Pendekanti (UG'23)"), 
    ("Vamika Dadoo (UG'24)", "Pankhudi Narayan (UG'23)", "Nipun Jain (UG'23)"), 
    ("Manasi Narula (UG 23)", "Bhavye Jain (UG'23)", "ONE_NON_CONFLICTING_NON_CIS_MEMBER")
)

entire_panel = "Neha Sheik (UG'23),RochaN Mohapatra (UG'23),Nipun Jain (UG'23),Bhavye Jain (UG'23),Manasi Narula (UG 23),Yasashvi Parakh (UG'23),Miloni Shah (UG'23),Niyati Pendekanti (UG'23),Vrinda Bhardwaj (UG'22),Vamika Dadoo (UG'24),Pankhudi Narayan (UG'23),Rajvee Parikh (UG'23),Arjun Khanna (UG'23),Harsh Gupta (UG '23)"
entire_panel = entire_panel.split(",")
print(entire_panel)


original_stdout = sys.stdout

cnt = Counter(panelist_groups)
cnt["(NO MATCH)"] = 0
people = pd.read_csv('responses.csv')

with open('output.txt', 'w') as f:
    sys.stdout = f
    print("People and corresponding panelists - ")
    print("")
    sys.stdout = original_stdout

for person in people.index:
    current_CoI = []

    for panelist in entire_panel:
        if (people[panelist][person] != "No"):
            current_CoI.append(panelist)
    
    # current_CoI = people['conflict_of_interest'][person]
    # current_CoI = current_CoI.split(",")
    interviewer_possibilities = []
    
    for panelist_group in panelist_groups:
        flag = True
        for interviewer in panelist_group:
            if (interviewer in current_CoI):
                flag = False
                break
        if (flag):
            interviewer_possibilities.append(panelist_group)

    print(interviewer_possibilities)

    if (len(interviewer_possibilities) != 0):
        rnd = random.choice(interviewer_possibilities)
        cnt[rnd] += 1
    else:
        rnd = "(NO MATCH)"
        cnt[rnd] += 1

    with open('output.txt', 'a') as f:
        sys.stdout = f
        print(people['Name (As per Official records)'][person], "-", rnd)
        sys.stdout = original_stdout

with open('output.txt', 'a') as f:
    sys.stdout = f
    print("")
    for x in cnt:
        print(x, cnt[x])