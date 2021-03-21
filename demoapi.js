const fetch = require('node-fetch');

fetch('http://localhost:1337/1337_1337_1337_1337_1337_1337_1337_1337=192.168.0.1', {
    method: 'GET',
})
    .then(res => res.json())
    .then(json => {
        console.log(json.ip);
    })
    .catch(err => console.log(err));