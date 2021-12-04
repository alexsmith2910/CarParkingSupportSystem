from src.database.database import DatabaseClient
from datetime import datetime

from src.models.card import CardAccess


test = DatabaseClient("Users")
test2 = DatabaseClient("Tickets")
test3 = DatabaseClient("Users")

print(f"{test == test3}")  # checking to see if the cache was reloaded into test3 from test
print(test._loaded)  # testing __new__ in DatabaseClient

user = {"ticketID": "1234-1234", "time_of_entry": datetime.now(), "has_card": True,
        "time_of_exit": datetime.now(), "card": CardAccess("1234-1234").to_readable()}
user2 = {"ticketID": "1234-1234-1234", "time_of_entry": datetime.now(), "has_card": False}

test.insert_one(user)   # testing inserts for different DatabaseClient's
test3.insert_one(user2)

test2.insert_many([{"ticketID": user["ticketID"]}, {"ticketID": user2["ticketID"]}])

print(test.find_one({"ticketID": "1234-1234"}))  # testing searches for different DatabaseClient's
print(test2.find_one({"ticketID": "1234-1234"}))

for data in test.find({"time_of_entry": datetime.fromisoformat("2021-12-03T15:40:02.587+00:00")}):
    print(data)
