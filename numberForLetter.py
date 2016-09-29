__author__ = 'deepsinghbaweja'

#number for letters using dicts
import string

all= list(string.ascii_uppercase)
dict={}
dict['A']=1
dict['B']=dict['A']*2+2
for i in range(2,len(all)):
    dict[all[i]]=dict[all[i-1]]*2+(i+1)
#dict generated

string="GREP"

string=list(string)
total=0
for i in string:
    total=total+dict[i]
print total
#answer released






