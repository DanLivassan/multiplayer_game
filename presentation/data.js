screen_width = 10
screen_height = 10


function Player(playerId, positionX, positionY){
    return {
        playerId: playerId, 
        playerPosition: {
            positionX:positionX, 
            positionY:positionY
        }
    }
}

function Fruit(fruitId, positionX, positionY){
    return {
        fruitId: fruitId, 
        fruitPosition: {
            positionX:positionX, 
            positionY:positionY
        }
    }
}
function createGame(){
    state = {
        me:{id:""},
        players:{},
        fruits:{}
    }

    
    function addPlayer(player){
        state.players[player.playerId] = player.playerPosition
    }

    function addFruit(fruit){
        state.fruits[fruit.fruitId] = fruit.fruitPosition
    }

    function removePlayer(playerId){
        delete state.players[playerId]
    }

    function removeFruit(fruitId){
        delete state.fruits[fruitId]
    }

    function movePlayer(command){
        keyPressed = command.keyPressed
        const moveFunctions = {
            "ArrowUp": ()=>{
                if (state.players[command.playerId].positionY>0) 
                    state.players[command.playerId].positionY-=1
            },
            "ArrowDown": ()=>{
                if (state.players[command.playerId].positionY<9)
                    state.players[command.playerId].positionY+=1
            },
            "ArrowLeft": ()=>{
                if (state.players[command.playerId].positionX>0)
                    state.players[command.playerId].positionX-=1
            },
            "ArrowRight": ()=>{
                if (state.players[command.playerId].positionX<9)
                    state.players[command.playerId].positionX+=1
            } 
        }
        const moveFunction = moveFunctions[keyPressed]
        const player = state.players[command.playerId]
        if(moveFunction && player){
            moveFunction()
            checkPlayerAndFruitColision(command.playerId)
        } 
        
    }

    function checkPlayerAndFruitColision(playerId){
        console.log(playerId)
        const player = state.players[playerId]
        for (const fruitId in state.fruits){
            const fruit = state.fruits[fruitId]
            
            if (fruit.positionX == player.positionX && fruit.positionY == player.positionY){
                console.log(`${playerId} colides with ${fruitId}`)
                removeFruit(fruitId)
            }
        }
    }

    return { 
        movePlayer,
        addPlayer,
        addFruit,
        removeFruit,
        removePlayer,
        checkPlayerAndFruitColision,
        state 
    }
}

const game = createGame()
game.addPlayer(Player("player1", 4, 5))
game.addPlayer(Player("player2", 3, 3))
game.addFruit(Fruit("fruit1", 2, 2))
game.addFruit(Fruit("fruit2", 9, 6))
game.state.me.id = "player1"