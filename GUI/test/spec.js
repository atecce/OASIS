// spec.js
describe('MarsOASIS', function() {
  beforeEach(function() {
    browser.get('http://localhost:8100');
  });

  it('should render the Tanks graph on launch', function() {
    expect(browser.getTitle()).toEqual('Tanks');
    expect(element(by.id('tanksChart')).isPresent()).toBe(true);
  });

  it('should render the Growth graph on switch', function() {
    element(by.linkText('Growth Medium')).click();
    expect(browser.getTitle()).toEqual('Growth');
    expect(element(by.id('growthChart')).isPresent()).toBe(true);
  });

  it('should render the Atmosphere graph on switch', function() {
    element(by.linkText('Atmosphere')).click();
    expect(browser.getTitle()).toEqual('Atmosphere');
    expect(element(by.id('atmosphereChart')).isPresent()).toBe(true);
  });

  it('should toggle Actuators view on click in Tanks', function() {
    expect(element(by.id('tanksChart')).isPresent()).toBe(true);
  });

  it('should toggle Actuators view on click in Growth', function() {
    element(by.linkText('Growth Medium')).click();
    expect(element(by.id('growthChart')).isPresent()).toBe(true);
  });

  it('should toggle Actuators view on click in Atmosphere', function() {
    element(by.linkText('Atmosphere')).click();
    expect(element(by.id('atmosphereChart')).isPresent()).toBe(true);
  });
});
