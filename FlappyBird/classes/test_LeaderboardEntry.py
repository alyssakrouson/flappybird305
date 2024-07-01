from unittest import TestCase
from LeaderboardEntry import LeaderboardEntry


class TestLeaderboardEntry(TestCase):
    def test_update_score(self):
        entry = LeaderboardEntry("uid", "Joe", 88)
        entry.updateScore(99)
        assert entry.score == 99

    def test_update_nickname(self):
        entry = LeaderboardEntry("uid", "Joe", 88)
        entry.updateNickname("Sam")
        assert entry.nickname == "Sam"

    def test_lt(self):
        entry = LeaderboardEntry("uid", "Joe", 88)
        entry2 = LeaderboardEntry("uid", "Sally", 89)
        assert entry < entry2
        assert not entry > entry2
        assert not entry == entry2


    def test_gt(self):
        entry = LeaderboardEntry("uid", "Joe", 90)
        entry2 = LeaderboardEntry("uid", "Sally", 89)
        assert not entry < entry2
        assert entry > entry2
        assert not entry == entry2
    def test_eq(self):
        entry = LeaderboardEntry("uid", "Joe", 90)
        entry2 = LeaderboardEntry("uid", "Sally", 90)
        assert not entry < entry2
        assert not entry > entry2
        assert entry == entry2