import discord
import os
import requests
import json
import curses
from Server import keep_alive
def mute():
    pass
client = discord.Client()

map = []

curses = ["fuck","cunt"]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message.author)
    if message.author == client.user:
        return 
    
    if message.content.startswith('$hello'):
        await message.channel.send("Hello! I am Pigeon, How may I be of service?")
    elif message.content.startswith('$add curses'):
        await message.channel.send("Hello, " + str(message.author) + "!!\nThank you for updating my curses dictionary")
        msg = message.content.lower().replace("$add curses ","")
        curses.append(msg)
        print(curses)
    elif any(curse in message.content.lower() for curse in curses):
        if message.author in map:
            await message.channel.send("Shut Up")
        else:
            await message.channel.send("Warning, Next Time you will be muted for 30 minutes")
            map.append(message.author)
keep_alive()
client.run(os.getenv('TOKEN'))
