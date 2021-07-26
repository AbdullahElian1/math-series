
def fibonacci_series(n):
    if n<0:
       return "enter positive number"
    elif n==0:
        return 0
    elif n==1:
       return 1
    else:
        return(fibonacci_series(n-1)+ fibonacci_series(n-2))

   
# print(fibonacci_series(7))





def lucas_numbers(n):
#    print("x")
   if n<0:
       return "enter positive number"
   elif n==0:
        return 2
   elif n==1:
       return 1
   else:
        return(lucas_numbers(n-1)+ lucas_numbers(n-2))

# print(lucas_numbers(8))
    





