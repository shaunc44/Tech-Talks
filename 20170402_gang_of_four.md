## What is the "Gang of Four" book?  


### *Design Patterns: Elements of Reusable Object-Oriented Software*  
![alt text](design_patterns_cover.jpeg "Logo Title Text 1")  


#### Chapters 1 - 2  

	1.  discuss the pros and cons OOP design techniques  
		i.  program to an interface, not an implementation
		ii. object composition over class inheritance
	2.  covers 7 case studies which include document structure, formatting, UI, UI standards, multiple windows, user operations and spell check  

#### Chapters 3 - 25  

	**CREATIONAL** - *patterns that create objects for you, instead of instantiation*  
	3.  **Abstract factory pattern** groups object factories that have a common theme.  
	4.  **Builder pattern** constructs complex objects by separating construction and representation.  
	5.  **Factory method pattern** creates objects without specifying the exact class to create.  
	6.  **Prototype pattern** creates objects by cloning an existing object.  
	7.  **Singleton pattern** restricts object creation for a class to only one instance.  

	**STRUCTURAL** - *class and object composition; use inheritance to compose the interface*  
	8.  **Adapter** allows classes with incompatible interfaces to work together by wrapping its own interface around that of an already existing class.
	9.  **Bridge** decouples an abstraction from its implementation so that the two can vary independently.
	10. **Composite** composes zero-or-more similar objects so that they can be manipulated as one object.
	11. **Decorator** dynamically adds/overrides behaviour in an existing method of an object.
	12. **Facade** provides a simplified interface to a large body of code.
	13. **Flyweight** reduces the cost of creating and manipulating a large number of similar objects.
	14. **Proxy** provides a placeholder for another object to control access, reduce cost, and reduce complexity.

	**BEHAVIORAL** - *concerned with communication between objects*  
	15. **Chain of responsibility** delegates commands to a chain of processing objects.
	16. **Command** creates objects which encapsulate actions and parameters.
	17. **Interpreter** implements a specialized language.
	18. **Iterator** accesses the elements of an object sequentially without exposing its underlying representation.
	19. **Mediator** allows loose coupling between classes by being the only class that has detailed knowledge of their methods.
	20. **Memento** provides the ability to restore an object to its previous state (undo).
	21. **Observer** is a publish/subscribe pattern which allows a number of observer objects to see an event.
	22. **State** allows an object to alter its behavior when its internal state changes.
	23. **Strategy** allows one of a family of algorithms to be selected on-the-fly at runtime.
	24. **Template** method defines the skeleton of an algorithm as an abstract class, allowing its subclasses to provide concrete behavior.
	25. **Visitor** separates an algorithm from an object structure by moving the hierarchy of methods into one object.



##### *Sources:*  
<https://en.wikipedia.org/wiki/Design_Patterns>  