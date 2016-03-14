// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.services' is found in services.js
// 'starter.controllers' is found in controllers.js
var app = angular.module('app', ['ionic', 'firebase', 'chart.js', 'app.controllers', 'app.routes', 'app.services', 'app.directives']);

app.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)

    //Log out user session on load
    var AuthRef = new Firebase("https://cumarsoasis.firebaseio.com/");

    AuthRef.unauth();


    if(window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
    }
    if(window.StatusBar) {
      $cordovaStatusBar.style(1);
    }
  });

})

app.factory("Tanks", ["$firebaseObject", function($firebaseObject) {
  return function(sysID) {
    var ref = new Firebase("https://cumarsoasis.firebaseio.com/sensors/minute/S101");
    var tankRef = ref.child(sysID);

    // return it as a synchronized object
    return $firebaseObject(tankRef);
  }}
]);

app.config(['ChartJsProvider', function (ChartJsProvider) {
  // Configure all charts
  ChartJsProvider.setOptions({
    // colours: ['#FF5252', '#FF8A80'],
    // animation: false,
    // responsive: true,
    // pointDot : false,
    // showTooltips: false,
    // datasetStrokeWidth: 0.01,
    bezierCurve : true,
    // showScale: true,
    // scaleOverride: false,
    // scaleShowGridLines : false,
    // scaleShowLabels: false,
  });
}])
