import discord
import os
import commands.commandparser as cmdparser

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Callback on chat message. Will send to message parse and will write a message in chat based on the command
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = cmdparser.checkcommands(message)
    if msg:
      #rich text formatting needs embeded
      if msg.type == "rich":
        await message.channel.send(embed=msg)
      else:
        await message.channel.send(msg)
    
# start the discord connection given the settings in the .env file
def runClient():
  client.run(os.getenv('TOKEN'))