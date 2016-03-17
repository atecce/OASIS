var debug = false;
angular.module('app.controllers', [])

// * Login
// ************************************************************************************
.controller('loginCtrl', function($scope) {
  $scope.login = function(){
    var AuthRef = new Firebase("https://cumarsoasis.firebaseio.com/");
    $scope.logged = false;
    $scope.isloggedIn = false;
    if($scope.password == null){
      console.log("Enter a password");
      $scope.loginError = true;
      $scope.error_password = true;
    }
    AuthRef.authWithPassword({
      email      : $scope.email,
      password   : $scope.password
    }, function(error, authData) {
      if (error) {
        $scope.loginError = true;
        $scope.$digest();
        switch(error.code) {
          case "INVALID_EMAIL":
            $scope.error_user = false;
            $scope.error_password = false;
            $scope.error_email = true;
            $scope.$digest();
            console.log("Bad email");
            break;
          case "INVALID_PASSWORD":
            $scope.error_email = false;
            $scope.error_user = false;
            $scope.error_password = true;
            $scope.$digest();
            console.log("Bad password");
            break;
          case "INVALID_USER":
            $scope.error_email = false;
            $scope.error_password = false;
            $scope.error_user = true;
            $scope.$digest();
            console.log("Bad User");
            break;
          default:
            console.log("There was an error.")
        }

        // console.log('Cannot log in: ', error);
      }
      else {
        $scope.loginError = false;
        $scope.logged = true;
        $scope.loggedSuccess = true;
        $scope.isloggedIn = true;
        setTimeout(function(){
          $scope.loggedSuccess = false;

          $scope.$digest();
        },3000);

        $scope.$digest();
        console.log("Successfully logged in user:" + authData.uid);
      }
    });
  };
  $scope.forgot = function(){
    var AuthRef = new Firebase("https://cumarsoasis.firebaseio.com/");
    AuthRef.resetPassword({
      email: $scope.email
    }, function(error){
      if(error){
        switch (error.code) {
          case "INVALID_USER":
            console.log("The specified user account does not exist.");
            break;
          default:
            console.log("Error resetting password:", error);
    }
      } else {
        $scope.logged = true;
        $scope.loggedForgot = true;
        setTimeout(function(){$scope.logged = false;$scope.$digest();},3000);
        $scope.$digest();
        console.log("Success!");
      }
    });
  };
  $scope.logout = function(){
    var AuthRef = new Firebase("https://cumarsoasis.firebaseio.com/");
    console.log("Successfully Logged out user: ",AuthRef.getAuth().uid);
    $scope.logged = false;
    AuthRef.unauth();
  };
})

.controller('registerCtrl', function($scope) {
  $scope.register = function() {
    var AuthRef = new Firebase("https://cumarsoasis.firebaseio.com/");
    if($scope.password === $scope.passwordConfirm){
      AuthRef.createUser({
        email: $scope.email,
        password: $scope.passwordConfirm
      }, function(error, authData){
        if(error){
          console.log("Account not Created",error);
          $scope.regError = true;
          $scope.$digest();
        }
        else{
          console.log("Account Created!");
          $scope.regError = false;
          $scope.registered = true;
          $scope.registeredBar = true;
          setTimeout(function(){$scope.registeredBar = false;$scope.$digest();}, 3000);
          $scope.$digest();
        }
      });
    }
    else{
      console.log("passwords do not match");
      $scope.passMismatch = true;
      $scope.$digest();
    }
  };
  $scope.registerOpen = function(){
    $scope.showRegister = true;

  };
})

