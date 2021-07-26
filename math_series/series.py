
def fibonacci_series(n):
    """
    this function will take number and do fibonacci series on it

    Arg[number]
    output => summation based on fibonacci series
    """
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
    





def sum_series(n,first=0,second=1):
#    print(first)
   if n<0:
       return "enter positive number"
   elif n==0:
        return first
   elif n==1:
       return second
   else:
        return(sum_series(n-1,first,second)+sum_series(n-2,first,second))
    

print(sum_series(7,0,1))
    
