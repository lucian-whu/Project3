# coding=utf-8
import csv

with open('D://python_projects//project3//data//meshInformation.csv','r') as file:
    csvReader = csv.reader(file)
    for row in csvReader:
        with open('D://python_projects//project3//output//meshesNumber.txt','ab') as file1:
            file1.write(row[0]+"\n")

