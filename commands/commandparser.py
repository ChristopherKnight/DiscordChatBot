import commands.helpcommand as hc
import commands.clubconquest as cq
import commands.members as mem
import commands.openings as op
import commands.ability as ab

#check which type of command it is
def checkcommands(message, client):
  message_type = None

  #find which message type is being asked for
  if message.content.startswith(hc.HELP_COMMAND):
    message_type = hc
  elif message.content.startswith(cq.CQ_COMMAND):
    message_type = cq
  elif message.content.startswith(mem.MEMBERS_COMMAND):
    message_type = mem
  elif message.content.startswith(op.OPENINGS_COMMAND):
    message_type = op
  elif message.content.startswith(ab.ABILITY_COMMAND):
    message_type = ab

  #get the response message the bot should say based on the command issued
  if message_type is not None:
    if message_type == ab:
      return message_type.getResponseMessage(message, client)
    else:
      return message_type.getResponseMessage(message)