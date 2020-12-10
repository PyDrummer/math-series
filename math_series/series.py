num = 9

def fibonacci(n):
    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(num))

# source cited: https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/

# recursive function 
def lucas(n): 
    # Base cases  
    if (n == 0): 
        return 2
    if (n == 1): 
        return 1
  
    # recurrence relation  
    return lucas(n-1) + lucas(n-2)  

# print(lucas(num)) 

#cited source: https://www.geeksforgeeks.org/lucas-numbers/

def sum_series(i, x=0, y=1):
    # print(x)
    # print(y)
    if (x == 0 and y == 1):
      if i - 1 == 0:
        return x
      if i - 1 == 1:
        return y
      return sum_series(i - 1, x, y) + sum_series(i - 2, x, y)
    else:
      if i == 0:
        return x
      if i == 1:
        return y
      return sum_series(i - 1, x, y) + sum_series(i - 2, x, y)

# print(sum_series(9, 2, 1))
# print(f"sum_series = {sum_series(num, 2, 1)}")