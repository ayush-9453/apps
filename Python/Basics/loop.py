# for loop in python
name = 'Tatya'
for i in name:
  print(i ,end=",")

color =['red','yellow','green']
for x in color:
   for i in x :
      print(" char:", i)
   if(x=='red'):
      print('This is "red" color')
   elif(x=='yellow'):
      print('This is "yellow" color')
   elif(x == 'green'):
       print('This is "green" color')
# In this range starts from 0 to 20 because a is not initialize 
for a in range(20):
   print(a)
# In this range from 1 to 6
for v in range(1,6):
   print(v)
# In this 1st and 2nd signify range and 3rd increment
for b in range(1,12,2):
   print(b)

# while loops in python
i =int(input("Enter the number: "))
while(i<3):
   i =int(input("Enter the number: "))
   print(i)
   i+=1
# while loops with else statments
count =5 
while(count > 0):
    print(count)
    count-=1
else : 
    print("i am inside else")

# for loops with break statment 
# where the break statement simply break the loop and come out of the command
for i in range(12):
    if(i==10):
      break
    print("5 X", i+1,"=",5*(i+1))
 
print("break statement is executed")

# for loops with continue statement 
# where the conitinue statement skips the current iteration to the next one
for i in range(12):
    if(i==10):
      print("continue statement is executed & the iteration is skipped")
      continue
    print("5 X", i+1,"=",5*(i+1))
    
    