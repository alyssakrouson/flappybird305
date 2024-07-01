import requests
import json
from LeaderboardEntry import LeaderboardEntry
from classes.LeaderboardStorage import LeaderBoardStorage


class LeaderboardGlobal:
    def __init__(self):
        # Get Bearer token for further requests
        URL = "https://api.globalstats.io/oauth/access_token"
        # Normally this would not be good practice to include on the GitHub repository.
        params = {'grant_type': 'client_credentials', 'scope': 'endpoint_client', 'client_id': 'NymW9lKYZNc80yaYcXFiZmYPwz7y1cAPLXMViwTh',  'client_secret': '6plFAkRyZaxm8nSIvrKI2AtZmphTizdpZy5zSW8S'}
        r = requests.post(URL, data=params)
        self.bearer = r.json()['access_token']

    def addScore(self, entry: LeaderboardEntry):
        jsondata = {}
        values = {}
        values['score'] = entry.score
        jsondata['values'] = values
        jsondata['name'] = entry.nickname
        URL = "https://api.globalstats.io/v1/statistics"
        verb = "POST"
        params = {'Authorization': 'Bearer ' + self.bearer, 'Accept': 'application/json'}
        if entry.uid is not None:
            URL += "/" + entry.uid
            verb = "PUT"
        r = requests.request(verb, URL, headers = params, json=jsondata)
        print(r.json())
        print(json.dumps(jsondata))
        if entry.uid is None:
            entry.uid = r.json()['_id']
    def getSurrounding(self, entry:LeaderboardEntry):
        URL = "https://api.globalstats.io/v1/statistics/" + entry.uid + "/section/score"
        verb = "GET"
        params = {'Authorization': 'Bearer ' + self.bearer, 'Accept': 'application/json'}
        r = requests.request(verb, URL, headers = params)
        return r.json()
    def getTopTen(self):
        jsondata = {}
        jsondata['limit'] = 2
        URL = "https://api.globalstats.io/v1/gtdleaderboard/score"
        verb = "POST"
        params = {'Authorization': 'Bearer ' + self.bearer, 'Accept': 'application/json'}
        r = requests.request(verb, URL, headers=params, json=jsondata)
        return r.json()

