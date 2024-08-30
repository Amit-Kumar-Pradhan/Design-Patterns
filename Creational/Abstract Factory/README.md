# Abstract Factory Design Pattern
* It builds on the factory method as the name suggests.

Problem:
---------
* It is useful when a user expect to receive a family of related objects on a given time but doesn't have to know which family it is.

Scenario:
---------
* A pet factoryb include a dog and cat factory. Both cat and dog factory produce dogs and cats related products such as dog and cat food.

Solution:
---------
* Abstract factory consists of abstract factory, concrete factory, abstract product and concrete product.
* For the abstract factory will use abstract pet factory.
* For concrete factory will use dog and cat factory.
* For concrete product will be creating dog and dog food, cat and cat food.
* We implement our abstract factory using inheritance because python is dynamically typed language.
* Please check the solution in abstract_factory.py file.