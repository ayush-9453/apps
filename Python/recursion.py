# when a code is run multiple time without using loops like for statement

# for a factorial recursion 
# def factorial(num):
#     if (num ==1 or num ==0):
#         return 1
#     else:
#         return num*factorial(num-1)
    
# print(factorial(3))

# for fibonnaci series
def fibonnaci(num):
      if num<=0:
            return 0
      elif num==1:
            return 1
      else:
            return fibonnaci(num-1)+fibonnaci(num-2)
            
          
print(fibonnaci(4))