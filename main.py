class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"My name is {self.name}. My team is {self.team}")


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, name):
        new_player = Player(name, self.name)
        self.players.append(new_player)

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                print(f"Player {player.name} is Removed")
                break

    def show_total_xp(self):
        total_xp = 0
        for player in self.players:
            total_xp += player.xp
        print(f"Our Team Total Xp is {total_xp}")

    def show_players(self):
        for player in self.players:
            player.introduce()


nico = Player(name="nico", team="Team X")
nico.introduce()

lynn = Player(name="lynn", team="Team Y")
lynn.introduce()

team_x = Team(name="Team X")
team_x.add_player(nico.name)

team_y = Team(name="Team Y")
team_y.add_player(lynn.name)

team_x.show_players()
team_y.show_players()

team_x.show_total_xp()
team_y.show_total_xp()

team_x.remove_player(nico.name)
team_x.show_players()

team_y.remove_player(lynn.name)
team_y.show_players()
