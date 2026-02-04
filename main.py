# person = {"name": "Nico", "xp": 1000, "team": "Team X"}


def create_player(name, xp, team):
    return {"name": name, "xp": xp, "team": team}


def introduct_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")


person = create_player("nico", 1500, "Team Y")
introduct_player(person)
