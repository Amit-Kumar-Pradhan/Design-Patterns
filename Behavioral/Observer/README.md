# Observer Design Pattern
* The observer design pattern establishes a one to many relationship between a subject and multiple observers.

Problem:
------------
Our problem here is that a subject need to be monitored and other observer objects should be notified when there is a change in the subject.

Scenario:
-------------
* Keep track of core temperature of reactors at a power plant. When there is a change in the core temperature, registered observers must be notified.


Solution:
-----------
* Our solution uses an abstract class called subject, which has the interface that allows operations such as attaching, detaching and modifying observers.
* We also need concrete subject classes inheriting from the abstract subject class.
* Singleton is related to the observer design pattern.