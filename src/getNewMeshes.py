# coding=utf-8
import csv

with open('D://python_projects//project3//data//meshInformation.csv','rb') as f:
    csvReader = csv.reader(f)
    header = csvReader.next()



    for csvLine in csvReader:
        if csvLine[3] is not "DateEstablishedYear":
            year = int(csvLine[3])
            if year > 2005:
                s = str(csvLine[1]) + '\t'+ str(year)
                with open('D://python_projects//project3//output//newMeshes.csv','ab') as f1:
                    newMesh = s + '\n'
                    f1.write(newMesh)
