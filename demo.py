from fonAPI import FonApi

fon = FonApi('247b4f00e53c7e4e8304e2aa3edd8342850de201e0c60ce8')

device = 'p10'
phones = fon.getdevice(device)
try:
    for phone in phones:
        print phone['DeviceName']
        print phone['weight']
        print phone['resolution']
except:
    print phones
