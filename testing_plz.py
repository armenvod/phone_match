'''phone1 = 'Samsung Galaxy S8 Smartphone, Android, 5.8", 4G LTE, SIM Free, 64GB'

print(phone1.replace(',',''))'''


'''def brand_search(phone):
    result = []
    phone_split = phone.split()
    string_length = len(phone_split)
    i=0
    while i < string_length:
        empty = []
        phones = fon.getdevice(phone_split[i])
        try:
            for phone in phones:
                empty.append(phone['DeviceName'])

        except:
            empty.append(phones)
        i =i+1
        result.append(empty)
   # print(result)
    #seen = set()
   # uniq = [x for x in result if x not in seen and not seen.add(x)]
    #print(uniq)
    gross = [[1,2,3,],[2,5,6]]
    seen = set()
    repeated = set()
    for l in result:
        for i in set(l):
            if i in seen:
                repeated.add(i)
            else:
                seen.add(i)
    print(repeated)'''

import csv
import pandas as pd
df = pd.read_csv('18_oct.csv')
#saved_column = df['Name'] #you can also use df['column_name']

"""included_cols = [1,2]
with open('18_oct.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        content = list(row[i] for i in included_cols)
        print(content)"""
