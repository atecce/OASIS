angular.module('app.services', [])

// .factory('Auth', [function($firebaseAuth){
//
// }]);
.factory('Actuators', function($firebaseObject) {
  var ref = new Firebase("https://cumarsoasis.firebaseio.com/");
  var data = $firebaseObject(ref.child('actuators').child('current'));
  return data;
})

.factory('Authentication', function($firebaseObject){
  var ref = new Firebase("https://cumarsoasis.firebaseio.com/");

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
