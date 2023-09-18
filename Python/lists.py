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