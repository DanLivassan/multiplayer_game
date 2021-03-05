const screen = document.getElementById("screen")
const context  = screen.getContext("2d")

renderScreen()
function renderScreen(){
    clearScreen()
    renderObjetcs(game_data.players, "black")
    renderObjetcs(game_data.fruits, "green")
    requestAnimationFrame(renderScreen)
}

function clearScreen(){
    context.clearRect(0, 0, screen_width, screen_height)
}
function renderObjetcs(objects, color){
    for (const objectId in objects){
        let object = objects[objectId]
        renderPixel(color, {X: object.positionX, Y: object.positionY})
    }
}

function renderPixel(color, position){
    context.fillStyle = color
    context.fillRect(position.X, position.Y, 1,1)
}