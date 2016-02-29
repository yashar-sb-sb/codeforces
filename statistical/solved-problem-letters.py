#this file is edited

import urllib.request
import json

def get(handle):
'''
fetches data from codeforces api and stores it into data/handles/handle/
'''
  sj = json.loads(urllib.request.urlopen('http://codeforces.com/api/user.status?handle=yashar_sb_sb&from=1').read().decode('utf-8'))
  cj = json.loads(urllib.request.urlopen('http://codeforces.com/api/contest.list').read().decode('utf-8'))
  
  f = open('data/handles/'+handle+'/result','w')
