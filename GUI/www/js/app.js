// * Startup
// ************************************************************************************

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.services' is found in services.js
// 'starter.controllers' is found in controllers.js
var app = angular.module('app', ['ionic', 'firebase', 'chart.js', 'app.controllers', 'app.routes', 'app.services', 'app.directives']);
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

// * Tanks
// ************************************************************************************
app.factory("Tanks", ["$firebaseObject", function($firebaseObject) {
  return function(sysID) {
    var ref = new Firebase("https://cumarsoasis.firebaseio.com/sensors/minute/");
    var tankRef = ref.child(sysID);

    // return it as a synchronized object
    return $firebaseObject(tankRef);
  }}
]);

// * Growth
// ************************************************************************************
app.factory("Growth", ["$firebaseObject", function($firebaseObject) {
  return function(sysID) {
    var ref = new Firebase("https://cumarsoasis.firebaseio.com/sensors/minute/");
    var growthRef = ref.child(sysID);

    // return it as a synchronized object
    return $firebaseObject(growthRef);
  }}
]);

// * Atmosphere
// ************************************************************************************
app.factory("Atmosphere", ["$firebaseObject", function($firebaseObject) {
  return function(sysID) {
    var ref = new Firebase("https://cumarsoasis.firebaseio.com/sensors/minute/");
    var atmosphereRef = ref.child(sysID);

    // return it as a synchronized object
    return $firebaseObject(atmosphereRef);
  }}
]);

// * Global Chart Settings
var chartSettings = {
  bezierCurve: true,
  bezierCurveTension: 0.2,
  emptyDataMessage: "Retrieving data . . .",
  scaleShowHorizontalLines: true,
  scaleShowLabels: true,
  scaleType: "date",
  animation: false,
  responsive: true,
  pointDot : false,
  showTooltips: false,
  datasetStrokeWidth: 1,
  bezierCurve : false,
  showScale: true,
  scaleOverride: false,
  scaleShowGridLines : false
}
