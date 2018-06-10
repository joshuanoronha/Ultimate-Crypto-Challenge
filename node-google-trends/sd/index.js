var request = require('sync-request');
var sd;
function getData(coin) {
    var res = request('GET', 'http://13.126.248.75:8080/dataset/coin/'+coin)
    return JSON.parse(res.body)
}

function coeff(crypto1, crypto2, start, end) {
    crypto1_data = getData(crypto1)
    crypto2_data = getData(crypto2)
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
    var skewness = 0;
    var kurtosis = 0;
    for (var i = start; i < end; i++) {
        var x_xbar = crypto1_data[i].Open - mean_crypto1;
        skewness = skewness + Math.pow(x_xbar,3);
        kurtosis = kurtosis + Math.pow(x_xbar,4);
        sumxsq = sumxsq + x_xbar * x_xbar;
    }
    sd = (Math.sqrt(sumxsq))/length;
    kurtosis = (kurtosis/(length*Math.pow(sd,4)))-3
    skewness = skewness/(length*Math.pow(sd,3));
    console.log(sd)
    console.log(skewness)
    console.log(kurtosis)
}
coeff("bitcoin","ethereum",0,90)