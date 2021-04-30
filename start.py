import discord

from utils import get_secret


# Read secrets
client_secret = get_secret("ClientSecret")


client = discord.Client()
client.run(client_secret)

