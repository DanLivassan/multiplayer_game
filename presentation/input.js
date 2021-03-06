keyboard_listener = createKeyboardListener()
keyboard_listener.subscribe(game.movePlayer)
function createKeyboardListener(){

    const state = {
        observers: []
    }

    function subscribe(observerFunction){
        state.observers.push(observerFunction)
    }

    function notifyAll(command){
        for (const observerFunction of state.observers){
            observerFunction(command)
        }
    }
    document.addEventListener("keydown", handleKeyDownEvent)
    

    function handleKeyDownEvent(event){
        command = {keyPressed:event.key, playerId:game.state.me.id}
        notifyAll(command)
    }

    return {
        subscribe
    }
}

