var express = require('express');

var app = express();

app.get('/', function (req, res) {
    res.send('Hola mundo');
});

app.get('/mensajes/:message', function (req, res) {
    res.send('tu mensaje es '+ req.params.message);
})

app.listen(3000);