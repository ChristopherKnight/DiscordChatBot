#returns the result of the club conquest command
import commands.advancedhelp as ah
import discord
import math

CQ_COMMAND = '!cq-time'

def getResponseMessage(msg):
  #first check if the user wants advanced help, if not return other message
  adv_help = ah.getIfAdvancedHelp(msg)
  if adv_help:
    helpMessage = (
      """
      > **__Minion Help __**
      > !cq-time calculates when a team reaches 45k points
      > or if a team can pass the other with the time left
      > for reaching 45k points use arguments 1 and 2
      > for seeing if team 2 can pass team 1, use all 4
      > arguments:
      >   1. Team 1 current score
      >   2. Team 1 points per minute
      >   3. Team 2 current score
      >   4. Team 2 points per minute 
      """
    )
    
  else:
    try:
      split_msg = msg.split(" ")
      if len(split_msg) == 3:
        team1 = (45000 - int(split_msg[1])) / int(split_msg[2]) / 60;
        team1 = math.floor(team1);
        helpMessage = 'This team will reach 45k in ' + str(team1) + ' hours'
      elif len(split_msg) == 5:
        team1 = (45000 - int(split_msg[1])) / int(split_msg[2]) / 60;
        team2 = (45000 - int(split_msg[3])) / int(split_msg[4]) / 60;
        team1 = math.floor(team1);
        team2 = math.floor(team2);
        if (team2 < team1):
          helpMessage = 'Team 2 will overtake team 1 and win in ' + str(team2) + ' hours'
        else:
          helpMessage = 'Team 2 will never catch up'
      else:
        helpMessage = 'Invalid Number of Arguments sent. Use "!cq-time help" for advanced help'
    except:
      helpMessage = 'Invalid Argument Types. Make sure they are numbers'

  embed=discord.Embed(description=helpMessage)
  return embed
