angular.module('app.controllers', [])

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

.controller('tanksCtrl', function($scope, $interval, $timeout, $http) {
  // * Graph Configuration
  $scope.chartData = [{ data: [] }];

	var ctx = document.getElementById("chart").getContext("2d");
	var chart = new Chart(ctx).Scatter($scope.chartData, {
		// bezierCurve: true,
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
	});
  // console.log($scope.chartData);

  // * Data Fetch
  var fetchData = function() {
    console.log("*** Fetching Data... ***");
    $http({
      method: 'GET',
      url: 'https://cumarsoasis.firebaseio.com/data/sensors/internal_atmosphere/S305.json'
    }).then(function successCallback(response) {
      // console.log("Response from Firebase:"); console.log(response.data);

      for (var time in response.data) {
        chart.datasets[0].addPoint(new Date(time * 1000), response.data[time]);
      }
      chart.update();
    }, function errorCallback(response) {
      console.log("Error: " + response);
    });
  }

  // Fetch data on view render.
  fetchData();

  // Continuous data fetch every 30 seconds.
  $interval(function () { fetchData(); }, 30000);
})

.controller('growthCtrl', function($scope) {

})

.controller('atmosphereCtrl', function($scope) {

})

.controller('settingsCtrl', function($scope) {

})

.controller('actuatorCtrl', function($scope,$state) {
  // need initialize function for initial state
  $scope.saysLogged = function(){
    init($scope);
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
