import discord
import os
import commands.commandparser as cmdparser

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Callback on chat message. Will send to message parse and will write a message in chat based on the command
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = cmdparser.checkcommands(message, client)
    if msg:
      #rich text formatting needs embeded
      if msg.type == "rich":
        await message.channel.send(embed=msg)
      else:
        await message.channel.send(msg)


@client.event
async def characterSearch(character):
  found = False
  channel = client.get_channel(810330418657099789)
  #channel = client.get_channel(725041802628825150)
  if channel:
    messages = await channel.history(limit=200).flatten()
    embed= None
    for msg in messages:
        if character in msg.content:
          if character.lower() == msg.content.lower():
            if len(msg.attachments) > 0:
              embed = discord.Embed()
              embed.set_image(url=msg.attachments[0].url)
              found = True

  if found:        
    await channel.send(embed=embed)
  else:
    sryMsg = 'Sorry, failed to find ' + character
    await channel.send(sryMsg)

# start the discord connection given the settings in the .env file
def runClient():
  client.run(os.getenv('TOKEN'))