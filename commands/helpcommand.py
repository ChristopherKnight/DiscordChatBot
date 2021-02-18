#returns the help text for available bot commands
import commands.advancedhelp as ah
import discord

HELP_COMMAND = '!help'

def getResponseMessage(msg):
  #first check if the user wants advanced help, if not return other message
  msg = msg.content
  adv_help = ah.getIfAdvancedHelp(msg)
  if adv_help:
    helpMessage = ("""No advanced help for the help command""")
  else:
    helpMessage = (
      """
      > **__Minion Help __**
      > Use "!command help" to see advanced help. 
      > Example: !raid help
      > **__Supported Commands: __**
      > help - Display help text
      > ability - Display an ability guide for character
      > bug - Generate a bug report
      > cq-time - Calculate time till team reaches 45 K
      > emoji - Generate a list of Emojis available
      > members - List current club members of a club
      > openings - List current club member totals
      > ping - Ping!
      > raid - Get helpful raid info. !raid help for more info
      > restart - undefined
      > stone - Query information about sorcerer's stones
      """
    )
  embed=discord.Embed(description=helpMessage)
  return embed
