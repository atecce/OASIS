describe('tanksCtrl', function() {
  var scope, ctrl;

  // * LOAD
  beforeEach(module('app'));

  // * Initialize controller and a mock scope.
  beforeEach(inject(function($rootScope, $controller) {
    scope = $rootScope.$new();
    ctrl = $controller('tanksCtrl', { $scope: scope });
  }));

  // * TESTS
  it('should return true', function() {
    expect(true).toBe(true);
  });

  it('should have a $scope variable', function() {
    expect(scope).toBeDefined();
  });
});
