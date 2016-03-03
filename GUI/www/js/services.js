angular.module('app.services', [])

.factory('Auth', [function($firebaseAuth){
  var usersRef = new Firebase("https://cumarsoasis.firebaseio.com/users");
  return $firebaseAuth(usersRef);
}])

.service('BlankService', [function(){

}]);
