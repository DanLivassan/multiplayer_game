from models import GameObjectBuilder
import constants


class Game:
    def __init__(self):
        self.state = {
            "players": [],
            "fruits": [],
        }

    def add_player(self, player_id, position_x, position_y):
        self.state["players"].append(GameObjectBuilder.makeObject(constants.PLAYER, player_id, position_x, position_y))

    def add_fruit(self, fruit_id, position_x, position_y):
        self.state["fruits"].append(GameObjectBuilder.makeObject(constants.FRUIT, fruit_id, position_x, position_y))

    def remove_fruit(self, fruit_id: str):
        fruit = (next(item for item in self.state["fruits"] if item.fruit_id == fruit_id))
        self.state["fruits"].remove(fruit)

    def remove_player(self, player_id: str):
        player = (next(item for item in self.state["players"] if item.fruit_id == player_id))
        self.state["players"].remove(player)

    def game_state_to_dict(self):
        game_state_dict = {
            "players": [player.to_dict() for player in self.state["players"]],
            "fruits": [fruit.to_dict() for fruit in self.state["fruits"]]}
        return game_state_dict


