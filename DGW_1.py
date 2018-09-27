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

a=foofoo(3,2)
print(a)
