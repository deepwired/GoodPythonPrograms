__author__ = 'deepsinghbaweja'

from datetime import datetime

n=6
m=1
colnames=["ID","Name","Date","Score"]
rows=[
    [1,"Aditya Moody","2014-10-23 11:55",20],
    [2,"Utsav Moody","2014-10-24 15:18",21],
    [3,"Jon Doe","2014-10-23 02:51",62],
    [4,"Foo Bar","2014-10-23 12:00",98],
    [5,"Rahul Moody","2014-10-23 12:31",61],
    [6,"Umang JarJar","2014-10-23 11:21",33],
]
query="Date < '2013-10-23 12:00'"

#get the field,operator
text=''
for i in query:
    if i not in ('>','<','='):
        text=text+i
    else:
        queryField = text[:len(text)-1]
        queryOperator = query[len(text):len(text)+2].strip(" ")
        queryValue = query[len(text)+2:].strip("'")

#print queryField;
#print queryOperator
#print queryValue

#get index of field
index=colnames.index(queryField)

#iterate through all those fields only
count=0;
if queryField == 'Date':
    compareDate = datetime.strptime(queryValue,'%Y-%m-%d %H:%M')
for i in rows:
    tempdate = datetime.strptime(i[index],'%Y-%m-%d %H:%M')
    if queryOperator == '>':
        if tempdate > compareDate:
            count=count+1;
    elif queryOperator == '<':
        if tempdate < compareDate:
            count=count+1;
    elif queryOperator == '>=':
        if tempdate >= compareDate:
            count=count+1;
    elif queryOperator == '<=':
        if tempdate <= compareDate:
            count=count+1;

print count


for i in range(0,n):
    current=rows[i]

