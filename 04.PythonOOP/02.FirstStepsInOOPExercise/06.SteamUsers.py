class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.playeed_hours = 0

    def play(self, game, hours):
        if game not in self.games:
            return f"{game} is not in library"
        self.playeed_hours += hours
        return f"{self.username} is playing {game}"


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
