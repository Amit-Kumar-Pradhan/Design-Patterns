# Visitor Design Pattern
* Visitor design pattern sallows adding new features to an existing class hierarchy without changing it.

Problem:
-----------
* It's sometime necessary to add new operations, dynamically to exist in classes with minimal changes.

Scenario:
-----------
* For our scenario, we present a house class. Visitors in this scenarion include an HVAC specialist and an electrician.
* The HVAC specialist in our scenario is visitor type one, and the electrician is visitor type two.

Solutions:
------------
* The visitors pattern represents new operation to be performed on the various elements of an existing class hierarchy.
* Visitor can also provide an operation on a composite object.
