document.addEventListener("keydown", handleKeyDownEvent)

current_player_id = current_player_id
game_data = game_data
acceptedMoves = ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"]

const moveFunction = {
    "ArrowUp": ()=>{
        if (game_data.players[current_player_id].positionY>0) 
            game_data.players[current_player_id].positionY-=1
    },
    "ArrowDown": ()=>{
        if (game_data.players[current_player_id].positionY<9)
            game_data.players[current_player_id].positionY+=1
    },
    "ArrowLeft": ()=>{
        if (game_data.players[current_player_id].positionX>0)
            game_data.players[current_player_id].positionX-=1
    },
    "ArrowRight": ()=>{
        if (game_data.players[current_player_id].positionX<9)
            game_data.players[current_player_id].positionX+=1
    } 
}

function handleKeyDownEvent(event){
    if (acceptedMoves.includes(event.key))
        moveFunction[event.key]()
}