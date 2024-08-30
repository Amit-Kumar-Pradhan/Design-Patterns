# Prototypes Design Pattern
* It clones object according to prototypical instance.
* Here the keywork is cloning. We are talking about making copy instead of creating it.

Problem:
--------
* It is useful when creating many identical object individually. It's expensive interms of computing power.
* Cloning could be an good alternative because it makes carbon copy in the memory space instead of building individual object from scratch.

Scenario:
---------
* Let's assume we are building a car and we can mass produce the car has same color, same options and so on.
* Similarly in our pythion programming scenario you can clone the objects by making a copy of prototype object instead of building them through constructor as long as they are suppose to be identical without variation.

Solution:
---------
* Our solution creating a prototypical instance first and then cloning it whenever you need a replica.
* The prototype pattern is related to abstract factory.