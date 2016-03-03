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

.controller('tanksCtrl', ["$scope", "Tanks", function($scope, Tanks) {
  Tanks('S103').$bindTo($scope, "data");
  var readings = Tanks('S103');
  // var date = new Date(readings.data[0][1] * 1000).getHours();
  console.log(readings);
  // console.log(Object.keys(readings)[0]);

  // for (var key in readings) {
  //   console.log("Key: " + key);
  //   console.log("Value: " + readings[key]);
  // }

  var chart = c3.generate({
    bindto: '#chart',
    point: { r: 0 },
    tooltip: { show: false },
    data: {
      // json: {
        // readings
      // }
      columns: [
        [5, 6, 7],
        // readings,
        // readings
      ],

      rows: [
        readings
      ]
      // x: readings.data[0][0], // epoch
      // y: readings.data[1][0]  // CO2
    },
    axis: {
      x: {
        label: 'Date-Time',
        tick: { count: 5 }
      },
      y: {
        label: 'CO2'
      }
    },
    grid: {
      y: {
        lines: [
          { value: 0.0, text: 'Dangerous', axis: 'y', position: 'end' },
          { value: 0.1, text: 'Safe', axis: 'y', position: 'end' },
          { value: 0.2, text: 'Dangerous', axis: 'y', position: 'end' },
        ]
      }
    },
    regions: [
      // {axis: 'y', start: 0.3, end: 0.4, class: 'regionDangerous'},
      // {axis: 'y', start: 0.2, end: 0.3, class: 'regionSafe'},
      // {axis: 'y', start: 0, end: 0.1, class: 'regionDangerous'},
      {axis: 'y', start: 0.1, end: 0.2, class: 'regionSafe'}
    ]
  });
  chart.legend.hide();
}])

.controller('growthCtrl', function($scope) {

})

.controller('atmosphereCtrl', function($scope) {

})

.controller('settingsCtrl', function($scope) {

})
