# from os import getenv
# from dotenv import load_dotenv

# #Necessary Variables 
# API_ID = int(getenv("API_ID", 23476439))
# API_HASH = getenv("API_HASH", "1626e884119a29dbccbb78e39b48128f")
# BOT_TOKEN = getenv("BOT_TOKEN", "6240917464:AAGR6qb3pqzYnX56leySXRyNomsUc1AypB4") #Put your bot token here
# CHANNEL = getenv("CHANNEL", "bot_list_hub") #Your public channel username without @ for force subscription.
# MONGO = getenv("MONGO", "mongodb+srv://new-user_31:new-user_31@cluster0.pn0nyyu.mongodb.net/") #Put mongo db url here
# #Optional Variables
# OWNER_ID = int(getenv("OWNER_ID", 5446536405)) #Go to @ThunderrXbot and type /id and put that value here. 
# FSUB = bool(getenv("FSUB", True)) #Set this True if you want to enable force subscription from users else set to False.
from os import getenv
from dotenv import load_dotenv

#Necessary Variables 
API_ID = int(getenv("API_ID", 29400566))
API_HASH = getenv("API_HASH", "8fd30dc496aea7c14cf675f59b74ec6f")
BOT_TOKEN = getenv("BOT_TOKEN", '6240917464:AAGR6qb3pqzYnX56leySXRyNomsUc1AypB4') #Put your bot token here
CHANNEL = getenv("CHANNEL", "bot_list_hub") #Your public channel username without @ for force subscription.
MONGO = getenv("MONGO", 'mongodb+srv://new-user_31:new-user_31@cluster0.pn0nyyu.mongodb.net/') #Put mongo db url here
#Optional Variables
DELAY = int(getenv("DELAY", 600)) #Delay in secondsbefore join request should be accepted default to 10 minutes
OWNER_ID = int(getenv("OWNER_ID", 5446536405)) #Go to @ThunderrXbot and type /id and put that value here. 
FSUB = bool(getenv("FSUB", False)) #Set this True if you want to enable force subscription from users else set to False.
