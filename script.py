from urllib.request import urlopen
import json
import requests
import time
import os

f = open('music.txt', 'w', encoding='utf-8') #CREATES A MUSIC.TXT AND IF ALREADY EXISTS REWRITES HIM

print ('--------------------------TWITCH-SONGREQUEST-WRITE-----------------------------------------------------')

check = True
while check == True:
    try:
        channelName = input('Channel name:')
        channel_url = f'https://api.nightbot.tv/1/channels/t/{channelName}'
        channel_load = urlopen(channel_url)
        jsonList = json.load(channel_load) #LOADS THE SITE'S JSON
        channel_id = jsonList['channel']['_id'] #SEARCHS FOR THE CHANNEL'S ID
        print (f"Channel's id: {channel_id}")
        check = False
    except OSError:
        print('Channel not found, try again')
        continue

def Music():

    r = requests.get("https://api.nightbot.tv/1/song_requests/queue", headers={"Nightbot-Channel":channel_id}) #REQUESTS API DATA AND APPLY CHANNEL'S ID IN HTTP HEADER
    try:
        musicName = (r.json()['_currentSong']['track']['title']) #LOADS AS JSON AND SEARCHS FOR SONG'S NAME
        f = open('music.txt', 'r', encoding='utf-8') 
        if (f.read()) == musicName:
            pass
        else:
            f = open('music.txt', 'w', encoding='utf-8') #PUTS THE NAME IN A TEXT FILE IF NOT ALREADY THERE
            print (f"Now playing: {musicName}")
            f.write(musicName)
            f.close()
    except TypeError:
        print ('Nothing playing...')
        pass

while True:
    Music()
    time.sleep(10)
    

