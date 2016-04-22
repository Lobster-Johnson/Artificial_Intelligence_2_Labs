# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:11:02 2016

@author: Christopher Jerrard-Dunne
@student_number: C12449618

@author2: Marcus Daly
@student_number2: C12474932
"""

import sys
import pandas as pandas
import numpy as numpy
import random
from sklearn.ensemble import RandomForestClassifier
import csv
from collections import Counter

def main():
    
    if len(sys.argv) != 3:
        print("Usage: python filename [training_set] [queries]")
    
    print("Hello World")
    
    headings = [
    "ID",
    "age",
    "job",
    "marital",
    "education",
    "default",
    "balance",
    "housing",
    "loan",
    "contact",
    "day",
    "month",
    "duration",
    "campaign",
    "pdays",
    "previous",
    "poutcome",
    "y"
]
answerData = []
   
"""Read in data"""
trainingdata = pandas.read_csv("Data/trainingset.txt",header = None, names = headings)
queries = pandas.read_csv("Data/queries.txt",header = None, names = headings)



idnum = [0]
target = [17]
cont = [1, 5, 6, 10, 12, 13, 14, 15]
cat = [2, 3, 4, 7, 8, 9, 11, 16]



"""Learn from data"""
    
##Continuous Relevant Data: age, balance, previous
##Categorical Relevant Data: job, housing, loan, contact
##
##INSERT CODE THAT DOES THINGS HERE
##Implement Random Forest predictive algorithm
##Format data into numerical format
    
relevantFeatures = ["age","balance","previous","job","housing","loan","contact"]

#Convert job to numeric
def job_to_numeric(x):
    if x == 'unknown':
        return 0
    else:
        y = x[6:]
        return int(y)
#convert housing to numeric
def houseLoan_to_numeric(x):
    if x == 'yes':
        return 0
    if x == 'no':
        return 1
#convert loan to numeric
#see above
#convert contact to numeric
def contact_to_numeric(x):
    if x == 'unknown':
        return 0
    if x == 'telephone':
        return 1
    if x == 'cellular':
        return 2

"""Answer Queries"""




dataHeader = ["ID","Y"]
answerData.append(dataHeader)


#the following is test code to get id and target and put it into the answers
length = len(trainingdata.index)
print(length)

for x in range (0, length):
    temp = []
    newid = trainingdata.iloc[x]['ID']
    temp.append(newid)
    newtarget = trainingdata.iloc[x]['y']
    temp.append(newtarget)
    answerData.append(temp)

    

"""Output Queries"""
#Write all the data from the array into a text file.
 #Each iteration of queries should be written into the answerData list, as lists themselves.
newfile = open('./data/C12449618+C12474932.txt', 'w')
writerObject = csv.writer(newfile, lineterminator='\n')
    
for line in answerData:
    writerObject.writerow(line)
        
newfile.flush()
newfile.close()

if __name__ == '__main__':
    main()
 
