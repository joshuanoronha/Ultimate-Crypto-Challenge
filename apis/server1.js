/*
const key          = 'ZV5aCnZjIoKf3DYQPGRM7+2PKHvXkGZ/YU5eR4NQXkKe9hTQwGo4bonK'; // API Key
const secret       = 'hPlbCjwRyimQxIQAf3G0+khv7PTdvdjY7+1U1hpVVw5tFHoUxxMwR1kQkyD/gnHtMSJEW6ASMTX7mJLxtpTD4g=='; // API Private Key
const KrakenClient = require('kraken-node-api');
const kraken       = new KrakenClient(key, secret);
 
(async () => {
    // Display user's balance
    console.log(await kraken.api('Balance'));
 
    // Get Ticker Info
    console.log(await kraken.api('Ticker', { pair : 'XXBTZUSD' }));
})();



var KrakenClient = require('kraken-api');
var kraken = new KrakenClient('ZV5aCnZjIoKf3DYQPGRM7+2PKHvXkGZ/YU5eR4NQXkKe9hTQwGo4bonK', 'hPlbCjwRyimQxIQAf3G0+khv7PTdvdjY7+1U1hpVVw5tFHoUxxMwR1kQkyD/gnHtMSJEW6ASMTX7mJLxtpTD4g==');

// Display user's balance
kraken.api('Balance', null, function(error, data) {
    if(error) {
        console.log(error);
    }
    else {
        console.log(data.result);
    }
});

// Get Ticker Info
kraken.api('Ticker', {"pair": 'XBTCXLTC'}, function(error, data) {
    if(error) {
        console.log(error);
    }
    else {
        console.log(data.result);
    }
});

*/

const kraken = require('kraken-api-wrapper')('ZV5aCnZjIoKf3DYQPGRM7+2PKHvXkGZ/YU5eR4NQXkKe9hTQwGo4bonK', 'hPlbCjwRyimQxIQAf3G0+khv7PTdvdjY7+1U1hpVVw5tFHoUxxMwR1kQkyD/gnHtMSJEW6ASMTX7mJLxtpTD4g==') // create wrapper for API 

kraken.Time()
  .then(result => console.log(result))
  .catch(err => console.error(err));
