#returns the help text for available bot commands
import commands.advancedhelp as ah
#from discordclient import client
import discord

ABILITY_COMMAND = '!ability'

def getResponseMessage(msg, client):
  #first check if the user wants advanced help, if not return other message
  helpMessage = None
  msg = msg.content
  adv_help = ah.getIfAdvancedHelp(msg)
  if adv_help:
    helpMessage = (
      """
      > **__Minion Help __**
      > !ability takes the character given and returns a graphic on ability priority
      > arguments:
      >   1. Character Name
      """
    )
  else:

    split_msg = msg.split("!ability ")
    if len(split_msg) == 2:
      character = split_msg[1]
      #start the command in the background to pull messaged async
      client.loop.create_task(client.characterSearch(character))

  if helpMessage:
    embed=discord.Embed(description=helpMessage)
    return embed
  else:
    return None
