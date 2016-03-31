angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
  // .state('login', {
  //   url: '/login',
  //   templateUrl: 'templates/login.html',
  //   controller: 'loginCtrl'
  // })

  .state('register', {
    url: '/register',
    templateUrl: 'templates/register.html',
    controller: 'registerCtrl'
  })

  .state('tabsController.tanks', {
    url: '/tanks',
    views: {
      'tab1': {
        templateUrl: 'templates/tanks.html',
        controller: 'tanksCtrl'
      }
    }
  })

  .state('tabsController.growth', {
    url: '/growth',
    views: {
      'tab2': {
        templateUrl: 'templates/growth.html',
        controller: 'growthCtrl'
      }
    }
  })

  .state('tabsController.atmosphere', {
    url: '/atmosphere',
    views: {
      'tab3': {
        templateUrl: 'templates/atmosphere.html',
        controller: 'atmosphereCtrl'
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
  .state('tabsController.login', {
    url: '/login',
    views: {
      'tab5' : {
        templateUrl: 'templates/login.html',
        controller: 'loginCtrl'
      }
    }
  })
  .state('tabsController.actuators', {
    url: '/actuators',
    views: {
      'tab6' : {
        templateUrl: 'templates/actuators.html',
        controller: 'actuatorCtrl'
      }
    }
  })

  .state('tabsController', {
    url: '/main',
    templateUrl: 'templates/tabsController.html',
    abstract: true
  })

  .state('loginModal', {
    url:'/templates/loginModal.html',
    templateUrl: 'templates/loginModal.html'
  })

$urlRouterProvider.otherwise('/main/tanks')

});
