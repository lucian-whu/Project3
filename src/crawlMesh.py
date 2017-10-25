# coding=utf-8
import random

import requests
import time
from bs4 import BeautifulSoup

# get mesh term one by one
with open("D://python_projects//project3//output//meshesNumber.txt",'r') as file:
    lines = file.readlines()
    for line in lines:
        term = line

        # get html page of mesh term
        kv = {'term':term}
        r = requests.get("https://www.ncbi.nlm.nih.gov/mesh",params=kv,headers={'user-agent':'Mozilla/5.0'},)
        #print(r.text)

        #parse the mesh term page for the introduced year
        Soup = BeautifulSoup(r.text,"lxml")
        if Soup.find("h1","title") is not None:
            mesh =Soup.find("h1","title").string
        else:
            mesh = term
        if Soup.find("p","mesh_year_introduced") is not None:
            year = Soup.find("p","mesh_year_introduced").string
            year = year.split(':')
            year = year[1]
        else:
            year = 'null'
        time.sleep(3 + random.randint(1,5))

        # write in a file called 'meshYear'
        with open('D://python_projects//project3//output//meshYear.csv','ab')as file1:
            line1 = mesh + "\t" + year + "\n"
            file1.write(line1)


