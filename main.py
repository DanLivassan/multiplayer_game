from aiohttp import web
from game import Game
import socketio

game = Game()

game.add_fruit("fruit1", 3, 4)
#game.add_fruit("fruit2", 6, 8)
game.add_player("player1", 3, 6)
game.add_player("player2", 2, 9)

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


async def index(request):
    """Serve the client-side application."""
    with open('./presentation/client.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.event
async def connect(sid, environ):
    await sio.emit('open_game', {'state': game.game_state_to_dict()})
    print("connect ", sid)


@sio.event
async def chat_message(sid, data):
    print("message ", data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


app.router.add_static('/', 'presentation')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)