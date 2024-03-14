"""
Excercises (in-class) - Files 

Objective: Practice working with files. 

"""


"""
Part 1 - How to read a file

To work with files, we can read the whole file at once by using readlines(), 
or we can use loops and process a file one line at a time.
"""

def read_file_once():
    """
    This function reads the whole file at once
    """
    f_ref = open("week8_bus_record.txt", 'r')
    lines = f_ref.readlines()
    print("The lines are:\n")
    for line in lines:
        print(line)
    f_ref.close()  # Remember to close the file after processing


#read_file_once()


def read_file_once_with():
    """
    This function reads the whole file at once
    """
    with open("week8_bus_record.txt", 'r') as f_ref:  # "with" makes sure the file closed
        lines = f_ref.readlines()
        print("The lines using with are:\n")
        for line in lines:
            print(line)


#read_file_once_with()


def read_file_line_by_line():
    """
    This function prints the file content line by line
    """
    f_ref = open("week8_bus_record.txt", 'r')
    print("Line by line:\n")
    for line in f_ref:
        print(line)
    f_ref.close()  # Remember to close the file after processing


#read_file_line_by_line()


def read_file_line_by_line_with():
    """
    This function prints the file content line by line
    """
    with open("week8_bus_record.txt", 'r') as f_ref:
        print("Line by line using with: \n")
        for line in f_ref:
            print(line)


#read_file_line_by_line_with()
            
"""
Exercise 1: Complete the function below to 
only print the first 2 lines of the file week8_bus_record.txt.
"""

def read_two_lines():
    """
    This function only reads the first two lines of a file
    """
    f_ref = open("week8_bus_record.txt", 'r')    
    f_ref.close()  # Remember to close the file after processing

#read_two_lines()




"""
Part 2 - How to write a file
"""

def write_file():
    """
    This function writes a file
    """
    f_ref = open("ex_write.txt", "w")
    f_ref.write("We are all from COMP115!\n")
    f_ref.write("This is the second line, also the last line.\n")
    f_ref.close()


#write_file()


def write_file_with():
    """
    This function writes a file
    """
    with open("ex_write_with.txt", "w") as f_ref:
        f_ref.write("Hello, COMP115!\n")
        f_ref.write("This is the second line, also the last line.")


#write_file_with()
"""
The function below writes into a file named about.txt with name 
and hobby in the same line, separated by tab, given name and hobby as parameters.
"""


def write_hobby_file(name, hobby):
    """
    This function writes into a file with info (name and hobby) about the programmer
    """
    f_ref = open("name_hobby.txt", "w")
    f_ref.write(f"{name}\t")
    f_ref.write(f"{hobby}\n")
    f_ref.close()

#write_hobby_file("Ava", "Fishing")



"""
Exercise 2: Complete the function below to 
read the file week8_bus_record.txt,
and write the first id in each line into a file named first_ids.txt.

i.e., the first_ids.txt content will be:
110
108
110
102
"""


def write_first_ids():
    f_in = open("week8_bus_record.txt", "r")
    f_out = open("first_ids.txt", "w")
    f_in.close()
    f_out.close()


#write_first_ids()

"""
The following program reads lines from an input file - week8_bus_record.txt. After processing 
the data into a dictionary, it writes data in the dictionary into an output file - week8_bus_id_freq.txt, 
which will be in the same folder as this python file.
"""
def create_id_frequence_file():
    f_in = open("week8_bus_record.txt", "r")
    lines = f_in.readlines()

    dict_id_freq = {}
    for line in lines:
        ids = line.split()
        for id in ids:
            if id in dict_id_freq:
                dict_id_freq[id] += 1
            else:
                dict_id_freq[id] = 1
    
    f_out = open("week8_bus_id_freq.txt", "w")
    f_out.write("ID\tFrequency\n")
    for id in dict_id_freq:
        f_out.write(f"{id}\t{dict_id_freq[id]}\n")
    f_in.close()
    f_out.close()

#create_id_frequence_file()

"""
Given the list of student ids that are records of taking the shuttle bus, 
write a function bus_max_id to return the student id(s) who take the shuttle bus most frequently.

E.g., bus_max_id(["110", "180", "120", "180", "162", "110", "192", "253"]) will 
return ["110", "180"],
bus_max_id(["110", "180", "120", "180", "162", "110", "180", "253"]) will return ["180"].

"""


