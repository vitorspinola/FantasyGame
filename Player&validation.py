import bcrypt
import pickle
import time

class Player:
    def __init__(self, name, login, password, points=0):
        self.name = name
        self.login = login
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.points = points

    def add_points(self, amount):
        self.points += amount

    def remove_points(self, amount):
        self.points -= amount

	
    def validate_credentials(self, login, password):
        if self.login == login and bcrypt.checkpw(password.encode('utf-8'), self.password):
            return True
        else:
            return False

def save_players(players):
	with open("players.pickle", "wb") as f:
		pickle.dump(players, f)

def load_players():
	with open("players.pickle", "rb") as f:
		return pickle.load(f)

def auto_save(players, interval):
    while True:
        time.sleep(interval)
        save_players(players)


