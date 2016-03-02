angular.module('app.controllers', [])

.controller('loginCtrl', function($scope) {

})

.controller('registerCtrl', function($scope) {
  var ref = new Firebase("https://cumarsoasis.firebaseio.com/");
  ref.createUser({
    // wot
  }, function(error, userData) {
    if (error) {
      // error
    }
    else {
      // no error
    }
  });
})

.controller('overviewCtrl', function($scope, $http) {
  // XMLHttp Request to grab JSON file.
  var readings;
  $http({ method: 'GET', url: 'data/S305.json' }).then(function successCallback(response) {
      readings = response;
      console.log(readings.data);
      var date = new Date(readings.data[0][1] * 1000).getHours();
      // console.log(date.getHours());
      console.log(date);
      var chart = c3.generate({
        bindto: '#chart',
        point: { r: 0 },
        tooltip: { show: false },
        data: {
          columns: [
            readings.data[0],
            readings.data[1]
          ],
          x: readings.data[0][0], // epoch
          y: readings.data[1][0]  // CO2
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
    }, function errorCallback(response) {
      console.log("Error loading JSON data.")
    });
})

.controller('sensorsCtrl', function($scope) {

})

.controller('actuatorsCtrl', function($scope) {

})

.controller('settingsCtrl', function($scope) {

})
