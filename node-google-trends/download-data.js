// var http = require('http')
// x= new Promise(function (resolve,reject){
//     console.log("abc")
//     http.get({
//         hostname: '13.126.248.75',
//         port: 8080,
//         path: '/dataset/coin/ethereum',
//         agent: false  
//     }, (res) => {
        
//         resolve(res)
//     });
// })
// x.then(data => {
//     console.log(data)
//      data.on('chunk', function (chunk) {
//     console.log('BODY: ' + chunk);
// });})
var request = require('sync-request');
var res = request('GET','http://13.126.248.75:8080/dataset/coin/ethereum')
console.log(res.body.toString('utf-8'));


