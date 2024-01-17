"""
Lab 2 - Fundamentals of Python: variables, expressions, statements and function
(100 marks in total, including
5 exercises (80 marks) + submission (20 marks))

Your Name 😍:
Lab Due: 11:00am on Jan. 19

Objective:
1. Practice how to use variables, expressions and statements in Python
2. Practice how to debug errors in a program
3. Practice working with different data types: int, float, str, list
4. Learn the concept of a function
"""

#---------------------------------------------------------
# Exercise 1 (10 marks) - Add parenthesis to the following expression 
# num * 10 - 3 to change new_num's value from 47 to 35.
#---------------------------------------------------------
num = 5
new_num = num * 10 - 3 # Add parenthesis to make new_num to be 35
print(f"Exercise 1's new_num is: {new_num}")


#---------------------------------------------------------
# Exercise 2 (10 marks) - Modify the operators in quotient and remainder
# to make them get the correct results as hinted.
#---------------------------------------------------------
dividend = 10
divisor = 3
decimal_quotient = dividend / divisor 
quotient = dividend / divisor # The quotient should be 3
remainder = dividend / divisor # The remainder should be 1
print(f"Exercise 2's quotient is: {quotient}, remainder is: {remainder}.")


#---------------------------------------------------------
# Exercise 3 (10 marks) - Modify the expressions on the right side of 
# the perimeter statement and area statement
# to make them get the correct results as hinted.
#---------------------------------------------------------
rectangular_width = 5
rectangular_length = 3
perimeter = rectangular_width + rectangular_length # Modify it to calculate perimeter
area = rectangular_width + rectangular_length # Modify to calculate area
print(f"Exercise 3's rectangular has perimeter of: {perimeter}, area of: {area}.")


#---------------------------------------------------------
# Exercise 4 (10 marks) - Modify the expression of mark_mid + mark_final
# to make it calculate the correct average mark.
#---------------------------------------------------------
marks = [80.5, 86.5]
mark_mid = marks[0]
mark_final = marks[1]
mark_average = mark_mid + mark_final # Modify to get the correct average score of mark_mid and mark_final
print(f"Exercise 4's average mark is: {mark_average}")


#---------------------------------------------------------
# Exercise 5 (10 marks) - Modify the expression of len(words[0]) > len(words[1])
# to make longer_word get assigned with the word that has more characters.
#---------------------------------------------------------
words = ["apple", "pear"]
if len(words[0]) > len(words[1]): 
    longer_word = words[1]
else:
    longer_word = words[0]

print(f"Exercise 5's longer word is: {longer_word}")


#---------------------------------------------------------
# Exercise 6 (10 marks) - Modify the expression of increase / 100
# to convert the value of increase to its percentage correctly.
#---------------------------------------------------------
increase = 0.2
increase_percentage = increase / 100
print(f"Exercise 6's increase percentage is: {increase_percentage}%")



#---------------------------------------------------------
# Exercise 7 (20 marks) - The following program prints out
# the first 5 even natural numbers.
# Modify the expression of count < 5
# to make the following program print the first 8 even natural numbers:
# 2, 4, 6, 8, 10, 12, 14, 16
#---------------------------------------------------------

x = 2
count = 0
while count < 5: 
    print(x)
    x = x + 2
    count = count + 1

#---------------------------------------------------------
# Exercise 8 (Optional challenge) 
# Can you convert the exercise 7's code to a function named 
# first_natural_even_nums(total), where total is an input parameter.
# When you call your funtion, e.g., first_even_natural_nums(2) will print the 
# first 2 natural even numbers. first_even_natural_nums(50) will print the 
# first 50 natural even numbers.
#---------------------------------------------------------
def first_even_natural_nums(total):
    pass # Write your code here



#---------------------------------------------------------
# Submission (20 marks):
# After you finish this lab, please:
# 1. rename the lab file as lab2_{your_first_name}.py.
# 2. upload your lab2 python file to your GitHub "comp115" repository.
# 3. follow this link "https://comp115-bravo.github.io/" and fill the blanks there.
# Great job. Congratulations on finishing your lab2!
#---------------------------------------------------------
