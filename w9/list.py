s = 'n a w a r a t'
ss = 'konchai'
ss1 = 'JO'
ss2 = '1jo4'
ss3 = 100
ss4 = True


##print (len(s))
##print (s + ss)


sn = s.split()
print (sn)
print (s.count('a'))
for i in range(s.count('a')):
    print (sn)
    print(sn.index('a'))
    sn.remove(sn[1+i])
