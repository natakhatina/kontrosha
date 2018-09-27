def foofoo3_b(a,b):
    def foo3_a(a, b):
        if a > b:
            return True
        elif a==b:
            global flag
            flag=True
            return 7
        else:
            return False
    if foo3_a(a,b)==True:
        return a
    else:
        return b

flag=False

x=3
y=3
a=foofoo3_b(x,y)
if a==x and flag==False:
    print(a,'>',y)
elif flag==True:
    print (x,'=',y)
else:
    print(a,'>',x)

print(flag)