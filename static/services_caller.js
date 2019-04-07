const changeDirection = (direction) => {
    const Http = new XMLHttpRequest()
    const url = `/api/change-movement?direction=${direction}`
    Http.open('POST', url)
    Http.send()

    Http.onreadystatechange = (e) => {
        console.log(Http.responseText)
    }
}

