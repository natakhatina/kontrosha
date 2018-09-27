def foofoo(a,b):
    def foo(a, b):
        if a > b:
            return 1
        else:
            return 0
    if foo(a,b)==1:
        return a
    else:
        return b
x=3
y=2
a=foofoo(x,y)
if a==x:
    print(a,'>',y)
else:
    print(a,'>',x)
