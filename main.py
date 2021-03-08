from aiohttp import web
from game import Game
from random import randint
import constants
import socketio

game = Game()
sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)




async def index(request):

    """Serve the client-side application."""

    with open('./presentation/client.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.event
async def connect(sid, environ):
    await game.add_fruit("fruit1", randint(0, 9), randint(0, 9))
    await game.add_player(sid, randint(0, 9), randint(0, 9))
    print("connect ", sid)


@sio.event
async def chat_message(sid, data):
    print("message ", data)


@sio.on("move_player")
async def move_player(sid, data):
    if "move" in data:
        move = data["move"]
        player_id = data["playerId"]
        await game.move_player(move, player_id)


@sio.on("colision")
async def move_player(sid, data):
    await game.remove_fruit(data["fruitId"])


@sio.event
async def disconnect(sid):
    await game.remove_player(sid)
    print('disconnect ', sid)


@sio.event
async def send_state_to_frontend(state):
    await sio.emit('load_game', {'state': state["state"]})

game.subscribe(send_state_to_frontend)


app.router.add_static('/', 'presentation')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)