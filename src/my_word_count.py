__author__ = 'Kelvin'

# import the regular expression and os libraries
import re
import os
import sys


################## Part I: Word Count ##################################

# function read_words reads all the words from a certain text file
def read_words(file_path):
    text_file = open(file_path, "r")
    x = text_file.read()
    x = re.sub("-", "", x) # remove all hyphens
    x = re.sub("'", "", x) # remove apostrophes
    word_list = re.sub("[^\w]", " ", x).split()
    return word_list

print "##################################################################"
print "Start counting words..."

# define the directory
direct = sys.argv[1]
# define the path for the output file
outfile_path = sys.argv[2]

# initialize a new dictionary
word_dict = {}
# get a list of files in this directory and sort it on alphabetical order
file_list = os.listdir(direct)
file_list = sorted(file_list)
# check if the file_list is empty, if so print out the error message and terminate the program
if len(file_list) == 0:
    print("No files in the input folder!")
    exit()
# go through each file
for file in file_list:
    # if the file is a .txt file
    if file.endswith(".txt"):
        file_path = direct + '/' + file
        wl = read_words(file_path)
        # use for loop to process all the words in word_list
        for word in wl:
            word_lc = word.lower()
            if word_lc in word_dict:
                # if the key exist, add 1 to count
                word_dict[word_lc] += 1
            else:
                # if the key does not exist, create a new key in this dictionary
                word_dict[word_lc] = 1


# sort the whole dictionary
word_dict_sorted = sorted(word_dict.items(), key=lambda t: t[0])
print "A dictionary is generated..."

# define the width of each line in wc_result.txt
max_width = max(len(word_info[0]) + len(str(word_info[1])) for word_info in word_dict_sorted) + 2

# writing results
print "Start writing results to the output file : wc_result.txt..."
with open(outfile_path, "w") as text_file:
    # write each key-value pair to the output file
    for word_info in word_dict_sorted:
        text_file.write(word_info[0].ljust(max_width) + str(word_info[1]).rjust(0) + '\n')
print "Result is generated for word count! Check the wc_output folder"
print "##################################################################"
