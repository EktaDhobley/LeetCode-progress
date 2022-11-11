class Leaderboard:

    def __init__(self):
        #playerId : score
        self.scoreboard = defaultdict()
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scoreboard:
            self.scoreboard[playerId] += score
        else:
            self.scoreboard[playerId] = score

    def top(self, K: int) -> int:
        return sum(sorted(self.scoreboard.values(), reverse=True)[:K])
        # scoreboard = sorted(self.scoreboard.items(), key = operator.itemgetter(1), reverse = True)
        # res = []
        # i = 0
        # while i < K:
        #     res.append(scoreboard.pop())
        #     i += 1

    def reset(self, playerId: int) -> None:
        self.scoreboard[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)