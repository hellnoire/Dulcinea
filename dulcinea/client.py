import discord
from PyDictionary import PyDictionary

client = discord.Client()
dictionary = PyDictionary()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# required modules, can be edited
from modules.service.help import help
from modules.service.commands import commands
# misc modules
from modules.games.eightball import eightball
from modules.games.snark import snark
from modules.games.library.master import master

@client.event
async def on_message(message):
    pass
    if message.content.startswith('!Help'):
        await client.send_message(message.channel, help())
    elif message.content.startswith('!Commands'):
        await client.send_message(message.channel, commands())
    elif message.content.startswith('!8ball'):
        await client.send_message(message.channel, eightball())
    elif message.content.startswith('!Story'):
        await client.send_message(message.channel, master())
    elif message.content.startswith('!Snark'):
        await client.send_message(message.channel, snark())
    elif message.content.startswith('!define'):
        word = message.content.split(' ')[1]
        try:
            await client.send_message(message.channel, dictionary.meaning(word))
        except discord.Forbidden:
            await client.send_message(message.channel, "No bueno.")
        except discord.errors.HTTPException:
            await client.send_message(message.channel, "I'm sorry, I'm drawing a blank. Can you try a different word?")
    elif message.content.startswith('!synonym'):
        word = message.content.split(' ')[1]
        try:
            await client.send_message(message.channel, dictionary.synonym(word))
        except discord.Forbidden:
            await client.send_message(message.channel, "No bueno.")
        except discord.errors.HTTPException:
            await client.send_message(message.channel, "I'm sorry, I'm drawing a blank. Can you try a different word?")
    elif message.content.startswith('!antonym'):
        word = message.content.split(' ')[1]
        try:
            await client.send_message(message.channel, dictionary.antonym(word))
        except discord.Forbidden:
            await client.send_message(message.channel, "No bueno.")
        except discord.errors.HTTPException:
            await client.send_message(message.channel, "I'm sorry, I'm drawing a blank. Can you try a different word?")
# reviewer automation
    elif message.content.startswith('!Review'):
        role = discord.utils.get(message.server.roles, name="Writ-on")
        try:
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, 'Thank you for the review! You can post content now!')
        except discord.Forbidden:
            await client.send_message(message.channel, "I cannot add this role.")
    elif message.content.startswith('[Critique]'):
        role = discord.utils.get(message.server.roles, name="Writ-on")
        try:
            await client.remove_roles(message.author, role)
            await client.send_message(message.channel, 'Thanks for posting! I hope you get a nice review!')
        except discord.Forbidden:
            await client.send_message(message.channel, "I cannot remove this role.")
    else:
        pass
try:
    client.run('token')
except discord.errors.LoginFailure:
    print("Failed to authenticate into Discord with provided token")