// * Tanks
// ************************************************************************************
.controller('tanksCtrl', function($scope, Tanks) {
  // * Graph Configuration
  $scope.chartData = [{ data: [] }, { strokeColor: '#FFFFFF', data: []}];
	var ctx = document.getElementById("tanksChart").getContext("2d");
	var tanksChart = new Chart(ctx).Scatter($scope.chartData, chartSettings);

  // * Data Fetch
  var tanksObj = Tanks('S102');
  tanksObj.$bindTo($scope, 'tankData');
  tanksObj.$watch(function() { console.log('Fetching data in Tanks.'); fetchData(); });
  var fetchData = function() {
    // Enumerating through the JSON data.
    angular.forEach($scope.tankData, function(sensorValue, time) {
      // Firebase appends two useless pieces of data at the end of the JSON file..
      // We need to guard against those or else the graph shits itself.
      if (typeof sensorValue === 'number') {
        if (debug) console.log(new Date(time * 1000), sensorValue);
        tanksChart.datasets[0].addPoint(new Date(time * 1000), sensorValue);
        tanksChart.update();
      }
    });
  }

  setTimeout(fetchData, 1000);
})

// * Growth
// ************************************************************************************
.controller('growthCtrl', function($scope, Growth) {
  // * Graph Configuration
  $scope.chartData = [{ data: [] }, { strokeColor: '#FFFFFF', data: []}];
	var ctx = document.getElementById("growthChart").getContext("2d");
	var growthChart = new Chart(ctx).Scatter($scope.chartData, chartSettings);

  // * Data Fetch
  var growthObj = Growth('S201');
  growthObj.$bindTo($scope, 'growthData');
  growthObj.$watch(function() { console.log('Fetching data in Growth.'); fetchData(); });
  var fetchData = function() {
    angular.forEach($scope.growthData, function(sensorValue, time) {
      if (typeof sensorValue === 'number') {
        if (debug) console.log(new Date(time * 1000), sensorValue);
        growthChart.datasets[0].addPoint(new Date(time * 1000), sensorValue);
        growthChart.update();
      }
    });
  }

  setTimeout(fetchData, 1000);
})

// * Atmosphere
// ************************************************************************************
.controller('atmosphereCtrl', function($scope, Atmosphere) {
  // * Graph Configuration
  $scope.chartData = [{ data: [] }, { strokeColor: '#FFFFFF', data: []}];
	var ctx = document.getElementById("atmosphereChart").getContext("2d");
	var atmosphereChart = new Chart(ctx).Scatter($scope.chartData, chartSettings);

  // * Data Fetch
  var atmosphereObj = Atmosphere('S305');
  atmosphereObj.$bindTo($scope, 'atmosphereData');
  atmosphereObj.$watch(function() { console.log('Fetching data in Atmosphere.'); fetchData(); });
  var fetchData = function() {
    // Enumerating through the JSON data.
    angular.forEach($scope.atmosphereData, function(sensorValue, time) {
      // Firebase appends two useless pieces of data at the end of the JSON file..
      // We need to guard against those or else the graph shits itself.
      if (typeof sensorValue === 'number') {
        if (debug) console.log(new Date(time * 1000), sensorValue);
        atmosphereChart.datasets[0].addPoint(new Date(time * 1000), sensorValue);
        atmosphereChart.update();
      }
    });
  }

  setTimeout(fetchData, 2000);
})

// * Settings
// ************************************************************************************
.controller('settingsCtrl', function($scope) {

})

// * Actuators
// ************************************************************************************
.controller('actuatorCtrl', function($scope, $interval, $timeout, $http, $state) {
  // need initialize function for initial state
  $scope.saysLogged = function(){
    var userRef = new Firebase("https://cumarsoasis.firebaseio.com/");
    var user = userRef.getAuth();
    if(user === null){
      $scope.error = true;
      $scope.accessErr = true;
      setTimeout(function(){
        $scope.accessErr = false;
        $scope.$digest();
      },3000);
    }
    else {
      $scope.error = false;
      $scope.accessErr = false;
      console.log("Session User: ",user.uid);
      // Pull states here
    }
    //init($scope);
  }

  var init = function($scope){
    var userRef = new Firebase("https://cumarsoasis.firebaseio.com/");
    var user = userRef.getAuth();
    if(user === null){
      $scope.error = true;
    }
    else {
      $scope.error = false;
      console.log("Session User: ",user.uid);
      // Pull states here
    }
  };
  init($scope);
})
