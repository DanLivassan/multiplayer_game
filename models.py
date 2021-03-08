import constants


def move_left(state):
    if state["x"] > 0:
        state["x"] -= 1
    return state


def move_right(state):
    if state["x"] < 9:
        state["x"] += 1
    return state


def move_up(state):
    if state["y"] > 0:
        state["y"] -= 1
    return state


def move_down(state):
    if state["y"] < 9:
        state["y"] += 1
    return state


moveFunctions = {
    "LEFT": lambda state: move_left(state),
    "RIGHT": lambda state: move_right(state),
    "UP": lambda state: move_up(state),
    "DOWN": lambda state: move_down(state)
}
"""
state = {"x": 4, "y": 4}
for i in range(10):
    state = moveFunctions["RIGHT"](state)
    print(state)
"""


class GameObject:

    def move_object(self, move):
        self.position = moveFunctions[move](self.position)


class Fruit(GameObject):
    def __init__(self, fruit_id: str, position_x: int, position_y: int):
        self.fruit_id = fruit_id
        self.object_type = constants.FRUIT
        self.color = constants.COLORS[constants.FRUIT]
        self.position = {"x": position_x, "y": position_y}

    def to_dict(self):
        return {
            "FruitId": self.fruit_id,
            "color": self.color,
            "FruitPosition": {
                "positionX": self.position["x"],
                "positionY": self.position["y"]
            }

        }


class Player(GameObject):
    def __init__(self, player_id: str, position_x: int, position_y: int):
        self.player_id = player_id
        self.object_type = constants.PLAYER
        self.color = constants.COLORS[constants.PLAYER]
        self.position = {"x": position_x, "y": position_y}

    def to_dict(self):
        return {
            "PlayerId": self.player_id,
            "color": self.color,
            "PlayerPosition": {
                "positionX": self.position["x"],
                "positionY": self.position["y"]
            }

        }


class GameObjectBuilder:
    @staticmethod
    def makeObject(object_type: str, object_id: str, position_x: int, position_y: int) -> GameObject:
        if object_type == constants.PLAYER:
            return Player(object_id, position_x, position_y)
        elif object_type == constants.FRUIT:
            return Fruit(object_id, position_x, position_y)
