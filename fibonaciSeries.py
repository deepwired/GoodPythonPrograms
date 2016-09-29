__author__ = 'deepsinghbaweja'


nterms=10

n1 = 0
n2 = 1
count = 2
print n1
print n2
while count < nterms:
   nth = n1 + n2
   print nth
   # update values
   n1 = n2
   n2 = nth
   count += 1