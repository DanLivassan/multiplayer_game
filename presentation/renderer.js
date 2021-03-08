export default function renderScreen(context, state, requestAnimationFrame, currentPlayerId){  
    
    clearScreen(context)
    renderObjetcs(state.fruits, "green", context)
    renderObjetcs(state.players, "black", context)
    
    function clearScreen(context){
        const screen_width = 10
        const screen_height = 10
        context.clearRect(0, 0, state.screen.x, state.screen.y)
    }
    function renderObjetcs(objects, color, context){
        
        for (const objectId in objects){
            let object = objects[objectId]
            if (objectId!=currentPlayerId){

                renderPixel(color, {X: object.positionX, Y: object.positionY}, context)
            }
            else{
                renderPixel("yellow", {X: object.positionX, Y: object.positionY}, context)
            }
                
        }
    }
    
    function renderPixel(color, position, context){
        context.fillStyle = color
        context.fillRect(position.X, position.Y, 1,1)
    }
    requestAnimationFrame(()=>{
        renderScreen(context, state, requestAnimationFrame, currentPlayerId)
    })
}

