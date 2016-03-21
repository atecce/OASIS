describe('tanksCtrl', function() {
  var scope, ctrl;

  // * INITIALIZE controller and a mock scope.
  beforeEach(function() {
    module('app');
    inject(function($rootScope, $controller) {
      scope = $rootScope.$new();
      ctrl = $controller('tanksCtrl', { $scope: scope });
    });
  });


  // * TESTS
  it('should have a $scope variable', function() {
    expect(scope).toBeDefined();
  });

  it('should return true', function() {
    expect(true).toBe(true);
  });

});
