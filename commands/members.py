#returns the result of the club conquest command
import commands.advancedhelp as ah
import discord
import json
import os

MEMBERS_COMMAND = '!members'

clubs = None
guild_id = None

def set_clubs():
  #read the json resource for the clubs and save them in a dictionary
  cur_path = os.path.dirname(__file__)
  cur_path = os.path.join(cur_path, '../resources/sigma-guild-info.json')
  with open(cur_path) as f:
    data = json.load(f)
  global clubs
  global guild_id
  clubs = data['clubs']
  guild_id = data['guild_id']

def get_club_not_found_message():
  #return the message if a bad club is passed to the bot
  club_list = ''
  for c in clubs:
    club_list += c["role"] + "\n"
  helpMessage = 'Club Not Found.  Available Clubs: \n\n' + club_list
  return helpMessage

def getResponseMessage(msg):
  #first check if the user wants advanced help, if not return other message
  guild = msg.guild
  msg = msg.content
  adv_help = ah.getIfAdvancedHelp(msg)
  if adv_help:
    helpMessage = (
      """
      > **__Minion Help __**
      > !members lists out the members for the club given
      > arguments:
      >   1. Club Tag Name
      """
    )
    
  else:
    set_clubs()
    #get the club name being passed in chat
    split_msg = msg.split("!members ")
    if len(split_msg) == 2:
      tag = split_msg[1]
      
      club = None
      #Loop over list of clubs to see if passed club matches
      for c in clubs:
        if c["role"].lower() == tag.lower():
          club = c
      if club:
        #if the club is found, loop over guild members to see if they are in that club
        member_count = 0
        member_list = ''
        for member in guild.members:
          for mem_role in member.roles:
            if str(mem_role) == club['role']:
              member_count += 1
              member_list += member.name + "\n"
          
        #return a message with the club name plus available members
        helpMessage = 'Members of ' + club["name"] + ": (" + str(member_count) + ")\n\n" + member_list
      else:
        helpMessage = get_club_not_found_message()
    else:
      helpMessage = get_club_not_found_message()

  embed=discord.Embed(description=helpMessage)
  return embed
