

#Replace student names with Avengers names. 

from os import lstat
import pandas as pd
import numpy as np

#Create the dictionary. This has the students' name with the Avengers name that will replace the student name.
import csv
 
dict_from_csv = {}
with open("c:/Users/campb/OneDrive/Documents/Personal/RandomPythonScripts/RenameStudents_Avengers/Avengers_Rename.csv", mode = 'r') as inp:
    reader = csv.reader(inp)
    dict_from_csv= {rows[0]:rows[1] for rows in reader}

#print(dict_from_csv)

#nested loop
#inner loop loops through a given csv, matches the student name with its avengers' name. 
##read csv
#df = pd.read_csv("c:/Users/campb/OneDrive/Documents/Personal/RandomPythonScripts/RenameStudents_Avengers/Names/zoomus_meeting_report_91240224982_Feb01.csv")
#Replace values in column "User Name" with dictonary items (i.e., matched avengers names)
#df2 = df.replace({"User Name":dict_from_csv}, inplace=TRUE)

#save csv under same name? 

#outer loop loops through all csv's, running the inner loop on each csv. 
#lst = create list of csv's
path = "C:/Users/campb/OneDrive/Documents/Personal/RandomPythonScripts/RenameStudents_Avengers/Names"
import os
folder = os.fsdecode(path)
filenames = []

#https://stackoverflow.com/questions/62426695/find-and-replace-in-multiple-csv-files-using-python
for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.endswith(('.csv')):
        filenames.append(filename)

filenames.sort()

#each csv is in each row of the filenames. 
#Task: for each line in filenames,
    #do read then replace

import glob as glob
all_files = glob.glob(os.path.join(path, "*.csv"))
df = pd.concat(map(pd.read_csv, filenames))
li = []
for filename in filenames:
    with open(os.path.join(path, filename), 'r') as f:
        reader = csv.reader(f)
        renames = {rows[0]:rows[1] for rows in reader}
        f.replace({"User Name":dict_from_csv}, inplace=True)
f.close()
    #save?
    #close(df) row1 of filenames

