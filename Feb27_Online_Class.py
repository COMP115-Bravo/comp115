## Feb. 27 (Tuesday)'s online class 

## Midterm coding question 1 sample solution
# def foo(current_month, months_to_completion):
#     completion_month = (current_month + months_to_completion) % 12
#     if completion_month == 0:
#         completion_month = 12
#     return completion_month

# Unit tests
# assert foo(10, 4) == 2    
# assert foo(1, 12) == 1
# assert foo(6, 18) == 12



## Strings
# empty_s = '' # ""
# print(len(empty_s))
# empty_s = empty_s + 'Hi'
# print(empty_s)
# print(("You" + " rock! ") * 3)

# ss = "python rocks"
# print(len(ss)) # 12
# print(ss[4] + ss[-5]) # string index 'or'
# print(ss[7:11]) # A substring of a string is called a slice
# ss[0] = 'P' # Error! Strings in Python are immutable, while lists are mutable
# print('A' not in "Apple")
#print('apple' > 'B')
#print('apple' == 'Apple')
#print('apple' > 'Apple')
# print(ord("B")) # Ordinal value
# print(ord("@")) # https://www.asciitable.com/


## Strings are also objects. They have methods as:
# s = ' Hi world'
# print(s.upper())
# print(s.lower())
# print(s.count('i'))
# print(s.find('w'))
# print(f"***{s.rstrip()}***")
# print(f"***{s}***")



## f-string VS format
# origPrice = 100
# discount = 60
# newPrice = (1 - discount/100)*origPrice
# calculation = '{} discounted by {}% is {:.2f}.'.format(origPrice, discount, newPrice)
# print(calculation)
# print(f'{origPrice} discounted by {discount}% is {newPrice:.2f}.')



## for loops:
# for i in range(3):
#     print(i)

# for c in "Hi 115":
#     print(c)

# for c in ["Hi", "115"]:
#     print(c)

# sentence = "Hi 115"
# for i in range(len(sentence)): # 0 - 5
#     if i % 2 == 1:
#         print(sentence[i])

# for _ in "Hi 115":
#     print("Good evening!")

# for _ in ["Hi", "115"]:
#     print("Good night!")


## Tuples are very similar to lists, except immutable and ()

# t = (1, 'like', True)
# print(t)
# print(t[1])

# ## Swap
# a = 1
# b = 2
# # tmp = a
# # a = b
# # b = tmp
# # print(a, b)
# (a, b) = (b, a) # excellent tuple assignment: all the expressions get evaluated before any assignment
# print(a, b)
