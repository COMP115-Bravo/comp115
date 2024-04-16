"""
Lab 10 - Exam Preparation Exercises

(100 marks in total, including:
8 code tracing exercises (5 marks each, 40 marks in total);
3 coding quetions (20 marks each, 60 marks in total))

Your Name: Kulwinder kaur
Due date: Apr. 5, 2024, 11am

Objective:
1. Review the function 
2. Review the conditionals (if-else)
3. Review the program flow (for/while - continue, break)
4. Practice when to use and how to operate on the collection data types: 
tuple, list, string, set, dictionary.
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable (accumulator) that is assigned to an integer, a list, etc. 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable.
"""


"""
Exercise 1 - Code tracing (5 marks)

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
practice_if(80, 80)?

Your answer is: Nicely done!

"""


def practice_if(score, average):
    if score < average:
        print("Do better next time!")
    else:
        if score >= 90:
            print("Woot woot!")
        elif score > 80:
            print("Great job!")
        else:
            print("Nicely done!")

practice_if(80,80)
"""
Exercise 2 - Code tracing (5 marks)

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
print(practice_for_if([5, 5, 2, 9], 3))?

Your answer is:[5,5,9] 

"""


def practice_for_if(nums, target):
    list = []
    for num in nums:
        if num > target:
            list.append(num)
    return list

print(practice_for_if([5, 5, 2, 9], 3))

"""
Exercise 3 - Code tracing (5 marks)

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
print(practice_function([5, 5, 2, 9, 6]))?

Your answer is: None

"""


def practice_function(nums):
    even_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)


print(practice_function([5, 5, 2, 9, 6]))
"""
Exercise 4, 5, 6 - Code tracing (15 marks in total)

First read and understand the following function.
Then answer the questions below:

Question 1: What will it print if we call this function by running 
print(practice_for_index_1([5, 5, 2, 9, 9, 6], 9))? (5 marks)
Your answer is:index_1 = 3 
               index_2 = 3
               index_3 = 4


Question 2: Are the function practice_for_index_1(nums, target) and 
the function practice_for_index_2(nums, target) have the same 
functionality? Why? (5 marks)
Your answer is: Yes, practice_for_index_1 and practice_for_index_2 have the same functionality.
                Both functions iterate through the list nums and return the index of the first occurrence of 
                the target value target, or -1 if the target value is not found.


Question 3: Are the function 
practice_for_index_2(nums, target) and the function 
practice_for_index_3(nums, target) have the same 
functionality? Why? (5 marks)
Your answer is: No,because practice_for_index_2 returns the index of the first occurrence of the
                target, while practice_for_index_3 returns the index of the last occurrence of the target.


"""


