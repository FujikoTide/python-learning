### Advanced Python OOP Exercises: Thinking Beyond the Basics

These exercises are designed to be more challenging. They don't have a single "right" answer, but they require a well-structured OOP solution. You will need to decide what classes to create, how they should interact, and which design patterns are most appropriate.

#### Exercise 1: A Command-Line Task Manager

**Goal:** Build a robust, extendable command-line task management application.

**The Challenge:**
Design and implement a system that can manage tasks. A user should be able to:
* Add a new task with a name and an optional priority (e.g., `high`, `medium`, `low`).
* Mark an existing task as complete.
* List all tasks, showing their status and priority.
* List only the completed tasks or only the pending tasks.
* Remove a task.
* Persist the tasks to a file (e.g., JSON or a simple text file) so that they are remembered between program runs.

**Thinking Points:**
* What classes do you need? (Hint: You'll likely need a `Task` class and a `TaskManager` or `TaskStorage` class.)
* What special methods (`__str__`, `__repr__`) would be useful for a `Task` object?
* How will you handle user input? You don't need a complex CLI library; simple `input()` loops and `if/elif` statements are fine.
* How will you separate the "logic" of the `TaskManager` from the "presentation" of the command-line interface?
* What custom exceptions might you need (e.g., `TaskNotFound`, `InvalidPriority`)?
* How will you implement the persistence? What dunder methods or composition patterns might help here?

---

#### Exercise 2: A Simple E-commerce Shopping Cart System

**Goal:** Create a system that models the process of a user making a purchase.

**The Challenge:**
Design and implement a system with the following functionalities:
* A user can browse a list of available products. Each `Product` should have a name, a unique ID, and a price.
* A user can add products to a `ShoppingCart`. The cart should be able to store multiple quantities of the same product.
* The `ShoppingCart` should be able to calculate its total price, including a subtotal and an optional sales tax (e.g., 5%).
* Implement a `Checkout` process. The checkout should have a method to process a payment using a specified payment method.
* Implement a basic `PaymentMethod` using an abstract base class. Create at least two concrete subclasses, like `CreditCardPayment` and `PayPalPayment`. These should handle their own logic for "processing" a payment (e.g., printing a confirmation message).
* Use composition to link the `ShoppingCart` and `PaymentMethod` to the `Checkout` process.

**Thinking Points:**
* What are the core classes here? `Product`, `ShoppingCart`, `Checkout`, and an abstract `PaymentMethod` are good starting points. Do you need a separate `LineItem` or `CartItem` class to store quantity?
* How can you use polymorphism to handle different payment methods seamlessly in the `Checkout` class?
* What custom exceptions might be useful (e.g., `ProductNotInStock`, `InsufficientFundsError`)?
* How will you represent the inventory of available products? A dictionary in a simple `Store` class is a good option.
* Consider using properties to manage the read-only attributes of a `Product` or the calculated total of a `ShoppingCart`.

---

#### Exercise 3: A Notification Service with a Strategy Pattern

**Goal:** Design a flexible notification system where the notification method can be easily changed at runtime.

**The Challenge:**
Create a system that can send notifications via different channels (e.g., email, SMS, console).
* Define a `Notifier` class that is the main interface for sending notifications.
* Use the **Strategy Pattern** by defining an abstract base class `NotificationStrategy` with an abstract method `send(message)`.
* Create concrete strategy classes, such as `EmailStrategy`, `SMSStrategy`, and `ConsoleStrategy`, that implement the `send` method. The `EmailStrategy` might need an email address, and the `SMSStrategy` a phone number.
* The `Notifier` class should have an attribute for the current `NotificationStrategy`. It should have a method `set_strategy(strategy)` to change the notification method dynamically. Its `send_notification(message)` method should delegate to the current strategy's `send` method.
* Create a simple `User` class with an email and phone number.
* Demonstrate the system by creating a `Notifier`, setting it to `EmailStrategy` to send an email to a user, and then changing it to `SMSStrategy` to send a text.

**Thinking Points:**
* How will you handle the recipient information? Should the `send` method of the strategy take the recipient, or should the strategy be initialized with it? Consider the pros and cons of both approaches.
* How can you use type hinting to ensure the `set_strategy` method only accepts objects that adhere to the `NotificationStrategy` interface?
* Think about how this design would make it easy to add a new notification type in the future (e.g., a `PushNotificationStrategy`) without changing the `Notifier` class itself.

---

#### Exercise 4: A Simple CSV Data Processor

**Goal:** Create a reusable data processing tool for CSV files using a combination of dunder methods, composition, and error handling.

**The Challenge:**
* Design a `CsvReader` class that acts as a context manager. When used with a `with` statement, it should open a CSV file and make the rows available. The `__exit__` method should handle closing the file, even if an error occurs.
* Implement the `__iter__` and `__next__` dunder methods in the `CsvReader` class to make it an iterator. This will allow it to be used directly in a `for` loop. The iterator should yield each row of the CSV as a dictionary where the keys are the headers.
* Create a separate `DataValidator` class that is composed by the `CsvReader`. The validator should have a method `validate_row(row)` that checks for simple data integrity (e.g., ensuring a specific column is a number and not a string).
* The `CsvReader` should use the `DataValidator` to validate each row before yielding it. If a row is invalid, it should either skip the row or raise a custom `DataValidationError` with details about the invalid row.
* Write a sample CSV file to test your code. The file should have some valid data and some invalid data.

**Thinking Points:**
* How do you combine the context manager (`__enter__`, `__exit__`) and iterator (`__iter__`, `__next__`) patterns? A common approach is for `__enter__` to return the iterator object itself (`self`).
* How will you handle file I/O errors and custom validation errors gracefully?
* Think about what attributes your `CsvReader` needs in its `__init__` and how it will manage the file handle.
* How does this design make the validation logic independent of the reading logic? This is a core benefit of composition.

These exercises are designed to push you to the next level of OOP proficiency. They require you to combine multiple concepts, make design choices, and build more realistic, well-structured applications. Good luck, and feel free to reach out if you have any questions or would like to discuss your design choices as you work on them!