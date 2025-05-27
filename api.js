const express = require('express');
var session = require('express-session')

// Yiff categories
const hug = require('./api/backend/hug.js');
const boop = require('./api/backend/boop.js');
const glomp = require('./api/backend/glomp.js');
const blep = require('./api/backend/blep.js');
const lick = require('./api/backend/lick.js');
const kiss = require('./api/backend/kiss.js');
const howl = require('./api/backend/howl.js');
const nuzzle = require('./api/backend/nuzzle.js');
const dog = require('./api/backend/dog.js');
const gay = require('./api/backend/gayyiff.js');
const bj = require('./api/backend/blowjob.js');
const pats = require('./api/backend/pats.js');
const roar = require('./api/backend/roar.js');
const nibble = require('./api/backend/nibble.js');

// Setup the app
const app = express();

// Load in the images.
app.use('/', express.static('public'));

// Get all todos.
app.get('/sfw/hug', (req, res) => {
    var request = hug.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/nsfw/yiff/blowjob', (req, res) => {
    var request = bj.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/sfw/headpats', (req, res) => {
    var request = pats.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/sfw/roar', (req, res) => {
    var request = roar.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/sfw/nibble', (req, res) => {
    var request = nibble.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/sfw/howl', (req, res) => {
    var request = howl.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/sfw/nuzzle', (req, res) => {
    var request = nuzzle.result(g => {
        res.status(200).send({
            result: g
        })
    })
});



app.get('/sfw/glomp', (req, res) => {
    var request = glomp.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/sfw/boop', (req, res) => {
    var request = boop.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/sfw/blep', (req, res) => {
    var request = blep.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/sfw/lick', (req, res) => {
    var request = lick.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/sfw/kiss', (req, res) => {
    var request = kiss.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/sfw/dog', (req, res) => {
    var request = dog.result(g => {
        res.status(200).send({
            result: g
        })
    })
});

app.get('/nsfw/yiff/gay', (req, res) => {
    var request = gay.result(g => {
        res.status(200).send({
            result: g
        })
    })
});




app.get('/sfw/dog/image0.png', (req, res) => {
	res.redirect('https://www.youtube.com/watch?v=o-YBDTqX_ZU')
    });






const PORT = 8080;

app.listen(PORT, () => {
    console.log(`server running on port ${PORT}`)
});
