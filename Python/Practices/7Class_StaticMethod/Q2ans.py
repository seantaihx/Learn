'''
Create a class User with a class variable user_count.
	•	Add a @classmethod called create_guest() that returns a user with name "Guest" and increases user_count.
 '''

class User:
    user_count = 0  # Class variable to track number of users

    def __init__(self, name):
        self.name = name
        User.user_count += 1

    @classmethod
    def create_guest(cls):
        return cls("Guest")
