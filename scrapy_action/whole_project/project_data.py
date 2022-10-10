from datetime import datetime
from collections import namedtuple
import sqlite3
import glob
import json

user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    }
CurrentDate = datetime.now()
HostInfo = namedtuple(field_names='cert hostname peername', typename='HostInfo')
urls=[]
conn=sqlite3.connect("heikotest.db")
c=conn.cursor()
date_id=1
# In[5]:
domainNames=[]

#this file contains ghostery server domain and i'm using this domain names including here to check if they exist in the domains that needs to be scrapped
#this is not a very good approach, if you have another way to get all the trackers of a domain please do
Myfiles = [i for i in glob.glob('/Users/edgarohanyan/Desktop/Shant/domains/domains/*.json')]
for each_file in Myfiles:
    with open(each_file,'r') as f:
        r4 = json.load(f)
        if (r4["owner"] and r4["owner"]["displayName"]):
            domainNames.append(r4["owner"]["displayName"])