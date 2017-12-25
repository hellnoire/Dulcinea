import discord
import asyncio
import random

client = discord.Client()
secure_random = random.SystemRandom()
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
        await client.send_message(message.channel,secure_random.choice(eight_ball))
client.run('Your_Token_Here')
