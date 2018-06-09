const binance = require('node-binance-api');
binance.options({
  APIKEY: '<kvOq2ffBrPVBXm1H4Q079XJiCSCtuuI4qic33PDdG1scyfdQyXFS8ZyLLH5Xk0F9>',
  APISECRET: '<ar6wQ1VxUD4jOrzudcZehdrxbl6qTW2Z6MToWB7fDvASyRr4DflscTYTWq3QFulf>',
  useServerTime: true, // If you get timestamp errors, synchronize to server time at startup
  test: true // If you want to use sandbox mode where orders are simulated
});

binance.openOrders(false, (error, openOrders) => {
  console.log("openOrders()", openOrders);
});
