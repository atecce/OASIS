# Testing
---

#### Who:
Alessandro Tecce, Prayash Thapa, Trevor Gould, Conor Amanatullah, Kyle Giacomini

#### Title:
MarsOASIS

#### Vision:
Between Blue Origin's successful landing of a booster on a sub-orbital launch and SpaceX's even more impressive landing of the Falcon 9's rocket booster on a mission that launched 11 satellites, an incredibly impressive amount of progress is being made on the space transportation problem. Back-of-the-envelope calculations place SpaceX's feat in particular at reducing the variable cost of space transport by a factor of three-hundred.

However, there has not been matching progress on life-support systems. When we get to Mars, we still have to figure out how to live there. That makes this kind of work critical. Successful completion of this project will create a framework in which it will be incredibly easy for engineers to work on the system while simultaneously generating interest in the cause in general.

#### Automated Tests:
##### Test runner: conf.js
##### Test file: test/spec.js
##### Log:
Using the selenium server at http://localhost:4444/wd/hub
[launcher] Running 1 instances of WebDriver
Started
[32m.[0m[32m.[0m[32m.[0m[32m.[0mWARNING - more than one element found for locator by.model("divText") - the first result will be used
[31mF[0mWARNING - more than one element found for locator by.model("divText") - the first result will be used
[31mF[0m

Failures:
1) MarsOASIS should toggle Actuators view on click in Growth
  Message:
[31m    Failed: Element is not currently visible and so may not be interacted with
    Build info: version: '2.52.0', revision: '4c2593c', time: '2016-02-11 19:06:42'
    System info: host: 'MacBook-Pro.local', ip: '10.201.9.3', os.name: 'Mac OS X', os.arch: 'x86_64', os.version: '10.11.4', java.version: '1.8.0_65'
    Driver info: driver.version: unknown[0m
  Stack:
    ElementNotVisibleError: Element is not currently visible and so may not be interacted with
    Build info: version: '2.52.0', revision: '4c2593c', time: '2016-02-11 19:06:42'
    System info: host: 'MacBook-Pro.local', ip: '10.201.9.3', os.name: 'Mac OS X', os.arch: 'x86_64', os.version: '10.11.4', java.version: '1.8.0_65'
    Driver info: driver.version: unknown
        at WebDriverError (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/error.js:26:26)
        at ElementNotVisibleError (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/error.js:73:26)
        at Object.checkLegacyResponse (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/error.js:580:13)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/webdriver.js:360:15
        at Promise.invokeCallback_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:1329:14)
        at TaskQueue.execute_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2790:14)
        at TaskQueue.executeNext_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2773:21)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2652:27
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:639:7
        at process._tickCallback (node.js:379:9)
    Error
        at [object Object].ElementArrayFinder.applyAction_ (/Users/effulgence/local/lib/node_modules/protractor/built/element.js:380:21)
        at [object Object].ElementArrayFinder.(anonymous function) [as click] (/Users/effulgence/local/lib/node_modules/protractor/built/element.js:78:17)
        at [object Object].ElementFinder.(anonymous function) [as click] (/Users/effulgence/local/lib/node_modules/protractor/built/element.js:708:7)
        at Object.<anonymous> (/Users/effulgence/Projects/MarsOASIS/GUI/test/spec.js:33:34)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/jasminewd2/index.js:96:23
        at new Promise (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:1043:7)
        at controlFlowExecute (/Users/effulgence/local/lib/node_modules/protractor/node_modules/jasminewd2/index.js:82:18)
        at TaskQueue.execute_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2790:14)
        at TaskQueue.executeNext_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2773:21)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2697:25
    From: Task: Run it("should toggle Actuators view on click in Growth") in control flow
        at Object.<anonymous> (/Users/effulgence/local/lib/node_modules/protractor/node_modules/jasminewd2/index.js:81:14)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/jasminewd2/index.js:18:5
        at Promise.invokeCallback_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:1329:14)
        at TaskQueue.execute_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2790:14)
        at TaskQueue.executeNext_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2773:21)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2652:27
    From asynchronous test:
    Error
        at Suite.<anonymous> (/Users/effulgence/Projects/MarsOASIS/GUI/test/spec.js:31:3)
        at Object.<anonymous> (/Users/effulgence/Projects/MarsOASIS/GUI/test/spec.js:2:1)
        at Module._compile (module.js:425:26)
        at Object.Module._extensions..js (module.js:432:10)
        at Module.load (module.js:356:32)
        at Function.Module._load (module.js:313:12)

2) MarsOASIS should toggle Actuators view on click in Atmosphere
  Message:
[31m    Failed: Element is not currently visible and so may not be interacted with
    Build info: version: '2.52.0', revision: '4c2593c', time: '2016-02-11 19:06:42'
    System info: host: 'MacBook-Pro.local', ip: '10.201.9.3', os.name: 'Mac OS X', os.arch: 'x86_64', os.version: '10.11.4', java.version: '1.8.0_65'
    Driver info: driver.version: unknown[0m
  Stack:
    ElementNotVisibleError: Element is not currently visible and so may not be interacted with
    Build info: version: '2.52.0', revision: '4c2593c', time: '2016-02-11 19:06:42'
    System info: host: 'MacBook-Pro.local', ip: '10.201.9.3', os.name: 'Mac OS X', os.arch: 'x86_64', os.version: '10.11.4', java.version: '1.8.0_65'
    Driver info: driver.version: unknown
        at WebDriverError (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/error.js:26:26)
        at ElementNotVisibleError (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/error.js:73:26)
        at Object.checkLegacyResponse (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/error.js:580:13)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/webdriver.js:360:15
        at Promise.invokeCallback_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:1329:14)
        at TaskQueue.execute_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2790:14)
        at TaskQueue.executeNext_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2773:21)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2652:27
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:639:7
        at process._tickCallback (node.js:379:9)
    Error
        at [object Object].ElementArrayFinder.applyAction_ (/Users/effulgence/local/lib/node_modules/protractor/built/element.js:380:21)
        at [object Object].ElementArrayFinder.(anonymous function) [as click] (/Users/effulgence/local/lib/node_modules/protractor/built/element.js:78:17)
        at [object Object].ElementFinder.(anonymous function) [as click] (/Users/effulgence/local/lib/node_modules/protractor/built/element.js:708:7)
        at Object.<anonymous> (/Users/effulgence/Projects/MarsOASIS/GUI/test/spec.js:41:34)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/jasminewd2/index.js:96:23
        at new Promise (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:1043:7)
        at controlFlowExecute (/Users/effulgence/local/lib/node_modules/protractor/node_modules/jasminewd2/index.js:82:18)
        at TaskQueue.execute_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2790:14)
        at TaskQueue.executeNext_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2773:21)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2697:25
    From: Task: Run it("should toggle Actuators view on click in Atmosphere") in control flow
        at Object.<anonymous> (/Users/effulgence/local/lib/node_modules/protractor/node_modules/jasminewd2/index.js:81:14)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/jasminewd2/index.js:18:5
        at Promise.invokeCallback_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:1329:14)
        at TaskQueue.execute_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2790:14)
        at TaskQueue.executeNext_ (/Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2773:21)
        at /Users/effulgence/local/lib/node_modules/protractor/node_modules/selenium-webdriver/lib/promise.js:2652:27
    From asynchronous test:
    Error
        at Suite.<anonymous> (/Users/effulgence/Projects/MarsOASIS/GUI/test/spec.js:39:3)
        at Object.<anonymous> (/Users/effulgence/Projects/MarsOASIS/GUI/test/spec.js:2:1)
        at Module._compile (module.js:425:26)_
        at Object.Module._extensions..js (module.js:432:10)_
        at Module.load (module.js:356:32)_
        at Function.Module._load (module.js:313:12)_

