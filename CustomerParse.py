import json
import math
import os
import operator

class Customer:
    def __init__(self, customer):
        self.name = customer['name']
        self.userID = customer['user_id']
        self.latitude = customer['latitude']
        self.longitude = customer['longitude']
        self.radius = 6371.07103 #radius of the earth

    def getUserID(self):
        return self.userID

    # TODO: Add methods for returning Customer attributes

    # Calculate distance between Customer object and "end" coordinates on Earth's surface
    def calc_distance(self, end_latitude, end_longitude):
        lat = math.radians(float(self.latitude))
        lon = math.radians(float(self.longitude))
        cent_ang = math.acos(math.sin(lat)*math.sin(end_latitude) + math.cos(lat)*math.cos(end_latitude)*math.cos(abs(lon-end_longitude)))
        return self.radius * cent_ang

    # Customer object represented as a String of UserID and Name
    def __repr__(self):
        return "UserID:{0:<3} Name:{1}".format(self.userID, self.name)


class Party:
    def __init__(self, location_latitiude, location_longitude, invite_radius):
        self.location_lon = location_longitude
        self.location_lat = location_latitiude
        self.max_distance = invite_radius
        self.invite_list = []

    def getUserID(self, person):
        return person.userID

    # TODO: Add methods for returning Party attributes
    
    # TODO: Clean method
    def determine_invites(self):
        cfin = []
        with open("TestInputs/CustomerList.txt", "r") as file:
            customers = file.readlines()
            for line in customers:
                line = line.replace("latitude", "\"latitude\"")
                line = line.replace("name", "\"name\"")
                line = line.replace("user_id", "\"user_id\"")
                line = line.replace("longitude", "\"longitude\"")
                cfin.append(json.loads(line))

            for c in cfin:
                potential_invite = Customer(c)
                if potential_invite.calc_distance(self.location_lat, self.location_lon) <= self.max_distance:
                    self.invite_list.append(potential_invite)

    # Generate output file containing sorted guest list
    def generate_list(self):
        self.invite_list.sort(key=operator.attrgetter('userID')) # Sort in ascending UserID Order
        os.remove("InviteList.txt")
        file = open("InviteList.txt", "a+")
        file.write("{0:^25}".format("Invite List"))
        file.write("\n")
        for invitee in self.invite_list:
            file.write(str(invitee))
            file.write("\n")
        file.close

            


if __name__ == "__main__":
    location = [37.788802, -122.4025067]
    party = Party(math.radians(location[0]), math.radians(location[1]), 100)
    party.determine_invites()
    party.generate_list()
