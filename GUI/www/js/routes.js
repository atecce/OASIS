angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
  .state('login', {
    url: '/login',
    templateUrl: 'templates/login.html',
    controller: 'loginCtrl'
  })

  .state('register', {
    url: '/register',
    templateUrl: 'templates/register.html',
    controller: 'registerCtrl'
  })
  
  .state('tabsController.overview', {
    url: '/overview',
    views: {
      'tab1': {
        templateUrl: 'templates/overview.html',
        controller: 'overviewCtrl'
      }
    }
  })

  .state('tabsController.sensors', {
    url: '/sensors',
    views: {
      'tab2': {
        templateUrl: 'templates/sensors.html',
        controller: 'sensorsCtrl'
      }
    }
  })

  .state('tabsController.actuators', {
    url: '/actuators',
    views: {
      'tab3': {
        templateUrl: 'templates/actuators.html',
        controller: 'actuatorsCtrl'
      }
    }
  })

  .state('tabsController.settings', {
    url: '/settings',
    views: {
      'tab4': {
        templateUrl: 'templates/settings.html',
        controller: 'settingsCtrl'
      }
    }
  })

  .state('tabsController', {
    url: '/main',
    templateUrl: 'templates/tabsController.html',
    abstract: true
  })

$urlRouterProvider.otherwise('/main/overview')

});
