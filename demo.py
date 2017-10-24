from fonAPI import FonApi

fon = FonApi('401bfde5401d0bdce2edddba6bcaa1d4bc8e4d17091b92cd')

#brand = 'Samsung '
phone1 = 'Apple iPhone 6s Plus, iOS, 5.5", 4G LTE, SIM Free, 128GB,'



def brand_search(phone):
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
    print(repeated)



def phone_search(phone):
    phone_clean = phone.replace(',','')
    result = []
    l = 0
    while l< len(phone_clean)-2:
        empty = ''
        phones = fon.getdevice(phone_clean.rsplit(' ',l)[0])
        try:
            for phone in phones:
                empty = phone['DeviceName']

        except:
            empty = phones
        #if empty[-1]
        l = l + 1
        result.append(empty)
    result[:] = [x for x in result if x != u'No Matching Results Found.']
    print result

phone_search(phone1)



