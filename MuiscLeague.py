import requests
import pickle
import time
import math

class theme():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.votes = 0
        return self

    def get_votes(self):
        return self.votes
    

class musicleague():
    def __init__(self, config_path=0):
        if config_path == 0:
            self.themeList = []
            return self
        try:
            config = open(config_path, "rb")
            themes = open(config["themes_path"], "rb")
            self.themeList = pickle.load(themes)
            
    def test_setup(self):
        for ii in range(4):
            self.themeList.add(theme(ii, f"the concept of {math.random(ii)}"))

    def get_cur_themes(self):
        return self.themeList
