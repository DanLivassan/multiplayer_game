import createKeyboardListener from './input.js'
import renderScreen from './renderer.js'

export function Player(playerId, positionX, positionY){
    return {
        playerId: playerId, 
        playerPosition: {
            positionX:positionX, 
            positionY:positionY
        }
    }
}

export function Fruit(fruitId, positionX, positionY){
    return {
        fruitId: fruitId, 
        fruitPosition: {
            positionX:positionX, 
            positionY:positionY
        }
    }
}
export function createGame(){
    var state = {
        me:{id:""},
        players:{},
        fruits:{},
        screen: {x:10, y:10}
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
        let keyPressed = command.keyPressed
        const moveFunctions = {
            "ArrowUp": ()=>{
                if (state.players[command.playerId].positionY>0) 
                    state.players[command.playerId].positionY-=1
            },
            "ArrowDown": ()=>{
                if (state.players[command.playerId].positionY<state.screen.y-1)
                    state.players[command.playerId].positionY+=1
            },
            "ArrowLeft": ()=>{
                if (state.players[command.playerId].positionX>0)
                    state.players[command.playerId].positionX-=1
            },
            "ArrowRight": ()=>{
                if (state.players[command.playerId].positionX<state.screen.x-1)
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
        const player = state.players[playerId]
        for (const fruitId in state.fruits){
            const fruit = state.fruits[fruitId]
            
            if (fruit.positionX == player.positionX && fruit.positionY == player.positionY){
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


