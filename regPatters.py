__author__ = 'deepsinghbaweja'

#interpret regex from defined symbols
string = "aaaaaannndnnnnnnfffhfhhgjjjwkkkllclc"
dict = {'.': 2, '*': 5, '+': 4}

def iterateString(line):
    text=""
    for i in line:
        if i in dict.keys():
            text=text+prevchar*(dict[i]-1)
        else :
            text=text+i
        prevchar=i
    count=0
    for i in range(0,len(string)):
        if string[i:i+len(text)]==text:
            count=count+1
    return count

print iterateString("a.a.")
print iterateString("n+")
print iterateString("a*")
print iterateString("an.")
print iterateString("a.d.")