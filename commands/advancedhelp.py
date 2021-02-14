#check if the user wants the advanced help option
#return True if user wants adanced help
def getIfAdvancedHelp(msg):
  adv_help = None
  split_msg = msg.split(" ",1)
  if len(split_msg) > 1:
    adv_help = msg.split(" ",1)[1]
  
  if adv_help == "help":
    return True
  else:
    return False