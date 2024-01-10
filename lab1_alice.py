"""
Lab 1 - First Impression of Python
(100 marks in total, including
3 exercises + submission (10 marks))

Your Name 😍:
Lab Due: 11:00am on Jan. 12

Objective:
0. Create a GitHub account and a repository named comp115 
(you can follow this guide: https://github.com/COMP115-Bravo/comp115/blob/main/Create%20a%20GitHub%20account%20and%20repository.pdf).
1. Practice how to run Python code in VScode or your IDE
2. Understand what is a comment, and what is a docstring in Python 
(this part is a docstring, which is a type of comments, providing info about modules, functions, classes, or methods)
3. Understand the concept of syntax error, semantic error, and runtime error
4. Understand how to use print() function in Python
5. Understand how to use a variable in Python
5. Understand how to use f-string in Python to involve variables in strings
"""

#---------------------------------------------------------
# Exercise 1 - Read the following code, try to guess the output, and run it to verify your guess.

# This exercise was inspired by one of our amazing friends in the class, who asked me how to use variables in programming.
#---------------------------------------------------------

x = 0
while x < 10:
    x = x + 2
    print(x)

#---------------------------------------------------------
# Exercise 2 (40 marks) - Fix the semantic error below, to make it calculate the area of the rectangle correctly.
 
# A regular comment usually starts with a #. 
# Regular comments are used to explain parts of the code for developers reading it.
# So this part is a comment. # is only able to comment one line at a time.
# If you want to comment multiple lines, 
# you can use command + / (Mac) or ctl + / (Windows). 
# Or you can use ''' ''' or """ """ to create a multiline string or a docstring. 
#---------------------------------------------------------

print("There is a rectangle, of which one side is 3 and the other side is 4.") # This line prints a string.
side_1 = 3
side_2 = 4
print(f"I think the area of the rectangle is: {side_1 + side_2}.") # This line prints a f-string, including variables in a string.


#---------------------------------------------------------
# Exercise 3 (50 marks) - Write a letter to your instructor
#---------------------------------------------------------

my_instructor_name = "COMP115 class 😄" # Change to "Alice 😄"
my_name = "Alice" # Change to your name
my_github_account = "https://github.com/COMP115-Bravo" # Change to your GitHub account
my_hobby = "hockey" # Change to your hobby
hours_coding_per_week = "5" # How many hours per week would you like to devote to learn coding?

coding_experience_types = ["newbie", "beginner", "intermediate", "advanced"]
my_coding_experience = coding_experience_types[3] 

project_types = ["game developing", "website application", "data analysis", "machine learning"]
project_interested = project_types[2]
project_another_interested = project_types[3] # Try to change the index from 3 to 4, and run the program :)


print(f"""
Hi {my_instructor_name},

I am {my_name}. I like {my_hobby}.

My experience level in coding is {my_coding_experience}, at least I think.
I would love to learning coding {hours_coding_per_week} hours per week.
The projects I'd like to do in this term are: {project_interested} and {project_another_interested}.
Here is my GitHub account: {my_github_account}.

Hope we will have fun in learning Python together this term! 

Cheers,
{my_name}
""")

#---------------------------------------------------------
# Submission (10 marks):
# After you finish this lab, please:
# 1. rename the lab file as lab1_{your_first_name}.py, e.g., lab1_alice.py would be my lab1 file name.
# 2. upload your lab1 python file to your GitHub "comp115" repository.
# 3. follow this link "https://comp115-bravo.github.io/" and fill the blanks there.
# Great job. Congratulations on finishing your lab1!
#---------------------------------------------------------
