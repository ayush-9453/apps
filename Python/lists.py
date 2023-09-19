# fruits is a list 
fruits =['oranges', 'apple','bananas','kiwi','apple']

# This count the number of occurce of a string or a value in a list
print(fruits.count('apple'))

#This tells the index of the value in a string
print(fruits.index('bananas'))
#Now this finds the value starting at 2
print(fruits.index('apple',2))

#to reverse a list
print(fruits.reverse())

# to append a value in a list
print(fruits.append('kiwi'))

#t0 sort a list 
print(fruits.sort())


## now stack operations

# stack = [3,4,5]
# # to push a value
# stack.append(6)
# stack.append(7)

# # to pop a value
# stack.pop(7)


# for a list of square numbers
squares =[]
for x in range(10):
    squares.append(x**2)

print(squares)

combs =[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))

print(combs)

# # for transpose in matrix
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# transposed=[]
# for i in range(4):
#     transposed_row =[]
#     for row in matrix:
#        transposed_row.append(row[i])
#     transposed.append(transposed_row)

# print(transposed)

# for a delete operations
a = [1 ,-1,3 ,35, 34 ,36,353]
del a[0]
print(a)
del a[2:4] # for in range del opertaions
print(a)
del a[:]
print(a) # to empty the list