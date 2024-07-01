class LeaderboardEntry:

    def __init__(self, nickname, uid, score: int):
        """Creates a new LeaderBoardEntry. Such LeaderBoardEntry can be created upon interaction with the
        globalstats.io API. For new players, it is necessary to get a UID before creating the score."""
        self.nickname = nickname
        self.uid = uid
        self.score = score
    def updateScore(self, score: int):
        """Updates a given score value"""
        self.score = score

    def updateNickname(self, nickname):
        """Updates the nickname in the leaderboardentry"""
        self.nickname = nickname

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score

