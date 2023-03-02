class Guild():

    def __init__(self, name):
        self.gild_name = name
        self.players = []

    def assign_player(self, player):
        if player.guild != self.gild_name and player.guild == "Unaffiliated":
            if player.guild != self.gild_name:
                player.guild = self.gild_name
                self.players.append(player)

                return f"Welcome player {player.name} to the guild {self.gild_name}"
            else:
                return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        try:
            player = next(filter(lambda p:p == player_name, self.players))

        except StopIteration:
            return f"Player {player_name} is not in the guild."

        if player in self.players:
            player_name.guild = "Unaffiliated"
            self.players.remove(player_name)

            return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        info = [f'Guild: {self.gild_name}\n']
        for player in self.players:
            info.append(player.player_info())
        return ''.join(info)

