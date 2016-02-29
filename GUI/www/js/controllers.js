angular.module('app.controllers', [])

.controller('loginCtrl', function($scope) {

})

.controller('registerCtrl', function($scope) {

})

.controller('overviewCtrl', function($scope) {
  var readings = 'data/S305.json';
  var chart = c3.generate({
    bindto: '#chart',
    point: { r: 0 },
    tooltip: { show: false },
    data: {
      // x: 'date',
      // x_format: '%Y-%m-%d %H:%M:%S',
      mimeType: 'json',
      url: readings
      // columns: [ readings ]
    },
    axis: {
      x: {
        tick: {
          count: 5
        }
      }
    },
    grid: {
      y: {
        lines: [
          { value: 0.2, text: 'Safe', axis: 'y', position: 'end' },
          { value: 0.1, text: 'Dangerous', axis: 'y', position: 'end' },
        ]
      }
    },
    regions: [
      {axis: 'y', end: 50, class: 'regionY'},
      {axis: 'y', start: 0, end: 0.1, class: 'regionY'},
      {axis: 'y', start: 0.1, end: 0.2, class: 'regionY'}
    ]
  });
})

.controller('sensorsCtrl', function($scope) {

})

.controller('actuatorsCtrl', function($scope) {

})

.controller('settingsCtrl', function($scope) {

})
