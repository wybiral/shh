let socket;

const update = (msg, className) => {
    const log = document.getElementById('log');
    const outer = document.createElement('div');
    const inner = document.createElement('div');
    outer.className = className;
    inner.innerText = msg;
    outer.appendChild(inner);
    const scroll = log.scrollTop > log.scrollHeight - log.clientHeight - 1;
    log.appendChild(outer);
    if (scroll) {
        log.scrollTop = log.scrollHeight - log.clientHeight;
    }
    return outer;
}

const connect = () => {
    let userId = null;
    const connecting = update('Connecting...', 'info').querySelector('div');
    socket = new WebSocket('ws://' + window.location.host + '/socket');
    socket.onopen = evt => {
        connecting.innerText = 'You are now connected.';
    };
    socket.onclose = evt => {
        connecting.innerText = 'Disconnected.';
        setTimeout(connect, 15);
    };
    socket.onmessage = evt => {
        let msg = JSON.parse(evt.data);
        switch (msg.type) {
            case 'welcome':
                userId = msg.id;
                update('You are ' + userId + '.', 'info');
                break;
            case 'join':
                update(msg.id + ' has joined.', 'info');
                break;
            case 'leave':
                update(msg.id + ' has left.', 'info');
                break;
            case 'name':
                if (msg.old == userId) {
                    update('You are now ' + msg.new, 'info');
                    userId = msg.new;
                } else {
                    update(msg.old + ' is now ' + msg.new, 'info');
                }
                break;
            case 'msg':
                let className = 'msg';
                if (msg.id == userId) {
                    className += ' self';
                }
                update(msg.id + ': ' + msg.body, className);
                break;
            case 'list':
                update('Currently online: ' + msg.ids.join(', '), 'info');
                break;
        }
    };
};

window.onload = () => {
    connect();
    const form = document.getElementById('form');
    const input = document.getElementById('input');
    form.onsubmit = evt => {
        evt.preventDefault();
        const msg = input.value.trim();
        input.value = '';
        if (msg.startsWith('/')) {
            const parts = msg.split(' ');
            if (parts[0] == '/nick') {
                socket.send(JSON.stringify({type: 'name', id: parts[1]}));
            } else if (parts[0] == '/list') {
                socket.send(JSON.stringify({type: 'list'}));
            } else {
                update("Unknown commands: " + parts[0], 'info');
            }
        } else {
            socket.send(JSON.stringify({type: 'msg', body: msg}));
        }
        setTimeout(() => input.focus(), 0);
    };
    input.focus();
};
