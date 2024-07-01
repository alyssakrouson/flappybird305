from classes.LeaderboardEntry import LeaderboardEntry
from classes.LeaderboardGlobal import LeaderboardGlobal
from classes.LeaderboardStorage import LeaderBoardStorage

class LeaderboardDisplay:
    def __init__(self):
        # Get score from file
        storage = LeaderBoardStorage()
        # Get score
        entry = storage.ReadScore()

        # Open connection to global leaderboard
        leaderboard = LeaderboardGlobal()

