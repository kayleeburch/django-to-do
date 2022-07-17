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
            window.location.replace("http://localhost:8000/all_todos")

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
            window.location.replace("http://localhost:8000/all_todos/")

        })
        .catch((error) => {
            console.log('ERROR')
            console.log(error)
        })

}

function signup() {
    console.log('signup function called')
    const email = document.getElementById('email').value
    const password = document.getElementById('password').value

    axios
        .post('http://localhost:8000/signup/', {
            email: email,
            password: password
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

function login() {
    console.log('login function called')
    const email = document.getElementById('email').value
    const password = document.getElementById('password').value

    axios
        .post('http://localhost:8000/login/', {
            email: email,
            password: password
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