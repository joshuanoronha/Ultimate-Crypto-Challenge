var express = require('express');
var app = express();
var firebase= require('firebase');
app.set('view engine', 'ejs');


var trends = require('google-trends-api');

app.get('/', function(req, res) {
    res.render('pages/index1', {'logged_in': firebase.currentUser});
    console.log("value is " + firebase.currentUser);

});

app.get('/login', function(req, res) {
    res.render('pages/login');

});

/*
trends.interestOverTime({keyword: ['Bitcoin', 'Ethereum','ripple','tron','cardano']})
.then(function(results){
  console.log('These results are awesome', results);
})
.catch(function(err){
  console.error('Oh no there was an error', err);
});
*/



app.use(express.static( "public" ) );
app.listen(8080);
