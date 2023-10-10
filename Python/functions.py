# function for a geometic mean
# function define
def geomen (x , y):
    mean = (x*y)/(x+y)
    print(mean)

# function for a greater number 
def greater (m ,n ):
    if ( m >n ):
       print("First number is greater than second and their geomean is :")
    else:
        print("Second number is greater than first so their geomean is :")

# for no body 
def lesser ( a , b):
    pass            

a = 1
b = 2
greater(a , b) # function call 
geomen(a,b)


# for a default value of function 
def average (a=6 , b=2):
    print("The average is : ", (a+b)/2)

average()
# for keyword argument 
average(b =9)


def average2(*num): # here num is a tuple
    sum =0
    for i in num:
        sum =sum +i
    print("Average is : ", sum/len(num))

average2(6,9)

# for a dictionary 
def name(**name):
    print("Hello,", name["fname"],name["mname"],name["lname"])

name(mname= "B", lname="C", fname="A")

# using return statement 
def add(*numb):
    sum = 0
    for i in numb:
        sum +=i
    return sum

z = add(1,2,3)
print(z)

#emulate functions
marks= [12, 45, 24, 52,73,63]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index ==3):
#         print("Awesome!")
#     index +=1

for index,mark in enumerate(marks, start=1):
    print(mark)
    if(index ==3):
        print("Awesome!")