var debug = true;
angular.module('app.controllers', [])
.controller('tabsCtrl', function($scope, $ionicTabsDelegate, $ionicHistory) {
})

// * Login
// ************************************************************************************
.controller('loginCtrl', function(loggedIn, $scope) {
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
          loggedIn.status = 1;
          console.log(loggedIn.status);
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

// * Register
// ************************************************************************************
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
.controller('tanksCtrl', function($scope, $ionicTabsDelegate, Tanks) {
  var cols = document.getElementsByClassName('tab-item-active');
  for(i=0; i<cols.length; i++) {
    cols[i].style.color =    'blue';
  }
  // * Graph Configuration
  $scope.chartData = [{ data: [] }, { strokeColor: '#DC5978', data: [] }];
	var ctx = document.getElementById("tanksChart").getContext("2d");
	var tanksChart = new Chart(ctx).Scatter($scope.chartData, tankChartConfig);

  // * Data Fetch
  var tanksObj = Tanks('S101', 'hour');
  tanksObj.$bindTo($scope, 'tankData').then(function() { fetchData(); });
  tanksObj.$watch(function() { fetchData(); });
  var fetchData = function() {
    console.log('Fetching data in Tanks.');
    // Enumerating through the JSON data.
    angular.forEach($scope.tankData, function(sensorValue, time) {
      // Firebase appends two useless pieces of data at the end of the JSON file..
      // We need to guard against those or else the graph shits itself.
      if (typeof sensorValue === 'number') {
        if (debug) console.log(new Date(time * 1000), sensorValue);
        tanksChart.datasets[0].addPoint(new Date(time * 1000), sensorValue);
      }
    });
    tanksChart.update();
  }
})

// * Growth
// ************************************************************************************
.controller('growthCtrl', function($scope, Growth) {
  // * Graph Configuration
  $scope.chartData = [{ data: [] }, { datasetStrokeColor: '#FFFFFF', data: [] }];
	var ctx = document.getElementById("growthChart").getContext("2d");
	var growthChart = new Chart(ctx).Scatter($scope.chartData, growthChartConfig);

  // * Data Fetch
  var growthObj = Growth('S201', 'hour');
  growthObj.$bindTo($scope, 'growthData').then(function() { fetchData(); });
  growthObj.$watch(function() { fetchData(); });
  var fetchData = function() {
    console.log('Fetching data in Growth.');
    angular.forEach($scope.growthData, function(sensorValue, time) {
      if (typeof sensorValue === 'number') {
        if (debug) console.log(new Date(time * 1000), sensorValue);
        growthChart.datasets[0].addPoint(new Date(time * 1000), sensorValue);
      }
    });
    growthChart.update();
  }
})

// * Atmosphere
// ************************************************************************************
.controller('atmosphereCtrl', function($scope, Atmosphere) {
  // * Graph Configuration
  $scope.chartData = [{ data: [] }, { strokeColor: '#FFFFFF', data: [] }];
	var ctx = document.getElementById("atmosphereChart").getContext("2d");
	var atmosphereChart = new Chart(ctx).Scatter($scope.chartData, atmChartConfig);

  // * Data Fetch
  var atmosphereObj = Atmosphere('S305', 'hour');
  atmosphereObj.$bindTo($scope, 'atmosphereData').then(function() { fetchData(); });
  atmosphereObj.$watch(function() { fetchData(); });
  var fetchData = function() {
    console.log('Fetching data in Atmosphere.');
    // Enumerating through the JSON data.
    angular.forEach($scope.atmosphereData, function(sensorValue, time) {
      // Firebase appends two useless pieces of data at the end of the JSON file..
      // We need to guard against those or else the graph shits itself.
      if (typeof sensorValue === 'number') {
        if (debug) console.log(new Date(time * 1000), sensorValue);
        atmosphereChart.datasets[0].addPoint(new Date(time * 1000), sensorValue);
      }
    });
    atmosphereChart.update();
  }
})

// * Settings
// ************************************************************************************
.controller('settingsCtrl', function($scope) {

})

// * Actuators
// ************************************************************************************
.controller('actuatorCtrl', function($scope,$ionicModal,$firebaseObject, Actuators, loggedIn) {

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
  $ionicModal.fromTemplateUrl('templates/loginModal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.modal = modal
  })
  $scope.openLogin = function(){
    //prompt user to login when they touch the thingy
    // var state = $scope.id;
    if(!loggedIn.status){
      console.log(loggedIn.status);
      $scope.modal.show();

    }
    else if (loggedIn.status){
      // do nothing
      console.log("logged in ayy lmao");

    }


  }
  $scope.closeModal = function(){
    $scope.modal.hide();
  }


})
