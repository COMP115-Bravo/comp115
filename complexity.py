"""
When comparing the efficiency of an algorithm, we often discuss its
time complexity and space complexity.

Time complexity is a function that describes 
how long an algorithm takes in terms of the quantity of input.

Space complexity is a function that describes 
how much memory (space) an algorithm requires to the quantity of input.

Big O, also known as Big O notation, represents an algorithm's worst-case complexity.
Big O and worst-case analysis are tools that greatly simplify our ability to compare 
the efficiency of algorithms. 
This is why we mostly use Big O notation during the algorithm analysis.
"""
"""
Assuming the quantity of input is n,
Common time complexities: O(1), O(log n), O(n), O(n^2), O(2^n), etc.
Common space complexities: O(1), O(log n), O(n), O(n^2), etc.
"""

#### Time complexity ####
# Constant Time O(1): means the running time does not depend on the input size.


def first_item(nums):  # Assume nums is not empty
    print(nums[0])


# Logarithmic time O(logn): binary search (below)


# Linear Time O(n):
# the running time grows at a linear function of n (proportional to n),
# where n is the size of input nums
def all_items(nums):
    for num in nums:
        print(num)


# Quadratic Time O(n^2):
# the running time grows at a quadratic function of n, where n is the size of input nums
def all_item_pairs(nums):
    for number in nums:
        for num in nums:
            print(number, num)


# Exponential Time O(2^n): recursive fibonacci algorithm (below)

#### Space complexity ####


# Constant Space O(1)
def sum(a, b):  # Assume nums is not empty
    result = a + b
    return result


# Logarithmic Space O(logn): binary search (below)


# Linear Space O(n)
def create_list(n):  # Or create a set, dictionary
    a_list = []
    for i in range(n):
        a_list.append(i)
    return a_list


#print(create_list(4))


# Quadratic Space O(n^2):
def create_matrix(n):
    a_matrix = []
    for i in range(n):
        a_matrix.append([])
        for j in range(n):
            a_matrix[i].append(j)
    return a_matrix


#print(create_matrix(3))
"""
Now let's analyze some classical algorithms together!
Recursive functions use the call stack, which occupies space.
"""


### Factorial recursive and iterative implementations
def factorial(n):  # Time: O(n), Space: O(1)
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def factorial_r(n):  # Time: O(n), Space: O(n)
    if n == 0 or n == 1:
        return 1
    return n * factorial_r(n - 1)


### Finonacci recursive and iterative implementations


def fibonacci(n):  # Time: O(n), Space: O(1)
    if n <= 1:
        return n
    pre = 0
    cur = 1
    for _ in range(2, n + 1):  #for _ in range(n - 1):
        print(cur)
        tmp = cur
        cur += pre
        pre = tmp
    return cur


def fibonacci_r(n):  # Time: O(2^n), Space: O(n)
    if n == 0 or n == 1:
        return n
    return fibonacci_r(n - 1) + fibonacci_r(n - 2)


### Search algorithms
def linear_search(nums, target):  # Time: O(n) Space: O(1)
    nums_length = len(nums)
    for i in range(nums_length):
        if nums[i] == target:
            return i
    return -1


# Teacher, why not use set? If target in nums, return True.
# Yes, but how can we return its index? So set is not appropriate here.

# Teacher, why not use dict? Good good! Use num as the key, and its index as its value.


def search_dict(nums, target):  # T: O(n), S: O(n)
    nums_length = len(nums)
    dict = {}
    for i in range(nums_length):
        dict[nums[i]] = i
    if target in dict:
        return dict[target]
    else:
        return -1


# Binary Search algorithm
def binary_search(nums, target):  # Time: O(logn)  Space: O(1)
    first = 0  # First index
    last = len(nums) - 1  # Last index
    while first <= last:
        mid = (first + last) // 2
        print(first, last, mid)
        if target < nums[mid]:
            last = mid - 1
        elif target > nums[mid]:
            first = mid + 1
        else:
            return mid
    return -1


#binary_search([1, 2, 4, 7, 8, 9], 6)
#0, 5, 2    (3, 5, 4)    (3, 3, 3)


def binary_search_recursive(nums, first, last,
                            target):  # Time: O(logn)  Space: O(logn)
    if first > last:
        return -1
    mid = (first + last) // 2
    if target < nums[mid]:
        return binary_search_recursive(nums, first, mid - 1, target)
    elif target > nums[mid]:
        return binary_search_recursive(nums, mid + 1, last, target)
    else:
        return mid


def binary_search_r(nums, target):
    return binary_search_recursive(nums, 0, len(nums) - 1, target)


#print(binary_search_r([1, 2, 4, 7, 8, 9], 10))
