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

.controller('tanksCtrl', function($scope, $interval, $http) {
  $scope.fetchData = function() {
    console.log("*** Fetching Data... ***");
    $http({
      method: 'GET',
      url: 'https://cumarsoasis.firebaseio.com/data/sensors/liquid_tanks_and_plumbing/S103.json'
    }).then(function successCallback(response) {
      console.log("Response from Firebase:"); console.log(response.data);
      $scope.data = response.data;
      $scope.keyArray = [];
      $scope.dataArray = [];

      for (var time in $scope.data) {
        $scope.keyArray.push(time);
        $scope.dataArray.push($scope.data[time]);
        console.log(time + " is " + $scope.data[time]);
      }

      $scope.myJson.scaleX.values = $scope.keyArray;
      $scope.myJson.series[0].values = $scope.dataArray;
    }, function errorCallback(response) {
      console.log("error recieving data");
    });
  }

  // $interval($scope.fetchData, 3000);

  $scope.myJson = {
    backgroundColor: "#434343",
    globals: { shadow: false, fontFamily: "Helvetica" },
    type: "area",

    legend: {
      layout: "x4",
      backgroundColor: "transparent",
      borderColor: "transparent",
      marker: {
        borderRadius: "50px",
        borderColor: "transparent"
      },
      item: {
        fontColor: "white"
      }
    },
    scaleX: {
      maxItems: 8,
      transform: {
          type: 'date'
      },
      zooming: true,
      values: $scope.keyArray,
      lineColor: "white",
      lineWidth: "1px",
      tick: {
          lineColor: "white",
          lineWidth: "1px"
      },
      item: {
          fontColor: "white"
      },
      guide: {
          visible: false
      }
    },
    scaleY: {
      lineColor: "white",
      lineWidth: "1px",
      tick: {
          lineColor: "white",
          lineWidth: "1px"
      },
      guide: {
          lineStyle: "solid",
          lineColor: "#626262"
      },
      item: {
          fontColor: "white"
      },
    },
    tooltip: {
      visible: false
    },
    crosshairX: {
      scaleLabel: {
        backgroundColor: "#fff",
        fontColor: "black"
      },
      plotLabel: {
        backgroundColor: "#434343",
        fontColor: "#FFF",
        _text: "Number of hits : %v"
      }
    },
    plot: {
      lineWidth: "2px",
      aspect: "spline",
      marker: {
        visible: false
      }
    },
    series: [{
      text: "S103",
      values: $scope.dataArray,
      backgroundColor1: "#1D8CD9",
      backgroundColor2: "#1D8CD9",
      lineColor: "#1D8CD9"
    }]
  };
})

.controller('growthCtrl', function($scope) {

})

.controller('atmosphereCtrl', function($scope) {

})

.controller('settingsCtrl', function($scope) {

})
