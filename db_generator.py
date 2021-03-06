from xmlrpc.client import DateTime
from website.models import *
import random
import string
import datetime


class DBGenerator():
    def __init__(self):
        self.db = DBConnection()
        self.users = []

    def cleanDB(self):
        self.db._engine.drop_all()
        self.db._engine.create_all()

    def createDB(self):
        self.createRoles()
        self.createProfiles()
        self.createUsers()
        
    def randomHash(self,size):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

    def createRoles(self):
        self.db.session.add(UserRole(name=UserRole.MEMBER))
        self.db.session.add(UserRole(name=UserRole.ADMIN))

    def createProfiles(self):
        profile1 = UserProfile(firstname = "Ludzie", last_name = "Kowalski",
                                date_of_birth = datetime.datetime.now(), age = 22,
                                gender = "Male", nationality = "Poland", avatarName = "user")
        profile2 = UserProfile(firstname = "Adrian", last_name = "Forest",
                                date_of_birth = datetime.datetime.now(), age = 22,
                                gender = "Male", nationality = "Poland", avatarName = "user")
   
        self.db.AddProfile(profile1)
        self.db.AddProfile(profile2)

    def createUsers(self):
        i = 1
        usernames = ["Adam","Mike","Olivia"]
        for user in usernames:
            user = User(username = user, email = user + "@box.com", 
                    passwordHash = self.randomHash(60), roleId = 1, profileId = 1)
            self.db.AddUser(user)
            i+=1
            self.users.append(user)

        admin1 = User(username="admin", email = "adminbor@bor.com", 
                password = "Cola4000!",
                roleId = 2, profileId = 2)

        self.db.AddUser(admin1)
        self.users.append(admin1)
        self.db.Flush()

if __name__ == "__main__":
    generator = DBGenerator()
    generator.cleanDB()
    generator.createDB()