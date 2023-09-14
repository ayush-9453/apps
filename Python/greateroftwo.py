# if 5>2:
#     print("5 is greater than two")
# a =int(input("Enter the number "))
# if (a > 18):
#     print("You can drive")
# elif(a==18):
#     print("you cannot drive")


# exercise

import time
timestamp = time.strftime('%H: %M :%S')
print("Time is : ",timestamp)
hour = int( time.strftime('%H'))
# print(hour)
min = time.strftime('%M')
# print(min)
sec = time.strftime('%S')
# print(sec)
if (hour < 5):
    print("Good night")
elif (hour < 12):
    print("Good morning")
elif(hour >= 12 and hour < 18):
    print("Good afternoon")
elif(hour>18 and hour< 22 ):
    print("Good evening")
else:
    print("Good night")