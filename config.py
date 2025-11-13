
import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "24037760"))
    API_HASH = os.environ.get("API_HASH", "dccc3070f1c12ab155011f14c3d6ae6a")
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://gohilkanubhai1980:wZMjeJxxBPeu0VOn@cluster0.sbyxs3i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_USERS = [8458169280]


