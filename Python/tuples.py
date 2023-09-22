# tuples in python cannot be changed 
tup =(1,2,"red",True)
print(type(tup),tup)
# indexing 
print(tup[0])
# negative indexing
print(tup[-1])
# conditiions
if 2 in tup:
    print("yes")

tup2 = tup[1:3]
print(tup2)

## operation in tuples

num=(0,1,2,3,1,2,3,1,1)
print(num.count(1))
print(num.index(2,0,5))
print(len(num))