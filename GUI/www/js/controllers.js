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
.controller('tanksCtrl', function($scope, $interval, $timeout, $http) {
  // * Graph Configuration
  $scope.chartData = [{ data: [] }, { strokeColor: '#FFFFFF', data: []}];

	var ctx = document.getElementById("chart").getContext("2d");
	var chart = new Chart(ctx).Scatter($scope.chartData, {
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
	});
  // console.log($scope.chartData);

  // * Data Fetch
  var fetchData = function() {
    console.log("*** Fetching CO2 Data... ***");
    $http({
      method: 'GET',
      url: 'https://cumarsoasis.firebaseio.com/sensors/minute/S101.json'
    }).then(function successCallback(response) {
      // console.log("Response from Firebase:"); console.log(response.data);

      for (var time in response.data) {
        chart.datasets[0].addPoint(new Date(time * 1000), response.data[time]);
      }

      chart.update();

      fetchPhData();
    }, function errorCallback(response) {
      console.log("Error: " + response);
    });
  }

  var fetchPhData = function() {
    console.log("*** Fetching pH Data... ***");
    $http({
      method: 'GET',
      url: 'https://cumarsoasis.firebaseio.com/sensors/minute/S102.json'
    }).then(function successCallback(response) {
      // console.log("Response from Firebase:"); console.log(response.data);

      for (var time in response.data) {
        // chart.datasets[1].addPoint(new Date(time * 1000), response.data[time]);
      }

      chart.update();
    }, function errorCallback(response) {
      console.log("Error: " + response);
    });
  }

  // Fetch data on view render.
  fetchData();

  // Continuous data fetch every 30 seconds.
  // $interval(function () { fetchData(); }, 30000);
})

// * Growth
// ************************************************************************************
.controller('growthCtrl', function($scope, $interval, $timeout, $http) {
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
    console.log("*** Fetching Temp. Data... ***");
    $http({
      method: 'GET',
      url: 'https://cumarsoasis.firebaseio.com/sensors/minute/S201.json'
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
  // $interval(function () { fetchData(); }, 30000);
})

// * Atmosphere
// ************************************************************************************
.controller('atmosphereCtrl', function($scope, $interval, $timeout, $http) {
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
    console.log("*** Fetching CO2 Data... ***");
    $http({
      method: 'GET',
      url: 'https://cumarsoasis.firebaseio.com/sensors/minute/S305.json'
    }).then(function successCallback(response) {
      // console.log("Response from Firebase:"); console.log(response.data);

      for (var time in response.data) {
        chart.datasets[0].addPoint(new Date(time * 1000), response.data[time]);
      }
      chart.update();
      return;
    }, function errorCallback(response) {
      console.log("Error: " + response);
    });
  }

  // Fetch data on view render.
  fetchData();

  // Continuous data fetch every 30 seconds.
  // $interval(function () { fetchData(); }, 30000);
})

// * Settings
// ************************************************************************************
.controller('settingsCtrl', function($scope) {

})

// * Actuators
// ************************************************************************************
.controller('actuatorCtrl', function($scope,$firebaseObject, Actuators) {

  //Pull states from database
  $rootScope = $scope

  $scope.load = function($rootScope){
    //I hope I find a way to simplify all of this...lol
    var air_bubbler = Actuators.liquid_tanks_and_plumbing.air_bubbler;
    var chiller = Actuators.liquid_tanks_and_plumbing.chiller;
    var condensate_pump = Actuators.liquid_tanks_and_plumbing.condensate_pump;
    var filter_pump = Actuators.liquid_tanks_and_plumbing.filter_pump;
    var heater = Actuators.liquid_tanks_and_plumbing.heater;
    var main_tank_circ = Actuators.liquid_tanks_and_plumbing.main_tank_circulation;
    var nutrient_1_circ = Actuators.liquid_tanks_and_plumbing.nutrient_1_circulation;
    var nutrient_1_dosing = Actuators.liquid_tanks_and_plumbing.nutrient_1_dosing;
    var nutrient_2_circ = Actuators.liquid_tanks_and_plumbing.nutrient_2_circulation;
    var nutrient_2_dosing = Actuators.liquid_tanks_and_plumbing.nutrient_2_dosing;
    var pH_dosing = Actuators.liquid_tanks_and_plumbing.pH_dosing;
    var UV_filter = Actuators.liquid_tanks_and_plumbing.UV_filter;

    console.log("Successfully Retrieved Actuator Status");

    if(air_bubbler){
      $scope.airBubblerState=true;
    }
    if(chiller){
      $scope.chillerState=true;
    }
    if(condensate_pump){
      $scope.condensatePumpState=true;
    }
    if(filter_pump){
      $scope.filterPumpState = true;
    }
    if(main_tank_circ){
      $scope.mainTankCirculationState = true;
    }
    if(nutrient_1_circ){
      $scope.nutrient1Circulation = true;
    }
    if(nutrient_1_dosing){
      $scope.nutrient1Dosing = true;
    }
    if(nutrient_2_circ){
      $scope.nutrient2Circulation = true;
    }
    if(nutrient_2_dosing){
      $scope.nutrient2Dosing = true;
    }
    if(pH_dosing){
      $scope.pHdosing = true;
    }
    if(UV_filter){
      $scope.UVfilter = true;
    }



  }



})
