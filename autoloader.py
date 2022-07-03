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

class Autoloader():
    def __init__(self, url=None):
        self.url = url
        self.lb_filename = '.lb_store'
        config_file = open('.config', 'rb')
        self.config = pickle.load(config_file)
        config_file.close()
        self.aoc_url = 'https://adventofcode.com/'
        self.leader_url = '/leaderboard/private/view/418907.json'

    def print_data(self):
        print(f"Url = {self.url}")

    def fetch(self, url=None):
        if url == None:
            url = self.url
        r = self.session.get(url)
        self.data = r.text
        return self.data

    def connect(self):
        aocauthurl = 'https://adventofcode.com/auth/github'
        ghauthurl = 'https://github.com/session'
        payload = {'login':self.config['github_user'], 'password':self.config['github_pass'], 'commit':'Sign in', 'utf8':'%E2%9C%93'}
        session = requests.Session()
        ghresponse = session.get(ghauthurl)
        soup = BeautifulSoup(ghresponse.text, 'html5lib')
        payload['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']

        ghresponse = session.post(ghauthurl, data=payload)
        s = session.get(aocauthurl)
        self.session = session

    def aoc_parser(self, mode='Auto'):
        if mode == 'Auto':
            if len(self.data.splitlines()) > 1:
                mode = 'lines'
            else:
                mode = 'string'
        if mode == 'lines':
            return self.aoc_line_parse()
        elif mode == 'string':
            return self.aoc_str_parse()

    def get_leaderboard(self, year):
        j = self.session.get(self.aoc_url+year+self.leader_url)
        t = time.time()
        js = j.json()
        self.lbs[year] = (t, js['members'])
        lb_file = open(self.lb_filename, "wb")
        pickle.dump(self.lbs, lb_file)
        lb_file.close()
        
    def check_leaderboard(self, year):

        lb_file = open(self.lb_filename, 'rb')
        self.lbs = pickle.load(lb_file)
        lb_file.close()

        if year not in self.lbs:
            self.get_leaderboard(year)
        elif time.time() - self.lbs[year][0] > 900:
            self.get_leaderboard(year)

        return self.lbs[year][1]
        


