import commands.helpcommand as hc

#check which type of command it is
def checkcommands(message):
  message_type = None

  #find which message type is being asked for
  if message.content.startswith(hc.HELP_COMMAND):
    message_type = hc
  
  #get the response message the bot should say based on the command issued
  if message_type is not None:
    return message_type.getResponseMessage(message.content)