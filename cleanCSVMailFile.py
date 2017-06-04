# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:45:07 2017

@author: shuchowdhury
"""


import pandas as pd  




email_filename = "emails.csv"
## Set your Project Directory
proj_dir = 'C:/Training/udacity/ProjectEmail/inputs/'
#proj_dir ='/app/hadoop/project/data/enron/'

"""
Total rows 517401
"""

#emails = pd.read_csv(proj_dir+email_filename,skiprows=500900,names ="file")

#emails = pd.read_csv(proj_dir+email_filename,nrows=2,usecols=[0],delimiter=',')

"""
Whole thing can be done in a loop by first finding the length of file and then 
incrementing it by 10,000 each time in that loop . But for simplicity 
I am doing the crude way.

First 10,000 rows with header 
"""
#==============================================================================
# try:
#==============================================================================
#emails = pd.read_csv(proj_dir+email_filename,header=0,delimiter=",",quotechar='"', encoding='utf-8')
#emails = pd.read_csv(proj_dir+email_filename,header=0,delimiter=",",nrows=50000,dtype=(str,50000))
emails = pd.read_csv(proj_dir+email_filename,header=0,delimiter=",",dtype=(str,3000))

#print(len(emails))
#emails.message[1]
#print(emails.message[99])
#emails.message=emails.message.str.replace(r"[\"\'\(--),]", '')
emails.message=emails.message.str.replace("--", '')
emails.message=emails.message.str.replace(r"[\"\',]", '')

emails.to_csv(proj_dir+'emails_clean.csv',  index=False)
#except:
#       print("Error in emails from 1 to 10 K")