def practice_for_index_1(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
print(practice_for_index_1([5, 5, 2, 9, 9, 6], 9))

def practice_for_index_2(nums, target):
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
            break
    return index
print(practice_for_index_2([5, 5, 2, 9, 9, 6], 9))

def practice_for_index_3(nums, target):
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
    return index
print(practice_for_index_3([5, 5, 2, 9, 9, 6], 9))

"""
Exercise 7 - Code tracing (5 marks)

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
practice_for_continue([5, 5, 2, 9, 6], 2)?

Your answer is: 
5
5
9
6

"""


def practice_for_continue(nums, target):
    for num in nums:
        if num == target:
            continue
        print(num)
practice_for_continue([5, 5, 2, 9, 6], 2)


"""
Exercise 8 - Code tracing (5 marks)

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
print(practice_while(30))?

Your answer is: 6

"""


def practice_while(n):
    count = 0
    while n > 4:
        n -= 5
        count += 1
    return count
print(practice_while(30))





"""
Exercise 9 - Coding question

Write a function named "exist_in_both" that takes two strings as input 
and returns the number of characters that occur in both strings.
You can assume that all characters within a string are unique (no repeats).

For example, 
if the function is passed "lap" and "help", 
the function exist_in_both("lap","help") will return 2,
because the characters "l" and "p" occur in both strings.

For example,
exist_in_both("computer","mute") wil return 4.

Function implementation. (15 marks) 
Pass your own unit tests. (5 marks) 

"""


def exist_in_both(str1, str2):
    str1_set = set(str1)
    str2_set = set(str2)
    common_chars = str1_set.intersection(str2_set)
    return len(common_chars)


assert exist_in_both("lap", "help") == 2
assert exist_in_both("computer", "mute") == 4
assert exist_in_both("abcdefg", "hijklmn") == 0
assert exist_in_both("testing", "123456") == 0








"""
Exercise 10 - Coding question

If both adjacent letters in a word are the same, 
we call the two adjacent letters are "good neighbors".

E.g.1, there are one pair of good neighbors inside the word "apple",
since word[1] == word[2], and they are both 'p'.

E.g.2, there are two pairs of good neighbors inside the word "occurrence",
since word[1] == word[2], and they are both 'c'; 
word[4] == word[5], and they are both 'r'.

E.g.3, there are two pairs of good neighbors inside the word "hmmm",
since word[1] == word[2], and they are both 'm'; 
word[2] == word[3], and they are both 'm'.


Write a function called "good_neighbors" that accepts a word as input, 
and return the number of pairs of good_neighbors. 
Assume that all the letters in the word are lowercase letters, 
and there are at least two letters in the word.

For example, good_neighbors("happy") will return 1, 
since there is one pair of adjacent letters 'p'.

good_neighbors("occurrence") will return 2, 
since there are twp pairs of adjacent letters, 'c' and 'r'.

word_example = "arrrrhhh"
good_neighbors(word_example) will return 5, since
word_example[1] == word_example[2], both 'r'
word_example[2] == word_example[3], both 'r'
word_example[3] == word_example[4], both 'r'
word_example[5] == word_example[6], both 'h'
word_example[6] == word_example[7], both 'h'


Hint:

We may compare each letter word[i] with its neighbor word[i + 1], 
while traversing the word using index i. Use the accumulator algorithm pattern.


Function implementation. (15 marks)
Pass your own unit tests. (5 marks) 
"""


def good_neighbors(word):
    count = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
    return count

assert good_neighbors("happy") == 1
assert good_neighbors("occurrence") == 2
assert good_neighbors("arrrrhhh") == 5
assert good_neighbors("a") == 0
assert good_neighbors("abc") == 0





"""
Exercise 11 - Coding question

Implement a function called "more_than_2" that accepts a list of strings as input. 
The function identifies strings that occur more than two times in the list,
and return these strings as a list. 

Eg.1, fruits = ["apple", "banana", "apple", "apple", "apple", "pear", "orange",
"banana", "banana", "watermelon"] 
more_than_2(fruits) will return ["apple","banana"]. 

Eg.2, colors = ["red", "red", "yellow", "green", "red", "yellow", "orange",
"green", "banana", "yellow"] 
more_than_2(colors) will return ["red", "yellow"]. 

Hint: Utilize dict data type to count the occurrences for each string, 
then traverse all the keys in the dict and compares its value to 3. 
Use the accumulator algorithm pattern.

Function implementation. (15 marks)
Pass your own unit tests. (5 marks) 
"""

def more_than_2(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    result = []
    for word, count in word_count.items():
        if count > 2:
            result.append(word)

    return result

# Unit tests
def test_more_than_2():
    fruits = ["apple", "banana", "apple", "apple", "apple", "pear", "orange",
              "banana", "banana", "watermelon"]
    colors = ["red", "red", "yellow", "green", "red", "yellow", "orange",
              "green", "banana", "yellow"]
    assert more_than_2(fruits) == ["apple", "banana"]
    assert more_than_2(colors) == ["red", "yellow"]
    assert more_than_2(["a", "b", "a", "c", "a", "d", "a"]) == ["a"]
    assert more_than_2(["apple", "banana", "pear"]) == []
    assert more_than_2([]) == []

test_more_than_2()



# Congratulations on your lab10! Please upload it to your github lab repository.