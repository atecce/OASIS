// * Startup
// ************************************************************************************

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'app' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.services' is found in services.js
// 'starter.controllers' is found in controllers.js
var app = angular.module('app', [
  'ionic',
  'firebase',
  'chart.js',
  'ionic-native-transitions',
  'app.controllers',
  'app.routes',
  'app.services',
  'app.directives'
]);

app.value('loggedIn', {
  status:0
});
app.run(function($ionicPlatform, loggedIn) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)

    //Log out user session on load
    var AuthRef = new Firebase("https://cumarsoasis.firebaseio.com/");
    AuthRef.unauth();
    loggedIn[status] = 0;

    if(window.cordova && window.cordova.plugins.Keyboard) cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
    if(window.StatusBar) $cordovaStatusBar.style(1);
  });
})

// * Tank Chart Settings 92d050
var tankChartConfig = {
  bezierCurve: false,
  emptyDataMessage: ". . .",
  scaleShowHorizontalLines: true,
  scaleShowLabels: true,
  scaleFontStyle: "normal",
  scaleType: "date",
  animation: false,
  responsive: true,
  pointDot : false,
  showTooltips: false,
  datasetStrokeWidth: 1,
  showScale: true,
  scaleOverride: false,
  scaleShowGridLines : false,
  datasetStrokeColor: '#DC5978'
}

// * Growth Chart Settings
var growthChartConfig = {
  bezierCurve: false,
  emptyDataMessage: ". . .",
  scaleShowHorizontalLines: true,
  scaleShowLabels: true,
  scaleFontStyle: "normal",
  scaleType: "date",
  animation: false,
  responsive: true,
  pointDot : false,
  showTooltips: false,
  datasetStrokeWidth: 1,
  showScale: true,
  scaleOverride: false,
  scaleShowGridLines : false,
  datasetStrokeColor: '#92d050'
}

// * Atmosphere Chart Settings
var atmChartConfig = {
  bezierCurve: false,
  emptyDataMessage: ". . .",
  scaleShowHorizontalLines: true,
  scaleShowLabels: true,
  scaleFontStyle: "normal",
  scaleType: "date",
  animation: false,
  responsive: true,
  pointDot : false,
  showTooltips: false,
  datasetStrokeWidth: 1,
  showScale: true,
  scaleOverride: false,
  scaleShowGridLines : false,
  datasetStrokeColor: '#387ef5'
}
