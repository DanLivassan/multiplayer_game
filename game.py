from models import GameObjectBuilder
import constants
import asyncio


class Command:
    pass


class Game:
    def __init__(self):
        self.observers = []
        self.state = {
            "players": [],
            "fruits": [],
        }

    async def notify_all(self, command):

        for observerFunction in self.observers:
            await observerFunction(command)

    def subscribe(self, observer_function):
        self.observers.append(observer_function)

    async def move_player(self, move, player_id):
        player = next(item for item in self.state["players"] if item.player_id == player_id)
        if move in constants.MAP_ARROW:
            player.move_object(move)
            await self.notify_all({"type": "move_player", "state": self.game_state_to_dict()})

    async def add_player(self, player_id, position_x, position_y):
        self.state["players"].append(GameObjectBuilder.makeObject(constants.PLAYER, player_id, position_x, position_y))
        await self.notify_all({"type": "add_player", "state": self.game_state_to_dict()})

    async def add_fruit(self, fruit_id, position_x, position_y):
        self.state["fruits"].append(GameObjectBuilder.makeObject(constants.FRUIT, fruit_id, position_x, position_y))
        await self.notify_all({"type": "add_fruit", "state": self.game_state_to_dict()})

    async def remove_fruit(self, fruit_id: str):
        fruit = (next(item for item in self.state["fruits"] if item.fruit_id == fruit_id))
        self.state["fruits"].remove(fruit)
        await self.notify_all({"type": "remove_player", "state": self.game_state_to_dict()})

    async def remove_player(self, player_id: str):
        player = (next(item for item in self.state["players"] if item.player_id == player_id))
        self.state["players"].remove(player)
        await self.notify_all({"type": "remove_player", "state": self.game_state_to_dict()})

    def game_state_to_dict(self):
        game_state_dict = {
            "players": [player.to_dict() for player in self.state["players"]],
            "fruits": [fruit.to_dict() for fruit in self.state["fruits"]]}
        return game_state_dict

