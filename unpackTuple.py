# tup1 = [1,2,4]
# n1 , n2 , n3 = tup1
# print(n3)

#def fun(**a):
#    print(a)
#    print(type(a))
#
#fun(a=1)

# add = lambda a,b:a+b
# print(add(4,9))

# pa = lambda a : print(a)
# pa(5)

def count_to_n(n):
    for i in range(1,n+1):
        yield i

val = count_to_n(3)
print(next(val))
print(next(val))
