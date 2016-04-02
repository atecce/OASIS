angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider, $ionicConfigProvider, $ionicNativeTransitionsProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $ionicNativeTransitionsProvider.enable(false);
  $ionicConfigProvider.tabs.position('bottom');
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

  .state('tabs.tanks', {
    url: '/tanks',
    nativeTransitions: {
        "type"      : "fade",
        "duration"  : "250"
    },
    views: {
      'tab1': {
        templateUrl: 'templates/tanks.html',
        controller: 'tanksCtrl'
      }
    }
  })

  .state('tabs.growth', {
    url: '/growth',
    nativeTransitions: {
        "type"      : "fade",
        "duration"  : "250"
    },
    views: {
      'tab2': {
        templateUrl: 'templates/growth.html',
        controller: 'growthCtrl'
      }
    }
  })

  .state('tabs.atmosphere', {
    url: '/atmosphere',
    nativeTransitions: {
        "type"      : "fade",
        "duration"  : "250"
    },
    views: {
      'tab3': {
        templateUrl: 'templates/atmosphere.html',
        controller: 'atmosphereCtrl'
      }
    }
  })

  .state('tabs.settings', {
    url: '/settings',
    views: {
      'tab4': {
        templateUrl: 'templates/settings.html',
        controller: 'settingsCtrl'
      }
    }
  })
  .state('tabs.login', {
    url: '/login',
    views: {
      'tab5' : {
        templateUrl: 'templates/login.html',
        controller: 'loginCtrl'
      }
    }
  })
  .state('tabs.actuators', {
    url: '/actuators',
    views: {
      'tab6' : {
        templateUrl: 'templates/actuators.html',
        controller: 'actuatorCtrl'
      }
    }
  })

  .state('tabs', {
    url: '/main',
    templateUrl: 'templates/tabs.html',
    controller: 'tabsCtrl',
    abstract: true
  })

  .state('loginModal', {
    url:'/templates/loginModal.html',
    templateUrl: 'templates/loginModal.html'
  })

$urlRouterProvider.otherwise('/main/tanks')

});
