const socket = io.connect('http://' + document.domain + ':' + location.port)

const changeDirectionEmitFunction = (direction) => {
    socket.emit('change_direction', { direction })
}

socket.on('connect', () => {
    socket.emit('connection_identification_event', {
        data: 'OKAY, connected'
    })

    const directions = [
        'forward_dir',
        'forward_left_dir',
        'forward_right_dir',
        'left_dir',
        'stop_dir',
        'right_dir',
        'backward_dir',
        'backward_left_dir',
        'backward_right_dir'
    ]

    directions.forEach((direction) => {
        const element = document.getElementById(direction)
        element.addEventListener('pointerdown', () => {
            changeDirectionEmitFunction(direction.replace('_dir', ''))
        })

        element.addEventListener('pointerup', () => {
            changeDirectionEmitFunction('stop')
        })
    })


    const angles = { 'rotate_left': 180, 'rotate_front': 90, 'rotate_right': 0 }
    Object.keys(angles).forEach((key) => {
        const element = document.getElementById(key)
        const angle = angles[key]

        element.onclick = () => {
            socket.emit('change_camera_angle', { angle })
        }
    })
})

socket.on('ultrasonic_distance', (data) => {
    console.log('Ultrasonic', data)
    if ('distance' in data) {
        document.getElementById('distance_tracker').innerHTML = `Distance ${data.distance} cm`
    }

})

socket.on('disconnect', () => {
    console.log('DISCONNECT EVENT!', socket)
})
