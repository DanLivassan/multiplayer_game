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


game = Game()

game.add_fruit("fruit1", 3, 4)
game.add_fruit("fruit2", 6, 8)
game.add_player("player1", 3, 6)
game.add_player("player2", 2, 9)




