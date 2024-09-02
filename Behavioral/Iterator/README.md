# Iterator Design Pattern
* The iterator pattern allows a client to have sequential access to the elements of an aggregate object without exposing it's underlying structure.

Problem:
----------
* Some programmers over crowds the transversal interfaces of an aggregate object for every possible way of iteration.

Scenario:
----------
* Will be building our own iterator that takes advantages of python iterator called zip.
* The iterator goes through a list of German counting words. It will iterate upto a certian point based on client input.

Solution:
----------
* The iterator involves access and traversal features from the aggregate object.
* It also provides an interface for accessing the elements of an aggregate object.
* An iterator keeps track of the objects being traversed.
* Our solution is to make the aggregate object create an iterator for a client.
* The composite design pattern is related to the iterator pattern.

