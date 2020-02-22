#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "katran009"


def add(x, y):
    a = x + y
    return a

result = add(2,4)
print(result)

def multiply(x,y): 
  
    # 0 multiplied with anything 
    # gives 0  
    if(y == 0):
        return 0
  
    # Add x one by one  
    if(y > 0 ):
        return (x + multiply(x, y - 1)) 
  
    # The case where y is negative 
    if(y < 0 ):
        return -multiply(x, -y) 
      
# Driver code 
print(multiply(6, -8)) 


def power(a,b): 
    if(b==0): 
        return 1
          
    answer=a 
    increment=a 
      
    for i in range(1,b): 
        for j in range (1,a):
            answer+=increment
        increment=answer
    return answer
  
# driver code 
print(power(2,8))


def factorial(x):
    fac = x
    for i in range(1, x):
        fac *= i
    return fac

print(factorial(4))


FibArray = [0,1] 
  
def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 
  
# Driver Program 
print(fibonacci(8)) 

if __name__ == '__main__':
    # your code to call functions above
    pass
