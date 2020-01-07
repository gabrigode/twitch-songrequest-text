from urllib.request import urlopen
import json
import requests
import time
import os

print ('--------------------------TWITCH-SONGREQUEST-WRITE-----------------------------------------------------')

channelName = input('Channel name:')

channel_url = f'https://api.nightbot.tv/1/channels/t/{channelName}'
channel_load = urlopen(channel_url)

jsonList = json.load(channel_load)
channel_id = jsonList['channel']['_id']
print (f"Channel's id: {channel_id}")

def Music():
    r = requests.get("https://api.nightbot.tv/1/song_requests/queue", headers={"Nightbot-Channel":channel_id})
    musicName = (r.json()['_currentSong']['track']['title'])
    print (f"Playing: {musicName}")
    f = open('music.txt', 'w', encoding='utf-8')
    f.write(musicName)
    f.close()

while True:
    Music()
    print ("Refreshing page...")
    time.sleep(10)
    

