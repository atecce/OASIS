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
