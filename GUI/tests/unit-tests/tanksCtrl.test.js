describe('Controller: tanksCtrl', function() {
  var scope, ctrl;

  // * LOAD
  beforeEach(module('app.controllers'));
  // beforeEach(module('app.controllers'));

  // * Initialize controller and a mock scope.
  beforeEach(inject(function($rootScope, $controller) {
    scope = $rootScope.$new();
    $controller('tanksCtrl', { $scope: scope });
  }));

  // * TESTS
  it('should return true', function() {
    expect(true).toBe(true);
  });

  // it('should have a $scope variable', function() {
  //   expect(scope).toBeDefined();
  // });
});
