# Proxy Design Pattern
* Proxy becomes handy when creating a highly resource intensive object.

Problem:
----------
* Postpone  object creation unless absolutely necessary due to the high resource requirement object we are creating.
* Therefore, there is a need for placeholder that will in turn create the object when it's creation is absolutely necessary.

Scenario:
-----------
* We create an instance of producer class only when it is available because only a fixed no of producer objects can exist at a time.
* Our proxy is an artist who is checking to see if a producer becaome available for a guest.

Solutions:
----------
* In the proxy design pattern clients interacting with a proxy object most of the time untill the resourse intensive object become available.
* The proxy object is in charge of creating the resource intensive objects.
* Adapter and decorator design patterns are related to the proxy design pattern.