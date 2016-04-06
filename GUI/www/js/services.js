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
.factory("Tanks", ["$firebaseObject", function($firebaseObject) {
  return function(sysID, tRange) {
    var url = "https://cumarsoasis.firebaseio.com/sensors/" + tRange + "/";
    var ref = new Firebase(url);
    var tankRef = ref.child(sysID);

    // return it as a synchronized object
    return $firebaseObject(tankRef);
  }}
])

// * Growth
// ************************************************************************************
.factory("Growth", ["$firebaseObject", function($firebaseObject) {
  return function(sysID, tRange) {
    var url = "https://cumarsoasis.firebaseio.com/sensors/" + tRange + "/";
    var ref = new Firebase(url);
    var growthRef = ref.child(sysID);

    // return it as a synchronized object
    return $firebaseObject(growthRef);
  }}
])

// * Atmosphere
// ************************************************************************************
.factory("Atmosphere", ["$firebaseObject", function($firebaseObject) {
  return function(sysID, tRange) {
    var url = "https://cumarsoasis.firebaseio.com/sensors/" + tRange + "/";
    var ref = new Firebase(url);
    var atmosphereRef = ref.child(sysID);

    // return it as a synchronized object
    return $firebaseObject(atmosphereRef);
  }}
]);
