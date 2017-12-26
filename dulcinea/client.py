import discord

client = discord.Client()

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
# reviewer automation
    elif message.content.startswith('!review'):
        role = discord.utils.get(message.server.roles, name="Reviewer")
        try:
            await client.add_roles(message.author, role)
        except discord.Forbidden:
            await client.send_message(message.channel, "I cannot add this role.")
    elif message.content.startswith('[Critique]'):
        role = discord.utils.get(message.server.roles, name="Reviewer")
        try:
            await client.remove_roles(message.author, role)
        except discord.Forbidden:
            await client.send_message(message.channel, "I cannot remove this role.")
    else:
        pass
try:
    client.run('Mzk0NzIxMTM3NjgwMDU2MzIz.DSIciQ.f7G1oR2TRORMrSeshf0ugiebkEE')
except discord.errors.LoginFailure:
    print("Failed to authenticate into Discord with provided token")