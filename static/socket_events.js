const socket = io.connect('http://' + document.domain + ':' + location.port)

const changeDirectionEmitFunction = (direction) => {
    socket.emit('change_direction', { direction })
}

socket.on('connect', () => {
    socket.emit('connection_identification_event', {
        data: 'OKAY, connected'
    })

    window.onload = () => {
        ['forward_dir', 'left_dir', 'stop_dir', 'right_dir', 'backward_dir']
            .forEach((direction) => {
                document.getElementById(direction).onclick = () => {
                    changeDirectionEmitFunction(direction.replace('_dir', ''))
                }
            })
    }
})

socket.on('disconnect', () => {
    console.log('DISCONNECT EVENT!', socket)
})
