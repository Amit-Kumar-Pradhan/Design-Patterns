# Strategy Design Pattern
* This patterns offers a family of interchangeable algorithms to a client.

Problem:
--------
* The problem we often see is that there is a need for dynamically changing the behavior of an object.

Scenario:
------------
* We offer our strategy class with it's default behavior. When there is a need, we provide another variation of the strategy class by dynamically replacing it's default method with a new one.

Solution:
----------
* Python allows adding methods dynamically by importing fthe types module.