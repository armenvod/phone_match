import csv
import pandas
from fonAPI import FonApi
from itertools import islice # may have to run chcp 65001

fon = FonApi('401bfde5401d0bdce2edddba6bcaa1d4bc8e4d17091b92cd')

# Import csv file and pick out phone names
with open( '18_oct.csv', 'r', newline='') as f:
    num_lines = sum(1 for line in f) #number of lines i.e. number of phones
    
with open( '18_oct.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    name_list = list(islice((row[1] for row in reader), num_lines)) #output is list of phone names

csvfile = "names_cleaned.csv"

#JC Testing git
#brand = 'Samsung '
phone1 = 'Samsung Galaxy J3 Smartphone, Android, 5", 4G LTE, SIM Free, 8GB,'

def phone_search(phone):
    '''function cycles through the website string and searches using fonoAPI.
     It shaves off a word from the string every time until the first phone match is found.'''
    phone_clean = phone.replace(',','') # removes commas from string
    result = ''
    l = 0
    while l< len(phone_clean):
        empty = ''
        phones = fon.getdevice(phone_clean.rsplit(' ',l)[0]) # deletes the "l"th word
        try: # fonoAPI name match command
            for phone in phones:
                empty = phone['DeviceName']
        except:
            empty = phones
        if empty != u'No Matching Results Found.':
            result = empty # result is equal to the first result found by fonoAPI
            break
        else:
            l = l + 1
    return result


def clean_names(list): #function cycles through list and outputs matching names
    names_clean = []
    for i in range(num_lines):
        search = phone_search(list[i])
        names_clean.append(search)
        i=i+1 
    print(names_clean)
    with open(csvfile, "w") as output:#output names into a csv file
        writer = csv.writer(output, lineterminator='\n')
        for val in names_clean:
            writer.writerow([val])   
           


if __name__ == "__main__":
    clean_names(name_list)