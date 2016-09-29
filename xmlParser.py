__author__ = 'deepsinghbaweja'

#interpret tags to perform operations

input ="""<expr>
<sub>
<elem>4</elem>
<elem>6</elem>
<elem>7</elem>
<elem>3</elem>
</sub>
</expr>"""
input=input.split("\n")
num=[]
opDict={
    '<sum>':'+',
    '<prod>':'*',
    '<sub>':'-',
    '<div>':'/'
}
for i in input:
    if i in opDict.keys():
        op=opDict[i]
        first=1;
    elif i[0:6] == "<elem>":
        num.append(i[6]);
if op == '+':
    total=0;
    for i in num:
        total=float(total)+float(i);
if op == '*':
    total=1;
    for i in num:
        total=float(total)*float(i);
elif op == '-':
    total=num[0]
    for i in num[1:len(num)]:
        total=float(total)-float(i);
elif op == '/':
    total=float(num[0])/float(num[1])

print total

