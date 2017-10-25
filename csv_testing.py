import csv
import pandas as pd


'''with open('18_oct.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=';')
    for column in reader:
        print(column[0])'''


from itertools import islice # may have to run chcp 65001

with open( '18_oct.csv', 'r', newline='') as f:
    num_lines = sum(1 for line in f)
    
with open( '18_oct.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    output = list(islice((row[1] for row in reader), num_lines))

for i in range(num_lines):
    print(output[i])
    i=i+1
