__author__ = 'deepsinghbaweja'

#compare elemts ofjson which are diff

a = "{'Geeks':'Test1','Are':'hey','Cool':'yeah'}"
b = "{'Geeks':'Test1','Are':'20','Cool':'yeah'}"


a = a.strip('{').strip('}').strip('"').split(",")
b = b.strip('{').strip('}').strip('"').split(",")

ans=""
for i in range(0,len(a)):
    if a[i]!=b[i]:
        temp=a[i].split(":")[0]
        for i in temp:
            ans=ans+i

print ans.strip("'").replace("''",':')
