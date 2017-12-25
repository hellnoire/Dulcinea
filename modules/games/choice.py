import discord
import asyncio
from random import randint

client = discord.Client()
eight_ball = ['hell no', 'it is a risk', 'maybe...', 'sure, why not?', 'hell yeah!']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!8ball'):
        await client.send_message(message.channel, eight_ball[randint(0, len(eight_ball))])
try:
    client.run('vodDA1jVqG84X2ob5sJNqoD9LWA8kNCq')
except discord.errors.LoginFailure:
    print("Failed to authenticate into Discord with provided token")
