from os import environ 

class Config:
    API_ID = environ.get("API_ID", "20937822")
    API_HASH = environ.get("API_HASH", "68d3b463d3c53536782545f790aa5147")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7074426603:AAEsb_Lh0wUeBcgR-XUSZAClCvcJ6656jTw") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://anmol:anmol@cluster0.sikg9g9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1663603208').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
