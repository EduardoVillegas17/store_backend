import pymongo
import certifi

con_str = "mongodb+srv://eduardovillegas12:estableco0912@cluster0.a8r29.mongodb.net/?retryWrites=true&w=majority"


client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())


db = client.get_database("OrganikaStore")

