# Adapter Design Pattern
* An adapter design pattern converts a interface of a class into another one which a client is expecting.

Problem:
---------
This time the problem is that the interfaces are incompatible between a client and server.

Scenario:
------------
* In our scenario we have Korean and British objects that hahve different method names for speaking.
* The client would like to have uniform interface i.e the speak method.

Solution:
---------------
* Use the adapter pattern that translate the method names between the client and the server called.
* Using decorator which is related to the adapter pattern.
