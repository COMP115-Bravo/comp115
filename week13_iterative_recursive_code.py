def sum_list_iteration(nums):
    total = 0
    for num in nums:
        total += num
    return total

#print(sum_list_iteration([2, 4, 5]))


def sum_list_recursion(nums):
    if len(nums) == 0:
        return 0
    # if len(nums) == 1:
    #     return nums[0]
    return nums[0] + sum_list_recursion(nums[1:])

#print(sum_list_recursion([2, 4, 5]))



def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac



def factorial_r(n):
    if n <= 1:
        return 1
    return n * factorial_r(n - 1)

#print(factorial_r(4))

# Remember how to implement the algorithm 
# of printing the nth Fibonacci number (n starts from 0)?
# 0, 1, 1, 2, 3, 5, 8, ...

def fibonacci(n):
    if n <= 1:
        return n
    pre = 0
    cur = 1
    for i in range(2, n + 1):
        (cur, pre) = (cur + pre, cur)
    return cur

def fibonacci_r(n):
    if n <= 1:
         return n
    return fibonacci_r(n - 1) + fibonacci(n - 2)

#print(fibonacci_r(4))

# Beautiful! For many questions, 
# it seems recursive algorithm is easier and more elegant.
# However, the elegance is usually traded off for cost of time and memory.
# We can compare how much time used by iterative and recursive algorithms as below.


import time
t1 = time.time()
print(fibonacci(100))
t2 = time.time()
print(f"Iteration costs {t2 - t1}s.")


t3 = time.time()
print(fibonacci_r(100))
t4 = time.time()
print(f"Recursion costs {t4 - t3}s.")
