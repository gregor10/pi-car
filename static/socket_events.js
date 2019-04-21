const socket = io.connect('http://' + document.domain + ':' + location.port)

const changeDirectionEmitFunction = (direction) => {
    socket.emit('change_direction', { direction })
}

socket.on('connect', () => {
    socket.emit('connection_identification_event', {
        data: 'OKAY, connected'
    })

    const directions = ['forward_dir', 'left_dir', 'stop_dir', 'right_dir', 'backward_dir']

    directions.forEach((direction) => {
        const element = document.getElementById(direction)
        element.onmousedown = () => {
            changeDirectionEmitFunction(direction.replace('_dir', ''))
        }

        element.onmouseup = () => {
            changeDirectionEmitFunction('stop')
        }
    })
})

socket.on('disconnect', () => {
    console.log('DISCONNECT EVENT!', socket)
})
