import time
from uuid import uuid4
from datetime import datetime

from src.models.user import User
from src.database.database import DatabaseClient


def main():
    testUser = User(str(uuid4()), datetime.now(), False)

    usersDB = DatabaseClient("Users")
    testUserFromDB = User.load_from_database(usersDB.find_one({"ticketID": "1234-1234"}))

    print(testUserFromDB.get_duration())

    time.sleep(5)

    testUser.time_of_exit = datetime.now()
    print(testUser.get_duration())


if __name__ == '__main__':
    main()
