# Chain Of Responsibilities Design pattern
* The chain of responsibility pattern opens up various responsibilities of processing for a given request.
* The chain of responsibility pattern decouples the request and it's processing.

Problem:
------------
* Our problem is that many different types of processing need to be done depending on the request.

Scenario:
-------------
* In our scenario, we can receive an integer value. We use different handlers to find out it's range.

Solution:
--------------
* As our solution, we use an abstract handler that stores a successor that will handle a request, if the current handler doesn't handle it.
* Concrete handlers check if they can handle the request.
* If they can, they can handle it and return true value, indicating that the request was handled.
* Composite is related to the chain of responsibility design pattern.
