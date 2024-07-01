import json
import os.path
from classes.LeaderboardEntry import LeaderboardEntry

class LeaderboardStorage:
    def __init__(self):
        self.filename = "score.json"

    def SaveScore(self, entry):
        file_object = open(self.filename, 'w+')
        jsondata = {}
        jsondata['uid'] = entry.uid
        jsondata['nickname'] = entry.nickname
        jsondata['score'] = entry.score
        file_object.write(json.dumps(jsondata, indent=4))
        file_object.close()

    def ReadScore(self) -> LeaderboardEntry:
        entry = None
        if os.path.isfile(self.filename):
            file_object = open(self.filename, 'a+')
            file_object.seek(0)
            dict = json.load(file_object)
            entry = LeaderboardEntry(dict["nickname"], dict["uid"], dict["score"])
            file_object.close()
        return entry
