class leaderboard():
    def __init__(self):
        self.scores = []
    def addScore(self, score):
        self.scores.append(score)
    def getScore(self):
        #Return scores in order from highest to lowest
        return []