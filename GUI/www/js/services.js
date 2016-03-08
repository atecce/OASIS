angular.module('app.services', [])

.factory('Auth', [function($firebaseAuth){
  var usersRef = new Firebase("https://cumarsoasis.firebaseio.com/users");
  return $firebaseAuth(usersRef);
}])

// .service('userLogout', [function(){
//   var usersRef = new Firebase("https://cumarsoasis.firebaseio.com/users");
//   var uid = usersRef.getAuth.uid;
//   usersRef.unauth();
//   console.log("Success in Logging out user", uid)
// }])

.service('BlankService', [function(){

}]);
