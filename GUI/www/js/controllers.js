angular.module('app.controllers', [])

.controller('loginCtrl', function($scope) {

})

.controller('registerCtrl', function($scope) {

})

.controller('overviewCtrl', function($scope) {
  var chart = c3.generate({
    bindto: '#chart',
    point: { r: 0 },
    tooltip: { show: false },
    data: {
      // x: 'date-time',
      mimeType: 'json',
      url: 'data/S305.json'

    }
  });
})

.controller('sensorsCtrl', function($scope) {

})

.controller('actuatorsCtrl', function($scope) {

})

.controller('settingsCtrl', function($scope) {

})
