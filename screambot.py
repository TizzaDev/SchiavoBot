import discord
import re

TOKEN = 'MjgxNzk4MjQzMTY2MTkxNjE2.WKW7EA.GlQmVmcKTUSbJY6CPk5815wr-i0'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    cmd = str(message.content)
    filtered_cmd  = re.sub(' +', ' ',cmd)
    words = filtered_cmd.split(' ')
    if words[0].lower() == 'schiavo':
        if words[1].lower() == 'urla':
            text = filtered_cmd.lower().replace('schiavo urla ','')
            response = ''
            for char in text:
                if char == ' ':
                    response += ' '*3
                else:
                    response += f':regional_indicator_{char}:'
            await message.channel.send(response)

client.run(TOKEN)
