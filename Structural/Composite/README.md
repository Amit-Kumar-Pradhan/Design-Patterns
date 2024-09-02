# Composite Design Pattern
* The composite design pattern maintains the tree data structure to represent part-whole relationships.
* Part-whole relationships are concepts that can be applied in many areas including math, reading anf linguistics.

ex: Part whole relationship helps to understand how the numbers in math made up of another numbers. * is sum of 2 and 6.

Problem:
----------
* Here we want to build a recursive data structure so that an element of a tree can have it's sub elements.

Scenario:
----------
* Creating menu and sub-menu items. The sub-menu items can also have their own sub-meniu items.
* Our coding challenge is to display menu and sub-menu items using the composite design pattern.

Solution:
-----------
Our solution consists of 3 major elements
1. Component
2. Child
3. Composite

* The component element is an abstract class, have concrete class called child, inherit from component class called composite.
* Finally our composite class maintains child objects by adding and removing them to and from a data structure. 