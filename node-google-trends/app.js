const googleTrends = require('google-trends-api');
var bodyParser = require('body-parser');

function getTrends(name) {
  return new Promise(function (resolve, reject) {
    googleTrends.interestOverTime({ keyword: name })
      .then(function (results) {
        results = JSON.parse(results);

        results.default.timelineData.forEach(element => {
          // console.log(element.time)
          // console.log(element.value[0])
          time = []
          value = []
          time.push(element.time)
          value.push(element.value[0])
          data = {
            time: time,
            value: value
          }
          resolve(data)
        });
      })
      .catch(function (err) {
        console.error('Oh no there was an error', err);
        reject(err)
      });
  })
}
function initial() {
  getTrends("Bitcoin").then(value => {
    console.log(value);
    return value
  }
  ).catch(err => {
    console.log(err);
  })
}
console.log(initial())