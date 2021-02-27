import requests as r

class User():
    def __init__(self, teleg_id):
        self.id = teleg_id

    @property
    def is_new(): # does user with that telegram id exists?
        pass

    def get_presents_list(): # get user's presents list from db
        pass

    def get_new_present(): # randomly pick present according to the last pay sum, save in db
        pass
