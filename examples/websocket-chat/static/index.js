function update(message) {
    let output = document.querySelector('#output');
    let outer = document.createElement('div');
    let inner = document.createElement('div');
    inner.className = 'message';
    inner.appendChild(document.createTextNode(message));
    outer.appendChild(inner);
    output.appendChild(outer);
}

window.onload = function() {
    let userId = null;
    let socket = new WebSocket('ws://' + window.location.host + '/socket');

    socket.onmessage = function(evt) {
        let msg = JSON.parse(evt.data);
        if (msg.type === 'join') {
            userId = msg.id;
        } else if (msg.type === 'msg') {
            let name = msg.id === userId ? 'you' : 'human' + msg.id;
            update(name + ': ' + msg.msg);
        }
    };

    let inputForm = document.querySelector('#input-form');
    let inputText = document.querySelector('#input-text');
    inputForm.onsubmit = function(evt) {
        evt.preventDefault();
        let msg = inputText.value;
        inputText.value = '';
        socket.send(msg);
        setTimeout(() => inputText.focus(), 0);
    };
    inputText.focus();
};
