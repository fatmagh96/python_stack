class Player:
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.age = data_dict['age']
        self.position = data_dict['position']
        self.team = data_dict['team']

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Uncomment the line below to test
player_kevin = Player(kevin)


print(player_kevin.team)