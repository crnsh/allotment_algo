# Input - responses.csv, panelists
# Output - 3 panelists, output which 2 non-cis-men"
"""
We need a program which can allot Panels for the CL interviews. The process is as follows:

Each applicant is given a form where they have to mark the Panellists they have a CoI with. 
The program should select a Panel of 3 pple where there should be atleast 2 Non-Cis Men. 
Things to take into account but not a hard rule -
    Balance the panel with at least 2 Non-Cis Men and one Cis Man. 
    Balance the interviews in such a way that Non-Cis Men are not overburdened with interviews(like last time, sending a vn)
"""
"""
Process -
    1.  For each 3-tuple of panelists in which non-cis are 2, check whether all people can be interviewed.
"""

import pandas as pd
import sys
import random

original_stdout = sys.stdout

panelists = pd.read_csv('panelists.csv')
people = pd.read_csv('responses.csv')

with open('output.txt', 'w') as f:
    sys.stdout = f
    print("People and corresponding panelists - ")
    print("")
    sys.stdout = original_stdout

for person in people.index:
    current_CoI = people['conflict_of_interest'][person]
    current_CoI = current_CoI.split(",")
    interviewer_possibilities = []
    
    for panelist in panelists.index:
        if (panelists['names'][panelist] not in current_CoI):
            interviewer_possibilities.append([panelists['names'][panelist], panelists['gender'][panelist]])

    non_cis = []
    cis = []

    for x in interviewer_possibilities:
        if x[1] == 'non-cis':
            non_cis.append(x[0])
        else:
            cis.append(x[0])
    
    cis_1 = random.choice(cis)
    non_cis_1 = random.choice(non_cis)
    non_cis.remove(non_cis_1)
    non_cis_2 = random.choice(non_cis)
    with open('output.txt', 'a') as f:
        sys.stdout = f
        print(people['names'][person], "-", cis_1, non_cis_1, non_cis_2)
        sys.stdout = original_stdout


# for n1 in panelists.index:
#     for n2 in panelists.index:
#         for n3 in panelists.index:
#             # names = panelists['names'][i]
#             # gender = panelists['gender'][i]
#             if (n1 != n2 != n3 != n1):     

#                 # Checking if non-cis-men is 2
#                 non_cis_cnt = 0

#                 if (panelists['gender'][n1] == 'non-cis'):
#                     non_cis_cnt+=1
#                 if (panelists['gender'][n2] == 'non-cis'):
#                     non_cis_cnt+=1
#                 if (panelists['gender'][n3] == 'non-cis'):
#                     non_cis_cnt+=1

#                 if (non_cis_cnt == 2):

#                     panelist_1_list = []
#                     panelist_2_list = []
#                     panelist_3_list = []

#                     cnt = 0

#                     for i in people.index:
                        
#                         panelist_1_possible = True
#                         panelist_2_possible = True
#                         panelist_3_possible = True

#                         current_interviewee = people['names'][i]
#                         panelist_1_name = panelists['names'][n1]
#                         panelist_2_name = panelists['names'][n2]
#                         panelist_3_name = panelists['names'][n3]

#                         current_CoI = people['conflict_of_interest'][i]
#                         current_CoI = current_CoI.split(",")

#                         # Checking if for current person, which panelist can interview
#                         for person in current_CoI:
#                             if (person == panelist_1_name):
#                                 panelist_1_possible = False
#                             if (person == panelist_2_name):
#                                 panelist_2_possible = False 
#                             if (person == panelist_3_name):
#                                 panelist_3_possible = False
                        
#                         if (panelist_1_possible or panelist_2_possible or panelist_3_possible):
#                             cnt+=1
                        
#                         if (panelist_1_possible):
#                             panelist_1_list.append(current_interviewee)
#                         if (panelist_2_possible):
#                             panelist_2_list.append(current_interviewee)
#                         if (panelist_3_possible):
#                             panelist_3_list.append(current_interviewee)

#                     if (cnt == len(people.index) and len(panelist_2_list) > threshold and len(panelist_2_list) > threshold and len(panelist_3_list) > threshold):
                        
#                         cnt = 0
#                         for x in panelist_1_list:
#                             if (cnt >= threshold):
#                                 break
#                             if (x in panelist_2_list or x in panelist_3_list):
#                                 if (x in panelist_2_list):
#                                     panelist_2_list.remove(x)
#                                 if (x in panelist_3_list):
#                                     panelist_3_list.remove(x)
#                                 cnt += 1
                                
#                         cnt = 0
#                         for x in panelist_2_list:
#                             if (cnt >= threshold):
#                                 break
#                             if (x in panelist_1_list or x in panelist_3_list):
#                                 if (x in panelist_1_list):
#                                     panelist_1_list.remove(x)
#                                 if (x in panelist_3_list):
#                                     panelist_3_list.remove(x)
#                                 cnt += 1
                        
#                         cnt = 0
#                         for x in panelist_3_list:
#                             if (cnt >= threshold):
#                                 break
#                             if (x in panelist_1_list or x in panelist_2_list):
#                                 if (x in panelist_1_list):
#                                     panelist_1_list.remove(x)
#                                 if (x in panelist_2_list):
#                                     panelist_2_list.remove(x)
#                                 cnt += 1
                        
#                         total = panelist_1_list.copy()
#                         total.extend(panelist_2_list)
#                         total.extend(panelist_3_list)

#                         if (len(panelist_1_list) + len(panelist_2_list) + len(panelist_3_list) == len(people.index) and len(set(total)) == len(total)):
                            
#                             with open('output.txt', 'a') as f:
#                                 sys.stdout = f
#                                 print("Panelist 1 -", panelists['names'][n1])
#                                 print("Possible interviewees -", panelist_1_list)
#                                 print("")
#                                 print("Panelist 2 -", panelists['names'][n2])      
#                                 print("Possible interviewees -", panelist_2_list)  
#                                 print("")
#                                 print("Panelist 3 -", panelists['names'][n3])      
#                                 print("Possible interviewees -", panelist_3_list)  
#                                 print("")
#                                 print("")

#                                 sys.stdout = original_stdout 

