# CSCI 3308: MarsOASIS Testing
---

#### Who:
###### GUI: Prayash Thapa, Conor Amanatullah, Kyle Giacomini, Trevor Gould
###### Systems software: Alessandro Tecce

#### Title: MarsOASIS

#### Vision:
> Between Blue Origin's successful landing of a booster on a sub-orbital launch and SpaceX's even more impressive landing of the Falcon 9's rocket booster on a mission that launched 11 satellites, an incredibly impressive amount of progress is being made on the space transportation problem. Back-of-the-envelope calculations place SpaceX's feat in particular at reducing the variable cost of space transport by a factor of three-hundred.
However, there has not been matching progress on life-support systems. When we get to Mars, we still have to figure out how to live there. That makes this kind of work critical. Successful completion of this project will create a framework in which it will be incredibly easy for engineers to work on the system while simultaneously generating interest in the cause in general.

#### Automated Tests:
##### Tools: End-to-End UI testing using Protractor & Jasmine
##### Test configuration file: GUI/conf.js
##### Test file: GUI/test/spec.js

```javascript
$ ionic serve && webdriver-manager start && protractor conf.js
```
##### Current state log: Failing 2/6 tests.
```javascript
Using the selenium server at http://localhost:4444/wd/hub
[launcher] Running 1 instances of WebDriver
Started . . . . . .

6 specs, 2 failures
Finished in 19.137 seconds
[launcher] 0 instance(s) of WebDriver still running
[launcher] firefox #01 failed 2 test(s)
[launcher] overall: 2 failed spec(s)
[launcher] Process exited with error code 1
###### 2 tests currently failing.
```

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
