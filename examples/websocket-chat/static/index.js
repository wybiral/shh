const update = msg => {
    const log = document.getElementById('log');
    const outer = document.createElement('div');
    const inner = document.createElement('div');
    inner.innerText = msg;
    outer.appendChild(inner);
    log.appendChild(outer);
    return outer;
}

window.onload = () => {
    const prefix = 'anon';
    let userId = null;
    let socket = new WebSocket('ws://' + window.location.host + '/socket');

    socket.onmessage = evt => {
        let msg = JSON.parse(evt.data);
        switch (msg.type) {
            case 'welcome':
                userId = msg.id;
                update('You are ' + prefix + userId + '.').className = 'info';
                break;
            case 'join':
                update(prefix + msg.id + ' has joined.').className = 'info';
                break;
            case 'leave':
                update(prefix + msg.id + ' has left.').className = 'info';
                break;
            case 'msg':
                const self = (msg.id === userId);
                const name = self ? 'you' : 'anon' + msg.id;
                const className = self ? 'msg self' : 'msg';
                update(name + ': ' + msg.msg).className = className;
                break;
        }
    };

    const form = document.getElementById('form');
    const input = document.getElementById('input');
    form.onsubmit = evt => {
        evt.preventDefault();
        const msg = input.value;
        input.value = '';
        socket.send(msg);
        setTimeout(() => input.focus(), 0);
    };
    input.focus();
};
