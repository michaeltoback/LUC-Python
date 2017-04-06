Length Unit Conversion Exercise, see attached pdf file for exercise

Solution files
===============
- <unit>ConversionStrategy.java - strategy object for insertion into implementation file
- <Component>Tests.java - JUnit tests
- ConversionStrategy.java - interface for strategy pattern
- LengthUnit.java - interface definition
- LengthUnitImpl.java - implementation as Value Object, including strategy pattern
- LUCMain.java - CLI Driver
- LUCTestSuite.java - JUnit driver

Execution
=========
How to run CLI:
java LUCMain <length> <unit> <conv_unit>

How to run tests:
java LUCTestSuite

Design Discussion
=================

Value Objects
-------------

From Martin Fowler's description of a value object (http://martinfowler.com/bliki/ValueObject.html)

In Patterns of Enterprise Application Architecture I described Value Object as a small object such as a Money or date range object. Their key property is that they follow value semantics rather than reference semantics.

You can usually tell them because their notion of equality isn't based on identity, instead two value objects are equal if all their fields are equal. Although all fields are equal, you don't need to compare all fields if a subset is unique - for example currency codes for currency objects are enough to test equality.

A general heuristic is that value objects should be entirely immutable. If you want to change a value object you should replace the object with a new one and not be allowed to update the values of the value object itself - updatable value objects lead to aliasing problems.

Early J2EE literature used the term value object to describe a different notion, what I call a Data Transfer Object. They have since changed their usage and use the term Transfer Object instead.

You can find some more good material on value objects on the wiki (http://c2.com/cgi/wiki?ValueObject) and by Dirk Riehle (http://www.riehle.org/computer-science/research/1998/ubilab-tr-1998-10-1.html).

Value Object Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The value object contains an equal method which can handle LengthUnit objects of different measurement types; that is, it knows that 3 m == 300 cm. It does this by calling the convert method on the second object where its' unit type differs from the first.

The Value object supports the strategy pattern, but takes advantage of the idea that it "knows" which strategy to implement by default. In the default implementation, it leverages the unit value as a key into a Map to get the strategy. However, one can also call an API to directly set the conversion method.

The Value Object implementation also contains the list of possible measurement values and its' mapping to conversion methods. If the default constructor is called, this is accessible.

Strategy Pattern
----------------

The better explanation with examples can be found in the GoF book (https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)

Here is the short version

From Wikipedia: (https://en.wikipedia.org/wiki/Strategy_pattern)
In computer programming, the strategy pattern (also known as the policy pattern) is a behavioral software design pattern that enables an algorithm's behavior to be selected at runtime. The strategy pattern

    defines a family of algorithms,
    encapsulates each algorithm, and
    makes the algorithms interchangeable within that family.

Strategy lets the algorithm vary independently from clients that use it.[1] Strategy is one of the patterns included in the influential book Design Patterns by Gamma et al. that popularized the concept of using patterns to describe software design.

For instance, a class that performs validation on incoming data may use a strategy pattern to select a validation algorithm based on the type of data, the source of the data, user choice, or other discriminating factors. These factors are not known for each case until run-time, and may require radically different validation to be performed. The validation strategies, encapsulated separately from the validating object, may be used by other validating objects in different areas of the system (or even different systems) without code duplication.

Strategy Pattern Implementation in this exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We implemented the strategy pattern by creating a simple interface called Conversion Strategy with a single method; convert, which takes the destination type as a single parameter.

Each implementation for the Conversion is essentially a case statement which creates a new object of the new unit type, converting the length attribute associated with the initial measurement unit to a length commensurate with the new measurement unit.

Adding a new measurement conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add a new measurement conversion, one would need to:
1) Add the constant to the list in the LengthUnit interface
2) Create a conversion strategy class which is contains an implementation of the convert routine
3) Add the conversion to each of the existing conversion routines (if applicable), and
4) Add the string/class entry to convStratMap, where the string is the reference to the constant in #1 and the class is conversion strategy implementation created in step 2.

IMHO, #3 is a "code smell" that might be addressed if more than one measurement type is added, possibly by moving the values associated with the case statement to a configuration file so that the code would not change, just a text entry.