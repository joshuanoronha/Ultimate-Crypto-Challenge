const googleTrends = require('google-trends-api');
var bodyParser = require('body-parser');
var firebase = require('firebase');
require('firebase/app');
require('firebase/database');
var config = {
  apiKey: "AIzaSyBf5ERovaG2P1_HblEVy9h5V2N850PWB74",
  authDomain: "cryptocast-2605a.firebaseapp.com",
  databaseURL: "https://cryptocast-2605a.firebaseio.com",
  projectId: "cryptocast-2605a",
  storageBucket: "cryptocast-2605a.appspot.com",
  messagingSenderId: "204336388119"
};
firebase.initializeApp(config);
var database = firebase.database();

function getTrends(name) {
  return new Promise(function (resolve, reject) {
    googleTrends.interestOverTime({ keyword: name })
      .then(function (results) {
        results = JSON.parse(results);
        time = []
        value = []
        results.default.timelineData.forEach(element => {
          time.push(element.time)
          value.push(element.value[0])
        });
        data = {
          title: name,
          time: time,
          value: value
        }
        resolve(data)
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
    var userId = firebase.auth().currentUser.uid;
    return firebase.database().ref('/users/' + userId).once('value').then(function (snapshot) {
      var username = (snapshot.val() && snapshot.val().username) || 'Anonymous';
    });

    // function writeUserData(value) {
    //   firebase.database().ref('crypto-rates/' + data.title).set({
    //     time : data.time,
    //     email: data.value,
    //   });
    // }
  }
  ).catch(err => {
    console.log(err);
  })
}

initial()