class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f'Player {self.name} is already in the guild.'

        if player.guild != self.name and player.guild != 'Unaffiliated':
            return f'Player {self.name} is in another guild.'

        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player):
        for player in self.players:
            if player.name == player.name:
                self.players.remove(player)
                player.guild = 'Unaffiliated'
                return f'Player {player} has been removed from the guild.'

        return f'Player {player} is not in the guild.'

    def guild_info(self):
        result = f'Guild: {self.name}'

        for player in self.players:
            result += '\n'
            result += player.player_info()

        return result

