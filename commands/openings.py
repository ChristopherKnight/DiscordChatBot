#returns the result of the club conquest command
import commands.advancedhelp as ah
import discord
import json
import os

OPENINGS_COMMAND = '!openings'
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


def getResponseMessage(msg):
  #first check if the user wants advanced help, if not return other message
  guild = msg.guild
  msg = msg.content
  adv_help = ah.getIfAdvancedHelp(msg)
  if adv_help:
    helpMessage = (
      """
      > **__Minion Help __**
      > !openings lists out all clubs and whether or not they have openings for new members
      """
    )
    embed=discord.Embed(description=helpMessage)
    
  else:
    set_clubs()
    #loop over all clubs recording their members to find openings
    embed=discord.Embed(title="Current Openings")
    for c in clubs:
      clubStr = c["short_name"] + ' (SS. ' + str(c["min_ss"] / 1000) + 'k lvl' + str(c["min_level"]) + ')'
      member_count = 0
      for member in guild.members:
        is_leader = False
        is_member = False
        for mem_role in member.roles:
          if str(mem_role) == c["role"]:
            member_count += 1
            is_member = True
          #Check if the captain. 
          if str(mem_role) == 'Club Leader':
            is_leader = True

        #Check leader name for / to indicate held spots
        if is_leader and is_member:
          leader_name_split = member.name.split("/")
          #subtract 1 for the actual member name which is in the first element and is not a /
          held_spots = len(leader_name_split) - 1
          member_count += held_spots

      openings = c["club_max"] - member_count
      openingsStr = ""
      if openings <= 0:
        openingsStr = 'Full'
      else:
        openingsStr = openings
      #add club string for openings
      embed.add_field(name=clubStr, value=openingsStr, inline=True)

            
  return embed