6 specs, 2 failures
Finished in 19.137 seconds
[launcher] 0 instance(s) of WebDriver still running
[launcher] firefox #01 failed 2 test(s)
[launcher] overall: 2 failed spec(s)
[launcher] Process exited with error code 1
##### 2 tests currently failing.


#### User Acceptance Tests:
Use Case ID: UC-01
Use Case Name: Display Graphs
Description: User is able to see sensor data displayed in the form of a graph.

Users: Engineers
Pre-conditions: User has launched the app.
Post-conditions: User sees graphs of sensor data.
Frequency of Use: Daily for data monitoring.
Flow of Events: Launch app -> Look at views
Test Pass? PASS!

Use Case ID: UC-02
Use Case Name: Ability to view the 3 main sensor data in their respective views.
Description: User is able to see all types of sensor data displayed in the form of a graph on the 3 main views provided.

Users: Engineers
Pre-conditions: User has launched the app.
Post-conditions: User sees graphs of sensor data and is able to switch between the 3 main categories of data that is collected.
Frequency of Use: Daily for data monitoring.
Flow of Events: Launch app -> Look at views -> Switch views to the other two.
Test Pass? PASS!

Use Case ID: UC-03
Use Case Name: Display data from a specific range of time.
Description: User is able to change the time interval for the given data.

Users: Engineers
Pre-conditions: User has launched the app and sees relevant graphs.
Post-conditions: User sees graphs of sensor data and is able to click on different buttons to change the range of time.
Flow of Events: Launch app -> Look at views -> Choose a time interval to display the data from (1 min, 1 hour, historical)
Test Pass? FAIL!
