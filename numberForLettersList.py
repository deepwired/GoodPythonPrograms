__author__ = 'deepsinghbaweja'

import string
chars= list(string.ascii_uppercase)
values=[1]

#dict['A']*2+2

for i in range(1,len(chars)):
    values.append(values[i-1]*2+i+1)

print chars
print values

string="GREP"

total=0
for i in range(0,len(chars)):
    if chars[i] in string:
        total=values[i]+total

length=len(values)
print total


def recursiveFunction(total,text):
    for i in range(0,len(values)):
        if values[i] < total:
            pass
        elif values[i]==total:
            text = text+chars[i]
            return text;
        elif values[i] > total:
            text = text + chars[i-1]
            total = total - values[i-1]
            return recursiveFunction(total,text)
    return text;

print recursiveFunction(total,"")