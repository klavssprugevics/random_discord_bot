import discord
import random

from utils import get_value_from_json, open_json


# Read secrets
client_secret = get_value_from_json('ClientSecret', './secrets.json')
client = discord.Client()

# Read image dictionary
image_dictionary = open_json('./image_dictionary.json')

# Events
@client.event
async def on_ready():
    print('Bot successfully logged in as: {0.user}'.format(client))


@client.event
async def on_message(message):

    # Checks if user has typed one of the keywords in the image dictionary
    for key in image_dictionary:    
        if(message.content.upper() == key):
            with open(image_dictionary[key], 'rb') as image:
                await message.channel.send(file=discord.File(image))
                break
    
    # Coinflip simulation
    if(message.content.upper() == '!COINFLIP'):
        if(random.random() < 0.5):
            with open('images/coinflip/heads.png', 'rb') as image:
                await message.channel.send(file=discord.File(image), content='Heads!')
        else:
            with open('images/coinflip/tails.png', 'rb') as image:
                await message.channel.send(file=discord.File(image), content='Tails!')



# Startup
client.run(client_secret)
