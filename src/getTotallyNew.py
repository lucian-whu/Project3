# coding=utf-8
import csv

with open('D://python_projects//project3//data//acute_myocardial_infarction_MESH_NEW_2006_2010.csv','r') as f:
    lines = f.readlines()
    for line in lines:
        print(line[0])
        # with open('','rb') as f1:
        #     csvReader1 = csv.reader(f1)
        #     for csvLine1 in csvReader1:
        #         if csv