def bus_max_id(ids):
    dict = {}
    for id in ids:
        dict[id] = dict.get(id, 0) + 1

    #max_value = max(dict.values())
    max_value = 0
    for id in dict:
        if dict[id] > max_value:
            max_value = dict[id]

    res = []
    for id in dict:
        if dict[id] == max_value:
            res.append(id)
    return res


assert bus_max_id(["110", "180", "120", "180", "162", "110", "192", "253"]) == ["110", "180"]
assert bus_max_id(["110", "180", "120", "180", "162", "110", "180", "253"]) == ["180"]



"""
Exercise 3:

We have the input file - week8_bus_record.txt in the folder. 
Please complete the function below to find the student id(s) 
who have the maximum occurrences in the bus record, 
and write the id(s) and value of the maximum occurrence into the file.

The output file's name is week8_id_bus_most.txt, in which there should be 
"
110 	 4
112      4
".

Hint:
You may first use dict to store the occurrences of all the students who take the bus. 
Then find the maximum occurrence.
Then output the id(s) and the maximum value into the file.

"""


def students_id_max_occurrences():
    f_in = open("week8_bus_record.txt", 'r')
    f_out = open("week8_id_bus_most.txt", 'w')
    f_in.close()
    f_out.close()


#students_id_max_occurrences()




"""
The typical reason why we work with files is because 
these files are too big, i.e., containing too many data,
or the data inside is changing all the time.
Therefore the data cannot be included inside the program explicitly, 
and we read data from other files.

For exercise 4, 5, we are going to use data from IMDb (Internet Movie Database). 

There are 2 data files for you:
 - title.basics.tsv - Contains the following fields for titles:

    tconst (string) - alphanumeric unique identifier of the title
    titleType (string) - the type/format of the title (This file only contain movie type)
    primaryTitle (string) - the more popular title / the title used by the filmmakers 
    originalTitle (string) - original title, in the original language
    isAdult (boolean) - 0: non-adult title; 1: adult title
    startYear (YYYY) - represents the release year of a title.
    endYear (YYYY) - TV Series end year. '\\N' for all other title types
    runtimeMinutes - primary runtime of the title, in minutes
    genres (string array) - includes up to three genres associated with the title

 - title.ratings.tsv - Contains the IMDb rating and votes information for titles

    tconst (string) - alphanumeric unique identifier of the title
    averageRating - weighted average of all the individual user ratings
    numVotes - number of votes the title has received

The details of these files can be found at https://www.imdb.com/interfaces/

"""

"""
The following function returns the number of the titles 
of which the ratings are more than 7.0, in the file title.ratings.tsv
"""
def count_rating_over_7():
    f = open('title.ratings.tsv', 'r')
    lines = f.readlines()
    count_over_7 = 0
    for line in lines[1:]:  # Think about why starting from 1 instead of 0
        words = line.split()
        if float(words[1]) > 7:
            count_over_7 += 1
    return count_over_7

#print(count_rating_over_7())
"""

Exercise 4:
Complete the function below to write into a file named rating_over_7.txt with
the titles of which the ratings are more than 7.0 in the file title.ratings.tsv.
"""


def write_rating_over_7():
    f_in = open('title.ratings.tsv', 'r')
    f_out = open("rating_over_7.txt", 'w')
    
    f_in.close()
    f_out.close()


#write_rating_over_7()
    
"""
Exercise 5

In the file title.basics.tsv, the 1st field contains a string indicating the title id, 
and the last field contains a string of movie genres (e.g., "Animation, Comedy, Romance").

Complete the following function to write into a file named comedy_titles.txt 
with the title ids of which the genres belong to Comedy.

Hint: 
    You will need to first split each line into fields. 
    split() method can split a string into a list.
    The default separator of split() is any whitespace. You can specify the separator. 
    For the file 'title.basics.tsv', the separator is tab '\t'.
    For separating the string of genres, you may want to use ',' as the separator.
"""


def write_comedy_titles():
    f_in = open('title.basics.tsv', 'r')
    f_out = open('comedy_titles.txt', 'w')

    f_in.close()
    f_out.close()
#write_comedy_titles()

# Note: all the exercises here have no return values,
# but generate side effects by reading or writing a file, i.e., void functions.