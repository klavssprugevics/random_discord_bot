import discord

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
        if(message.content == key):
            with open(image_dictionary[key], 'rb') as image:
                await message.channel.send(file=discord.File(image))
                break
    



# Startup
client.run(client_secret)
