const socket = io.connect('http://' + document.domain + ':' + location.port)
socket.on('connect', function () {
    socket.emit('connection_identification_event', {
        data: 'OKAY, connected'
    })

    window.onload = () => {
        document.getElementById('forward_dir').onclick = () => {
            socket.emit('change_direction', {
                direction: 'forward'
            })
        }
    }
})
