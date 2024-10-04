# set in python removes any repeated data
# it is a well define data set and unordered data
info = {
    "carlos",15, False,3.55
}
print(info)

name = set()
print(type(name))

for value in info:
    print(value)

# set joining
s1 = {1,2,3,5}
s2 = {2,4,7,9}
print(s1.union(s2)) 
s1.update(s2)
print(s1,s2)

# set intersection
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)

# symetric difference
s1.symmetric_difference(s2)
print(s1)

# difference
s1.difference(s2)
print(s1)