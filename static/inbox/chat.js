const id = JSON.parse(document.getElementById('json-username').textContent);

const message_username = JSON.parse(document.getElementById('json-message-username').textContent);

const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + id
    + '/'
)

socket.onopen = function (e) {
    console.log("CONNECTION ESTABLISHED")
}

socket.onclose = function (e) {
    console.log("CONNECTION lOST");
}

socket.onerror = function (e) {
    console.log(e);
}

socket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.username == message_username) {
        document.querySelector('#chat-body').innerHTML += `<div class="flex mb-4 cursor-pointer">
            <div class="flex max-w-96 bg-red-100 rounded-lg p-3 gap-3">
                <p class="text-gray-700"> ${data.message}</p>

        </div>`

    } else {
        document.querySelector('#chat-body').innerHTML += `<div class="flex justify-end mb-4 cursor-pointer">
        <div class="flex max-w-96 bg-indigo-500 text-white rounded-lg p-3 gap-3">
            <p class="text-gray-700"> ${data.message}</p>

    </div>`
    }
}



document.querySelector('#chat-message-submit').onclick = function (e) {
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;

    socket.send(JSON.stringify({
        'message': message,
        'username': message_username
    }));
    message_input.value = '';
}

