x = []
b = 5
z = []

for i in range (b) :
    a = int(input())
    x.append(a)
    x.sort() ##x.sort()
    z=sorted(x, reverse = True)
    
print(x)    
##print( sorted(x, reverse = True) ) ##prit + sorted()

print(z)
print (type(x))
