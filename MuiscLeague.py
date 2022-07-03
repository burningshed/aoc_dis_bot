import requests
import pickle
import time
from bs4 import BeautifulSoup
class theme():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.votes = 0
        return self

    def get_votes(self):
        return self.votes
    

class musicleague():
    def __init__(self):
        self.themeList = []

    def test_setup(self):
        for ii in range(4):
            self.themeList.add(theme(ii, f"the concept of {ii}"))

    def get_cur_themes(self):
        return self.themeList
