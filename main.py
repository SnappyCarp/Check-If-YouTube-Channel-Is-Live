import requests
from time import sleep


#Enter The Homepage Of The Channel You Want To Check(ie https://www.youtube.com/@LofiGirl)
channel_url = ''


while True:
    try:
        print('Checking If Channel Is Live')
        content = requests.get(channel_url).text
        EC = str(content).encode("ascii", "ignore")

        if 'hqdefault_live.jpg' in EC.decode():
            print('Channel Is Live')
        else:
            print("Channel Isn't Live")
    except Exception as error:
        print(f'Error {error}')
    
    sleep(3)
