# Bridge Design Pattern
* The bridge pattern helps unstangle an unnecessarily complicated class hierarchy.
* Especially when implementation specific classes are mixed with implementation-independent classes.

Problem:
----------
* There are 2 parallel or orthogonal abstractions.
* One is implementation specific and the other is implementation independent.

Scenario:
------------
Our scenario involves implementation-independent circle abstraction and implementation dependent circle abstration
    * The implementation dependent circle involves how to draw a circle.
    * And the implementation independent circle involves defining the properties of a circle and scaling it.


Solution:
-----------
* Our solution is avoiding abstracting both implementation specific and implementation independent classes in a single class hierarchy.