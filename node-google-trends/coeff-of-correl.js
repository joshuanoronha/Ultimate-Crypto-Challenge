var fs = require('file-system');
var firebase = require('firebase');
var http = require('http');
var waterfall = require('async-waterfall');
var cryptocurrency = ["ethereum", "blockchain", "ripple", "cardano", "tron"]

var config = {
    apiKey: "AIzaSyBf5ERovaG2P1_HblEVy9h5V2N850PWB74",
    authDomain: "cryptocast-2605a.firebaseapp.com",
    databaseURL: "https://cryptocast-2605a.firebaseio.com",
    projectId: "cryptocast-2605a",
    storageBucket: "cryptocast-2605a.appspot.com",
    messagingSenderId: "204336388119"
};
var app = firebase.initializeApp(config);

function writeData(crypto, data) {
    firebase.database().ref('crypto/' + crypto).set({
        data: data
    });
}

function getData(coin) {
    var request = require('sync-request');
    var res = request('GET', 'http://13.126.248.75:8080/dataset/coin/'+coin)
    return JSON.parse(res.body)
}

function coeff(crypto1, crypto2, start, end) {
    // console.log(end)
    crypto1_data = getData(crypto1)
    crypto2_data = getData(crypto2)
    writeData(crypto1, crypto1_data);
    writeData(crypto2, crypto2_data);
    var mean_crypto1 = 0;
    var mean_crypto2 = 0;
    var length = end-start;
    var sumxsq = 0;
    var sumysq = 0;
    var sumxy = 0;
    for (var i = start; i < end; i++) {
        mean_crypto1 = mean_crypto1 + crypto1_data[i].Open;
        mean_crypto2 = mean_crypto2 + crypto2_data[i].Open;
    }
    mean_crypto1 = mean_crypto1 / length;
    mean_crypto2 = mean_crypto2 / length;
    for (var i = start; i < end; i++) {
        var x_xbar = crypto1_data[i].Open - mean_crypto1;
        var y_ybar = crypto2_data[i].Open - mean_crypto2;
        sumxy = sumxy + x_xbar * y_ybar;
        sumxsq = sumxsq + x_xbar * x_xbar;
        sumysq = sumysq + y_ybar * y_ybar;
    }
    var r = sumxy / (Math.sqrt(sumxsq * sumysq));
    return {r:r,date:crypto1_data[0].Date};
}
finalObject = {"ethereum_bitcoin":[],"ethereum_ripple":[],"ethereum_cardano":[],"ethereum_tron":[],"cardano_bitcoin":[],"cardano_ripple":[],"cardano_tron":[],"bitcoin_tron":[],"bitcoin_tron":[],"ripple_tron":[],"bitcoin_ripple":[]}
for (var i=0;i<10;i++)
{
    console.log("Ethereum Bitcoin " + coeff("ethereum", "bitcoin",i,i+20));
    finalObject.ethereum_bitcoin[i] = (coeff("ethereum", "bitcoin",i,i+20));
    console.log("Ethereum Ripple " + coeff("ethereum", "ripple",i,i+20));
    finalObject.ethereum_ripple[i] = (coeff("ethereum", "ripple",i,i+20));
    console.log("Ethereum Cardano " + coeff("ethereum", "cardano",i,i+20));
    finalObject.ethereum_cardano[i] = (coeff("ethereum", "cardano",i,i+20));    
    console.log("Ethereum Tron "+ coeff("ethereum", "tron",i,i+20));
    finalObject.ethereum_tron[i] = (coeff("ethereum", "tron",i,i+20));    
    console.log("Cardano Bitcoin " + coeff("cardano", "bitcoin",i,i+20));
    finalObject.cardano_bitcoin[i] = (coeff("bitcoin", "cardano",i,i+20));    
    console.log("Cardano Ripple " + coeff("cardano", "ripple",i,i+20));
    finalObject.cardano_ripple[i] = (coeff("ripple", "cardano",i,i+20));    
    console.log("Cardano Tron " + coeff("cardano", "tron",i,i+20));
    finalObject.cardano_tron[i] = (coeff("tron", "cardano",i,i+20));    
    
    console.log("Bitcoin Ripple " + coeff("ripple", "bitcoin",i,i+20));
    finalObject.bitcoin_ripple[i] = (coeff("tron", "cardano",i,i+20));    
    
    console.log("Bitcoin Tron " + coeff("ripple", "bitcoin",i,i+20));    
    finalObject.bitcoin_tron[i] = (coeff("ripple", "bitcoin",i,i+20));    

    console.log("Ripple Tron " + coeff("ripple", "tron",i,i+20));
    finalObject.ripple_tron[i] = (coeff("tron", "ripple",i,i+20));    

    fs.writeFileSync("data.json",JSON.stringify(finalObject),'utf-8','w')
}
