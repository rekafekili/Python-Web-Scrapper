# Dictionary

player = {"name": "nico", "age": 12, "alive": True, "fav_food": ["Pizza", "Hamburger"]}

print(player)
print(player.keys())
print(player.values())
print(player.items())
print(player.get("name"))
print(player.get("fav_movie"))
print(player["fav_food"])

player.pop("age")
print(player)

player["age"] = 12
print(player)

player["fav_food"].append("Noodles")
print(player)
