describe('tanksCtrl', function() {
  var ctrl;

  beforeEach(module('firebase'))
  beforeEach(module('app.controllers'))
  beforeEach(module('app.services'))
  // * INITIALIZE controller and a mock scope.
  beforeEach(function() {
    inject(function(_$rootScope_, _$controller_, _firebase_) {
      var scope = _$rootScope_.$new();
      ctrl = _$controller_('tanksCtrl', { $scope: scope });
    });
  });


  // * TESTS
  it('should have a $scope variable', function() {
    expect(ctrl).toBeDefined();
  });

  it('should return true', function() {
    expect(true).toBe(true);
  });

});
