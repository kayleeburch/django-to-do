console.log('js being reached')

function add_item() {
    console.log('function called!')
    const title = document.getElementById('title').value
    const body = document.getElementById('body').value

    axios
        .post('', {
            title: title,
            body: body
        })
        .then((response) => {
            console.log('this is the response')
            console.log(response)
            window.location.replace("http://localhost:8000/")

        })
        .catch((error) => {
            console.log('ERROR')
            console.log(error)
        })
}

function update_item() {
    console.log('update item function called')
    const title = document.getElementById('title').value
    const body = document.getElementById('body').value

    axios
        .post('', {
            title: title,
            body: body
        })
        .then((response) => {
            console.log('this is the response')
            console.log(response)

        })
        .catch((error) => {
            console.log('ERROR')
            console.log(error)
        })

}