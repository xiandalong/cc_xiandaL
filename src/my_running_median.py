__author__ = 'Kelvin'

# import the regular expression and os libraries
import re
import os
import sys

################## Part II: Running Median ##################################

# define a function to count the number of words in a string
def wc(string):
    string = re.sub("-", "", string) # remove all hyphens
    string = re.sub("'", "", string) # remove apostrophes
    word_list = re.sub("[^\w]", " ", string).split()
    return len(word_list)

# define a function median to calculate the median for a List of numbers
def median(L):
    L = sorted(L)
    n = len(L)
    m = n - 1
    return (L[n / 2] + L[m / 2]) / 2.0

print "##################################################################"
print "Start finding running median..."

# define the directory
direct = sys.argv[1]
# define the path for the output file
outfile_path = sys.argv[2]

# get a list of files in this directory and sort it on alphabetical order
file_list = os.listdir(direct)
file_list = sorted(file_list)

# check if the file_list is empty, if so print out the error message and terminate the program
if len(file_list) == 0:
    print("No files in the input folder!")
    exit()

# initialize a list to contain the lines in all the text file
all_lines = []
# use a fool loop to read each text file in the input folder
for file in file_list:
    # get full path of the file
    file_path = direct + '/' + file
    # read each line in the file
    with open(file_path) as f:
        content = f.readlines()
    all_lines+=content
print "All text files loaded..."

# initialize a list to contain the word count
wc_list = []
# process each line and generate running median
print "Start writing results to the output file : med_result.txt..."
f = open(outfile_path, "w") # open file
for line in all_lines:
    # read the word count in this line
    word_count = wc(line)
    wc_list.append(word_count)
    # get the median and write this line to the output file
    f.write(str(median(wc_list)) + '\n')
f.close() # close file
print "Result is generated for running median! Check the wc_output folder"
print "##################################################################"
