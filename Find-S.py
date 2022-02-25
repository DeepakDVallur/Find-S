
"""
Implement and demonstrate the FIND-S algorithm for finding the most specific hypothesis 
based on a given set of training data samples. Read the training data from a .CSV file


CSV stands for “Comma Separated Values.” 
It is the simplest form of storing data in tabular form as plain text.
"""
# To read a CSV file: The first step is to import the csv library
import csv

# Create the empty List to store the values
a = []

# The open() method in python is used to open files and return a file object.
# use csv.reader object to read the CSV file
with open('1.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)

# To Check how many instances are there in the data set
print("\n The total number of training instances are : ",len(a))

# assign the total number of features excluding the target value. Hence, len(h[0])-1
num_attribute = len(a[0])-1

# Initialize  h  to  the  most  specific  hypothesis  in  H 
hypothesis = ['0']*num_attribute
print("\n The initial hypothesis is : \n", hypothesis)


# For  each  positive  training  instance  x
#  For  each  attribute  constraint  ai  in  h 
#   If  the  constraint  ai  is  satisfied  by  x 
#             Then  do  nothing 
#   Else  replace  ai  in  h  by  the  next  more  general  constraint  that  is  satisfied  by  x

for i in range(0, len(a)):
    if a[i][num_attribute] == 'yes':
        for j in range(0, num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
    print("\n The hypothesis for the training instance {} is: \n" .format(i+1),hypothesis)

print("\n The Maximally specific hypothesis for the training instances is: \n",hypothesis )