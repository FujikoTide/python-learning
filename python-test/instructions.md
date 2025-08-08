## Python OOP Exercises: Cementing Knowledge

### **Phase 1: Foundations (Core Concepts)**

#### 1. **Understanding the "Why" of OOP:**

- **Exercise 1.1: Procedural vs. OOP - Task Management:**

  - **Goal:** Appreciate how OOP structures code better for complex scenarios.
  - **Task:**
    1.  Write a simple _procedural_ script that manages tasks. It should store tasks as dictionaries (e.g., `{'name': 'Buy groceries', 'completed': False}`) in a list. Include functions to add a task, mark a task as complete, and list all tasks.
    2.  Now, refactor the task management system using an _OOP approach_. Create a `Task` class with attributes like `name` and `completed`, and methods like `mark_complete()`. Manage a list of `Task` objects.
    3.  Reflect: Which approach felt more organized and easier to extend (e.g., if you wanted to add task priorities or due dates)?

- **Exercise 1.2: Modeling a Simple Item:**

  - **Goal:** See the immediate benefit of bundling data and behavior.
  - **Task:**
    1.  Imagine you need to represent a "Product" in a store. What data (attributes) would it have? What actions (behaviors/methods) could you perform on it?
    2.  Sketch out the `Product` class structure (just class name, `__init__` with parameters, and a couple of method names) without writing full code yet. Briefly explain _why_ each chosen attribute and method belongs to the `Product` class.

- **Exercise 1.3: Reusability - User Profile:**

  - **Goal:** Understand how classes enable code reusability.
  - **Task:**
    1.  Define a `UserProfile` class that stores a user's `username`, `email`, and `is_active` status. Include methods to `activate()` and `deactivate()` the profile.
    2.  Create three different `UserProfile` objects (e.g., for an admin, a regular user, and a guest). Demonstrate how you can reuse the same class definition to manage distinct user data.

- **Exercise 1.4: Abstraction - Remote Control:**

  - **Goal:** Grasp the concept of hiding complexity.
  - **Task:**
    1.  Consider a `TV` class. It has complex internal mechanisms for `turn_on()`, `change_channel()`, etc.
    2.  Explain how a `RemoteControl` object abstracts away these complexities. What methods would the `RemoteControl` need to expose to the user, and how would they interact with the `TV`'s methods? You don't need to write code, just describe the interaction in plain language, highlighting the "abstraction."

- **Exercise 1.5: Identify OOP Candidates:**
  - **Goal:** Practice identifying where OOP is a good fit.
  - **Task:** For each of the following scenarios, decide whether an OOP approach would be beneficial, and if so, briefly describe what classes you would create and why:
    - Calculating the factorial of a number.
    - Building a simple bank application (accounts, transactions).
    - Sorting a list of integers.
    - Representing playing cards and a deck of cards.
    - Converting temperature from Celsius to Fahrenheit.

#### 2. **Classes and Objects:**

- **Exercise 2.1: Simple `Book` Class:**

  - **Goal:** Practice basic class and object creation, attributes, and methods.
  - **Task:**
    1.  Define a class `Book` with attributes `title`, `author`, and `publication_year`.
    2.  Add a method `get_age()` that returns how many years old the book is (current year - publication year).
    3.  Create two `Book` objects and print their details and age.

- **Exercise 2.2: `Restaurant` Class with Menu Items:**

  - **Goal:** Work with lists as attributes and simple method interactions.
  - **Task:**
    1.  Create a `Restaurant` class with `name` and `cuisine_type` attributes.
    2.  Add a method `add_menu_item(item_name, price)` that adds items to an internal list of menu items.
    3.  Add a method `display_menu()` that prints all menu items and their prices.
    4.  Instantiate a restaurant, add a few items, and display the menu.

- **Exercise 2.3: `Car` Driving Simulation:**

  - **Goal:** Understand `self` and state changes within methods.
  - **Task:**
    1.  Define a `Car` class with `make`, `model`, and `speed` (initialized to 0) attributes.
    2.  Add a `accelerate(amount)` method that increases `speed`.
    3.  Add a `brake(amount)` method that decreases `speed` (ensure speed doesn't go below 0).
    4.  Add a `get_speed()` method.
    5.  Create a `Car` object, accelerate it, brake it, and print its speed at different stages.

- **Exercise 2.4: `Student` and Grades:**

  - **Goal:** Practice managing collections within objects and calculating summaries.
  - **Task:**
    1.  Create a `Student` class with `name`, `student_id`, and a list called `grades` (initially empty).
    2.  Add a method `add_grade(grade)` that appends a grade to the list.
    3.  Add a method `get_average_grade()` that calculates and returns the average of all grades.
    4.  Create a `Student` object, add several grades, and print their average.

- **Exercise 2.5: Simple `Counter`:**
  - **Goal:** Reinforce `self` for attribute modification.
  - **Task:**
    1.  Define a `Counter` class.
    2.  Initialize an attribute `count` to 0 in its `__init__` method.
    3.  Add `increment()` and `decrement()` methods that modify `count`.
    4.  Add a `get_count()` method.
    5.  Create a counter, increment it multiple times, decrement it, and print its value.

#### 3. **The Constructor (`__init__`)**:

- **Exercise 3.1: Required Arguments in `__init__`:**

  - **Goal:** Ensure understanding of mandatory `__init__` parameters.
  - **Task:**
    1.  Create a `Person` class. Its `__init__` method must take `name` and `age` as arguments and assign them to instance attributes.
    2.  Try to create a `Person` object without providing a name or age. Observe the error.
    3.  Create two valid `Person` objects and print their details.

- **Exercise 3.2: Default Values in `__init__`:**

  - **Goal:** Use default parameters for optional attributes.
  - **Task:**
    1.  Modify the `Book` class from Exercise 2.1. Make `publication_year` an optional parameter with a default value of `None` (or the current year).
    2.  Create a `Book` object providing all parameters, and another one omitting the publication year. Print their details.

- **Exercise 3.3: `ShoppingCart` Initialization:**

  - **Goal:** Initialize complex data structures within `__init__`.
  - **Task:**
    1.  Create a `ShoppingCart` class. Its `__init__` should initialize an empty list called `items`.
    2.  Add an `add_item(item_name, price)` method.
    3.  Add a `get_total_price()` method.
    4.  Create a shopping cart, add a few items, and print the total price.

- **Exercise 3.4: Initial Validation in `__init__`:**

  - **Goal:** Implement basic input validation in the constructor.
  - **Task:**
    1.  Create a `Temperature` class. Its `__init__` should take a `celsius` value.
    2.  If `celsius` is less than -273.15 (absolute zero), raise a `ValueError`.
    3.  Add a `get_fahrenheit()` method.
    4.  Test with a valid temperature and an invalid one to see the `ValueError`.

- **Exercise 3.5: User Registration (Advanced `__init__`):**
  - **Goal:** Combine mandatory, optional, and default attributes in `__init__`.
  - **Task:**
    1.  Create a `User` class.
    2.  The `__init__` method should take `username` and `password` as mandatory.
    3.  It should also take `email` as an optional argument, defaulting to `None`.
    4.  Initialize `is_active` to `True` by default.
    5.  Add a method `deactivate_account()` that sets `is_active` to `False`.
    6.  Create a user with and without an email, and demonstrate deactivating an account.

#### 4. **Basic Method Types:**

- **Exercise 4.1: `MathOperations` with Static Methods:**

  - **Goal:** Practice defining and using static methods.
  - **Task:**
    1.  Create a `MathOperations` class.
    2.  Add static methods `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, and `divide(a, b)`.
    3.  Call these methods directly on the class (e.g., `MathOperations.add(5, 3)`).
    4.  Explain why static methods are suitable here.

- **Exercise 4.2: `DateConverter` with Class Methods:**

  - **Goal:** Use class methods as alternative constructors.
  - **Task:**
    1.  Create a `Date` class with `__init__(self, year, month, day)`.
    2.  Add a class method `from_string(cls, date_str)` that takes a date string (e.g., "2023-10-26") and returns a `Date` object. Assume the format is always YYYY-MM-DD.
    3.  Add a `display_date()` instance method.
    4.  Create `Date` objects using both the regular constructor and the class method.

- **Exercise 4.3: `Product` with Class-Level Price Calculation:**

  - **Goal:** Use class methods to operate on class attributes.
  - **Task:**
    1.  Modify the `Product` class. Add a `tax_rate` class variable (e.g., 0.05).
    2.  Add a `calculate_price_with_tax(cls, base_price)` class method that computes a price including the `tax_rate`.
    3.  Create a product instance and demonstrate calculating price using the class method. Change the `tax_rate` and show how it affects subsequent calculations.

- **Exercise 4.4: `LoggingUtility` with Static Methods:**

  - **Goal:** Understand static methods for utility functions.
  - **Task:**
    1.  Create a `LoggingUtility` class.
    2.  Add static methods `log_info(message)`, `log_warning(message)`, and `log_error(message)`. These methods should just print the message prefixed with "INFO: ", "WARNING: ", or "ERROR: ".
    3.  Call these static methods from different parts of your code to simulate logging.

- **Exercise 4.5: `UserSettings` with Class Method for Default Config:**
  - **Goal:** Apply class methods for common pre-defined configurations.
  - **Task:**
    1.  Create a `UserSettings` class with `theme`, `font_size`, and `language` attributes.
    2.  Add an `__init__` method.
    3.  Add a class method `default_settings(cls)` that returns a `UserSettings` object with predefined default values (e.g., "dark", 14, "en").
    4.  Create a settings object using `default_settings` and another with custom values.

#### 5. **Encapsulation (Implicit in Python):**

- **Exercise 5.1: `BankAccount` with Protected Balance:**

  - **Goal:** Use the single underscore convention for protected attributes.
  - **Task:**
    1.  Create a `BankAccount` class. Store the balance as `_balance` (protected).
    2.  Add `deposit(amount)` and `withdraw(amount)` methods that modify `_balance`. Ensure `withdraw` prevents negative balance.
    3.  Add a `get_balance()` method to read the balance.
    4.  Demonstrate deposit, withdraw, and getting balance. (Optional: Try to access `_balance` directly and reflect on why you shouldn't).

- **Exercise 5.2: `Person` with `@property` for Age:**

  - **Goal:** Use `@property` for read-only access to a computed attribute.
  - **Task:**
    1.  Create a `Person` class with `name` and `birth_year` attributes.
    2.  Implement an `@property` decorator for `age` that calculates the age based on `birth_year` and the current year. `age` should be read-only.
    3.  Create a `Person` object and print its name and age.

- **Exercise 5.3: `TemperatureConverter` with `@property` and Setter Validation:**

  - **Goal:** Use `@property` with a setter for validation.
  - **Task:**
    1.  Create a `Temperature` class. Store the temperature in Celsius as `_celsius`.
    2.  Implement `@property` for `celsius` (getter and setter).
    3.  In the `celsius` setter, add validation: raise a `ValueError` if the value is below -273.15.
    4.  Add another `@property` for `fahrenheit` (read-only, computed from `_celsius`).
    5.  Test setting valid and invalid Celsius values, and print Fahrenheit conversions.

- **Exercise 5.4: `Employee` with Weak Privacy (`__salary`):**

  - **Goal:** Understand `__double_leading_underscore` (name mangling).
  - **Task:**
    1.  Create an `Employee` class with `name` and `__salary` (private) attributes.
    2.  Add a `get_salary()` method.
    3.  Instantiate an employee and print their salary using `get_salary()`.
    4.  Attempt to access `__salary` directly (it will fail). Then, try to access it using the mangled name (`_Employee__salary`) to see it work, but reflect on why this bypasses encapsulation.

- **Exercise 5.5: `Configuration` Class with Properties:**
  - **Goal:** Apply properties for managing internal configuration values.
  - **Task:**
    1.  Create a `Configuration` class with internal protected attributes `_database_url` and `_api_key`.
    2.  Implement `@property` getters for both (`database_url`, `api_key`).
    3.  Implement setters for both, with simple validation (e.g., ensure `api_key` is a non-empty string).
    4.  Create a configuration object, set some values, and then try to set an invalid value to observe the validation.

---

### **Phase 2: Pillars of OOP**

#### 1. **Inheritance:**

- **Exercise 6.1: Basic `Shape` Hierarchy:**

  - **Goal:** Practice basic single inheritance.
  - **Task:**
    1.  Create a `Shape` class with a `color` attribute and a `describe()` method.
    2.  Create a `Circle` class that inherits from `Shape`. Add a `radius` attribute.
    3.  Override the `describe()` method in `Circle` to include radius information.
    4.  Create a `Circle` object and call its `describe()` method.

- **Exercise 6.2: `Vehicle` and `Car` with `super().__init__()`:**

  - **Goal:** Use `super()` to call the parent's constructor.
  - **Task:**
    1.  Create a `Vehicle` class with `brand` and `year` in its `__init__`.
    2.  Create a `Car` class that inherits from `Vehicle`.
    3.  In `Car`'s `__init__`, add `model` as an argument. Use `super().__init__()` to initialize `brand` and `year`.
    4.  Add a `display_info()` method to `Car` that prints all its details (brand, year, model).
    5.  Create a `Car` object and display its info.

- **Exercise 6.3: `Animal` and `Mammal` extending Behavior:**

  - **Goal:** Override and extend parent methods using `super()`.
  - **Task:**
    1.  Create an `Animal` class with a `move()` method that prints "Animal moves."
    2.  Create a `Mammal` class that inherits from `Animal`.
    3.  Override `move()` in `Mammal` to first call `super().move()` and then print "Mammal walks on land."
    4.  Create an `Animal` and a `Mammal` object and call their `move()` methods to observe the different outputs.

- **Exercise 6.4: `Electronics` and `Smartphone` Hierarchy:**

  - **Goal:** Practice multi-level inheritance with attribute inheritance.
  - **Task:**
    1.  Define an `Electronics` class with `brand` and `price`.
    2.  Define a `PortableDevice` class that inherits from `Electronics` and adds a `battery_life_hours` attribute.
    3.  Define a `Smartphone` class that inherits from `PortableDevice` and adds an `operating_system` attribute.
    4.  Add a `display_specs()` method to `Smartphone` that shows all inherited and its own attributes.
    5.  Create a `Smartphone` object and call `display_specs()`.

- **Exercise 6.5: Simple `Logger` with Level Inheritance:**

  - **Goal:** Use inheritance for specialized functionality.
  - **Task:**
    1.  Create a base `Logger` class with a `log(message)` method that simply prints the message.
    2.  Create an `InfoLogger` that inherits from `Logger` and overrides `log` to prefix messages with `"[INFO] "`.
    3.  Create an `ErrorLogger` that inherits from `Logger` and overrides `log` to prefix messages with `"[ERROR] "`.
    4.  Create instances of each logger and log some messages.

- **Exercise 6.6: Multiple Inheritance (Cautious Use) - `Artist` and `Musician`:**
  - **Goal:** Understand the mechanics of multiple inheritance and MRO.
  - **Task:**
    1.  Create a `Person` class with a `name` attribute.
    2.  Create an `Artist` class with a `create_art()` method.
    3.  Create a `Musician` class with a `play_instrument()` method.
    4.  Create a `Performer` class that inherits from both `Artist` and `Musician`.
    5.  Add a `stage_performance()` method to `Performer` that calls methods from both parent classes.
    6.  Instantiate a `Performer` and demonstrate their abilities.
    7.  (Self-reflection): Consider if there are any methods with the same name in `Artist` and `Musician`. What happens if you call it on `Performer`? How would you check the MRO?

#### 2. **Polymorphism:**

- **Exercise 7.1: `Animal` Sounds (Duck Typing):**

  - **Goal:** Practice basic duck typing.
  - **Task:**
    1.  Define classes `Dog`, `Cat`, and `Duck`. Each should have a `make_sound()` method that prints its specific sound.
    2.  Create a function `animal_parade(animals_list)` that iterates through a list of arbitrary objects and calls `make_sound()` on each.
    3.  Create a list containing instances of `Dog`, `Cat`, and `Duck`, and pass it to `animal_parade()`. Observe the polymorphic behavior.

- **Exercise 7.2: `PaymentProcessor` (Polymorphic Methods):**

  - **Goal:** Apply polymorphism to process different types of payments.
  - **Task:**
    1.  Define a `CreditCardPayment` class with a `process_payment(amount)` method.
    2.  Define a `PayPalPayment` class with a `process_payment(amount)` method.
    3.  Define a `BankTransferPayment` class with a `process_payment(amount)` method.
    4.  Each `process_payment` should print a message indicating how the payment was processed (e.g., "Processing credit card payment of $X").
    5.  Create a list of different payment objects and iterate through them, calling `process_payment()` on each.

- **Exercise 7.3: Flexible `Greeter` with Default Arguments:**

  - **Goal:** Achieve "method overloading" using default arguments.
  - **Task:**
    1.  Create a `Greeter` class with a single method `greet(name="Guest", formality="casual")`.
    2.  Inside `greet`, use `if/elif/else` to print different greetings based on `formality` (e.g., "Hi, \[name]!" for casual, "Good day, \[name]." for formal).
    3.  Call `greet()` with: no arguments, only `name`, and both `name` and `formality`.

- **Exercise 7.4: `Reporter` with `*args` and `**kwargs`:\*\*

  - **Goal:** Implement "method overloading" using variable arguments.
  - **Task:**
    1.  Create a `Reporter` class with a method `generate_report(*args, **kwargs)`.
    2.  Inside `generate_report`:
        - If `args` contains a single string, assume it's a simple message and print it.
        - If `kwargs` contains `title` and `content`, print a formatted report.
        - Otherwise, print "Unknown report format."
    3.  Call `generate_report()` in different ways to test these conditions.

- **Exercise 7.5: Drawing Different Shapes (ABC and Polymorphism):**
  - **Goal:** Combine ABCs with polymorphism.
  - **Task:**
    1.  Use the `Drawable` ABC from the previous section (or create a simpler `Shape` ABC with just an `area()` abstract method).
    2.  Create two concrete subclasses (e.g., `Circle`, `Rectangle`) that implement the abstract method(s).
    3.  Create a list containing instances of both `Circle` and `Rectangle`.
    4.  Write a function `print_areas(shapes_list)` that iterates through the list and calls the `area()` method on each, demonstrating polymorphism.

#### 3. **Abstraction:**

- **Exercise 8.1: `Worker` Abstract Base Class:**

  - **Goal:** Define and implement a simple ABC.
  - **Task:**
    1.  Create an `ABC` called `Worker` with an `__init__` that takes `name`.
    2.  Define abstract methods `work()` and `get_salary()`.
    3.  Create concrete subclasses `HourlyWorker` and `SalariedWorker`.
        - `HourlyWorker` needs `hours_worked` and `hourly_rate` attributes, and implements `work()` and `get_salary()`.
        - `SalariedWorker` needs `annual_salary` attribute, and implements `work()` and `get_salary()`.
    4.  Instantiate both types of workers and call their methods. (Try to instantiate `Worker` directly to see the `TypeError`).

- **Exercise 8.2: `DataProcessor` Abstract Interface:**

  - **Goal:** Emphasize the "interface" aspect of ABCs.
  - **Task:**
    1.  Define an `ABC` called `DataProcessor` with abstract methods `load_data(source)` and `process_data(data)`.
    2.  Create concrete subclasses `CSVProcessor` and `JSONProcessor`.
        - `CSVProcessor` implements `load_data` to simulate loading from a CSV (e.g., just print "Loading CSV from \[source]") and `process_data` to print "Processing CSV data: \[data]".
        - `JSONProcessor` does similarly for JSON.
    3.  Write a function `run_processor(processor_instance, source_path, data)` that takes an instance of `DataProcessor` and uses its methods.
    4.  Demonstrate using `run_processor` with both `CSVProcessor` and `JSONProcessor` instances.

- **Exercise 8.3: `Notifier` Abstract Methods:**

  - **Goal:** Define an abstract notification mechanism.
  - **Task:**
    1.  Create an `ABC` called `Notifier` with abstract methods `send_notification(message)` and `get_recipient()`.
    2.  Create subclasses `EmailNotifier` and `SMSNotifier`.
        - `EmailNotifier` should implement `send_notification` by printing an email message and `get_recipient` returning an email address.
        - `SMSNotifier` should implement `send_notification` by printing an SMS message and `get_recipient` returning a phone number.
    3.  Create instances and send notifications.

- **Exercise 8.4: Abstract `Logger` with Levels (Revisit):**

  - **Goal:** Refactor previous logger exercise using ABCs for stronger contract.
  - **Task:**
    1.  Define an `ABC` called `AbstractLogger` with an abstract method `log(level, message)`.
    2.  Create `ConsoleLogger` and `FileLogger` subclasses.
        - `ConsoleLogger` prints the message to the console, prefixed by the `level`.
        - `FileLogger` (simulate) writes the message to a file, prefixed by `level`.
    3.  Use these loggers to log messages at different levels (e.g., "INFO", "WARNING", "ERROR").

- **Exercise 8.5: Abstract `PaymentMethod`:**
  - **Goal:** Apply abstraction to payment processing.
  - **Task:**
    1.  Create an `ABC` called `PaymentMethod` with abstract methods `process_payment(amount)` and `get_currency()`.
    2.  Create subclasses `CreditCard`, `PayPal`, and `Bitcoin`.
        - Each implements `process_payment` (e.g., prints "Processing X amount via Y") and `get_currency` (e.g., returns "USD", "EUR", "BTC").
    3.  Create a list of different `PaymentMethod` instances and call `process_payment` on each.

---

### **Phase 3: Best Practices & Idiomatic Python**

#### 1. **Special Methods (Dunder/Magic Methods - `__method__`)**:

- **Exercise 9.1: `Vector` with `__str__` and `__repr__`:**

  - **Goal:** Implement human-readable and developer-friendly string representations.
  - **Task:**
    1.  Create a `Vector` class with `x` and `y` attributes.
    2.  Implement `__str__` to return a string like `"(x, y)"`.
    3.  Implement `__repr__` to return a string like `f"Vector(x={self.x}, y={self.y})"`.
    4.  Create a `Vector` object, `print()` it, and print its `repr()` output. Put it in a list and print the list.

- **Exercise 9.2: `Point` with Rich Comparisons (`__eq__`, `__lt__`):**

  - **Goal:** Enable comparison operators for custom objects.
  - **Task:**
    1.  Create a `Point` class with `x` and `y` attributes.
    2.  Implement `__eq__` to compare two `Point` objects based on whether both `x` and `y` are equal. Handle `NotImplemented` for non-`Point` types.
    3.  Implement `__lt__` to compare points (e.g., based on x-coordinate, then y-coordinate if x is equal).
    4.  Create several `Point` objects and test `==`, `!=`, `<`, and `>=`.

- **Exercise 9.3: `Playlist` as a Sequence (`__len__`, `__getitem__`, `__iter__`):**

  - **Goal:** Make your class behave like a list/sequence.
  - **Task:**
    1.  Create a `Song` class (simple, `title`, `artist`).
    2.  Create a `Playlist` class that stores a list of `Song` objects internally.
    3.  Implement `__len__` (number of songs).
    4.  Implement `__getitem__` (access song by index `playlist[0]`).
    5.  Implement `__iter__` (allow `for song in playlist:`).
    6.  Implement `__contains__` (allow `"Song Title" in playlist`).
    7.  Create a playlist, add songs, test `len()`, indexing, iteration, and `in` operator.

- **Exercise 9.4: `FileManager` as a Context Manager (`__enter__`, `__exit__`):**

  - **Goal:** Create an object that can be used with the `with` statement.
  - **Task:**
    1.  Create a `FileManager` class that takes a `filename` and `mode` (e.g., 'w', 'r') in its `__init__`.
    2.  Implement `__enter__` to open the file and return the file object.
    3.  Implement `__exit__` to close the file. Handle potential exceptions gracefully (print a message but re-raise).
    4.  Use your `FileManager` with a `with` statement to write to a file and then to read from it. Test with an intentional error inside the `with` block.

- **Exercise 9.5: `Wallet` with `__add__` and `__sub__`:**

  - **Goal:** Overload arithmetic operators.
  - **Task:**
    1.  Create a `Wallet` class with a `balance` attribute.
    2.  Implement `__add__(self, other)` to allow adding two `Wallet` balances or adding a number to a `Wallet`'s balance.
    3.  Implement `__sub__(self, other)` similarly for subtraction.
    4.  Create `Wallet` objects and demonstrate `+` and `-` operations.

- **Exercise 9.6: `Descriptor` for Attribute Access (Advanced):**
  - **Goal:** Explore a powerful dunder method for custom attribute behavior.
  - **Task:**
    1.  Define a `PositiveNumber` descriptor class with `__set_name__`, `__get__`, and `__set__` methods.
    2.  `__set__` should ensure that the value being set is a positive number, raising a `ValueError` otherwise.
    3.  Create a `Product` class and use `PositiveNumber` as a class attribute for `price` and `quantity`.
    4.  Test creating `Product` objects with valid and invalid (e.g., negative) prices/quantities.

#### 2. **Composition over Inheritance:**

- **Exercise 10.1: `Robot` with `MovementSystem` and `Battery`:**

  - **Goal:** Simple composition: `Robot` has a `MovementSystem` and a `Battery`.
  - **Task:**
    1.  Create a `MovementSystem` class with a `move(distance)` method.
    2.  Create a `Battery` class with `level` (e.g., 100) and `consume(amount)` methods.
    3.  Create a `Robot` class. In its `__init__`, it should create instances of `MovementSystem` and `Battery`.
    4.  Implement a `walk(distance)` method in `Robot` that uses its `MovementSystem` and `Battery` (e.g., `battery.consume(distance * 0.1)`).
    5.  Create a `Robot` object and make it walk, checking battery level.

- **Exercise 10.2: `Order` with `OrderItem`s:**

  - **Goal:** Composition of collection of objects.
  - **Task:**
    1.  Create an `Item` class with `name` and `price`.
    2.  Create an `OrderItem` class with `item` (an `Item` object) and `quantity`. It should have a `get_total()` method.
    3.  Create an `Order` class. In its `__init__`, it should have an empty list `_order_items`.
    4.  Add methods `add_item(item, quantity)` (creates an `OrderItem` and adds to list) and `calculate_total_order_price()`.
    5.  Create an `Order`, add several items, and calculate the total.

- **Exercise 10.3: `Computer` with `CPU`, `RAM`, `Storage`:**

  - **Goal:** Show how different components can be swapped out.
  - **Task:**
    1.  Define separate classes for `CPU`, `RAM`, and `Storage` (each with simple attributes like `model`, `size`, `capacity`).
    2.  Define a `Computer` class. Its `__init__` should take instances of `CPU`, `RAM`, and `Storage` as arguments.
    3.  Add a `get_specs()` method to `Computer` that prints details of its components.
    4.  Create different `CPU`, `RAM`, `Storage` objects and combine them to build various `Computer` configurations.

- **Exercise 10.4: `Notifier` using `EmailService` and `SMSService`:**

  - **Goal:** Implement a "strategy" pattern using composition.
  - **Task:**
    1.  Create `EmailService` and `SMSService` classes, each with a `send_message(recipient, message)` method.
    2.  Create a `NotificationSystem` class. Its `__init__` takes a `service` object (either `EmailService` or `SMSService`).
    3.  Add a `notify(recipient, message)` method to `NotificationSystem` that delegates to its internal `service` object.
    4.  Demonstrate how you can switch the `NotificationSystem` to use email or SMS by just passing a different service object during instantiation.

- **Exercise 10.5: `Logger` with `Formatter` and `Handler`:**
  - **Goal:** Complex composition, simulating a real-world logging system.
  - **Task:**
    1.  Create a `Formatter` class with a `format_record(message, level)` method (e.g., returns `f"[{level}] {message}"`).
    2.  Create a `Handler` abstract base class with an abstract `emit(formatted_record)` method.
    3.  Create `ConsoleHandler` and `FileHandler` subclasses for `Handler`.
    4.  Create a `Logger` class. Its `__init__` takes a `formatter` (a `Formatter` object) and a `handler` (a `Handler` object).
    5.  The `Logger` should have `info(message)` and `error(message)` methods that use the `formatter` to format the message and then the `handler` to emit it.
    6.  Create a `Logger` with a `ConsoleHandler` and a `FileHandler` (you might need two logger instances or a list of handlers for one logger) to see formatted output go to different destinations.

#### 3. **Immutability (and When to Use It):**

- **Exercise 11.1: Immutable `Color` with `namedtuple`:**

  - **Goal:** Create a simple immutable data structure.
  - **Task:**
    1.  Define an immutable `Color` type using `collections.namedtuple` with attributes `red`, `green`, `blue`.
    2.  Create a `Color` object.
    3.  Try to change one of its attributes (e.g., `color.red = 255`) and observe the error.
    4.  Print the `Color` object.

- **Exercise 11.2: Immutable `Configuration` with `dataclasses(frozen=True)`:**

  - **Goal:** Use dataclasses for more complex immutable objects with defaults.
  - **Task:**
    1.  Define an immutable `Config` class using `@dataclass(frozen=True)`.
    2.  Give it attributes `api_key` (str, no default), `log_level` (str, default "INFO"), `max_retries` (int, default 3).
    3.  Create a `Config` object, providing only the `api_key`.
    4.  Print all attributes. Try to modify `log_level` and observe the error.

- **Exercise 11.3: `Money` Object for Calculations:**

  - **Goal:** Create an immutable value object.
  - **Task:**
    1.  Create an `@dataclass(frozen=True)` called `Money` with `amount: float` and `currency: str`.
    2.  Implement `__add__` to allow adding two `Money` objects, but only if they have the same currency (otherwise, raise a `ValueError`). The result should be a _new_ `Money` object.
    3.  Implement `__eq__` for comparison.
    4.  Test adding valid and invalid `Money` objects.

- **Exercise 11.4: Immutable `Timestamp`:**

  - **Goal:** Represent a point in time immutably.
  - **Task:**
    1.  Create an `@dataclass(frozen=True)` `Timestamp` with `year`, `month`, `day`, `hour`, `minute`, `second`.
    2.  Implement `__lt__` and `__gt__` so `Timestamp` objects can be compared chronologically.
    3.  Create several `Timestamp` objects and demonstrate comparisons.

- **Exercise 11.5: `Point` with Custom `__setattr__` (More Control):**
  - **Goal:** Manually enforce immutability for a class if `dataclasses` isn't suitable.
  - **Task:**
    1.  Create a `Point` class with `x` and `y` attributes.
    2.  In `__init__`, use `object.__setattr__(self, 'attribute', value)` to set the initial values.
    3.  Override `__setattr__` to raise an `AttributeError("Cannot modify attributes of immutable object")` after initialization.
    4.  Create a `Point` object and verify that its attributes cannot be changed.

#### 4. **Error Handling with Custom Exceptions:**

- **Exercise 12.1: `InvalidEmailError`:**

  - **Goal:** Basic custom exception.
  - **Task:**
    1.  Define a custom exception `InvalidEmailError` that inherits from `ValueError`.
    2.  Create a `UserRegistration` class with a `register_user(username, email)` method.
    3.  Inside `register_user`, if the email does not contain both `@` and `.` (simple validation), raise `InvalidEmailError`.
    4.  Test the registration with valid and invalid emails, catching `InvalidEmailError`.

- **Exercise 12.2: `InsufficientFundsError` for `BankAccount`:**

  - **Goal:** Pass contextual data with custom exceptions.
  - **Task:**
    1.  Define `InsufficientFundsError` inheriting from `Exception`. Its `__init__` should take `amount_to_withdraw` and `current_balance`.
    2.  Modify the `BankAccount` `withdraw` method from Exercise 5.1. Instead of just printing, raise `InsufficientFundsError` if funds are insufficient, passing the relevant amounts.
    3.  Catch the custom exception and print a user-friendly message using the exception's attributes.

- **Exercise 12.3: `ProductNotFoundException`:**

  - **Goal:** Raise custom exceptions for specific business logic errors.
  - **Task:**
    1.  Define `ProductNotFoundException(Exception)` that takes a `product_id`.
    2.  Create an `Inventory` class that stores products in a dictionary (`product_id: product_object`).
    3.  Implement a `get_product(product_id)` method. If the product is not found, raise `ProductNotFoundException`.
    4.  Test getting existing and non-existing products, handling the exception.

- **Exercise 12.4: `InvalidInputError` with Detailed Message:**

  - **Goal:** Create a flexible custom exception for various input issues.
  - **Task:**
    1.  Define `InvalidInputError(ValueError)` that takes a `field_name` and `reason` in its `__init__`.
    2.  Override `__str__` for `InvalidInputError` to provide a message like `f"Invalid input for {self.field_name}: {self.reason}"`.
    3.  Create a `UserProfile` class with methods like `set_age(age)` and `set_phone(phone_number)`.
    4.  In these setters, raise `InvalidInputError` for invalid inputs (e.g., negative age, non-digit phone number).
    5.  Test with various invalid inputs and catch the `InvalidInputError`.

- **Exercise 12.5: Chained Exceptions with `raise from`:**
  - **Goal:** Understand how to chain exceptions for better debugging.
  - **Task:**
    1.  Define a custom exception `DatabaseError(Exception)`.
    2.  Define another custom exception `DataImportError(Exception)`.
    3.  Simulate a `Database` class with a `save_data(data)` method that _might_ raise a `TypeError` (e.g., if `data` is not a dictionary).
    4.  Create a `DataImporter` class with an `import_data(data)` method. Inside this method, call `database.save_data(data)`.
    5.  If `database.save_data` raises a `TypeError`, catch it and _re-raise_ a `DataImportError` **from** the original `TypeError` (using `raise DataImportError(...) from original_exception`).
    6.  Demonstrate the chained exception by calling `import_data` with invalid data and catching `DataImportError`. Print the traceback to see the "During handling of the above exception..." message.

#### 5. **Type Hinting:**

- **Exercise 13.1: Type Hinting for `Calculator` Methods:**

  - **Goal:** Apply basic type hints to function parameters and return values.
  - **Task:**
    1.  Take your `MathOperations` class from Exercise 4.1.
    2.  Add type hints to all method parameters (e.g., `a: int`, `b: float`) and return types (e.g., `-> float`).
    3.  Run a static type checker (like MyPy, if you have it set up) to ensure no errors.
    4.  (Self-reflection): Briefly explain how type hints improve readability for someone else looking at your `MathOperations` class.

- **Exercise 13.2: Class Attributes with Type Hints:**

  - **Goal:** Add type hints to class and instance attributes.
  - **Task:**
    1.  Create a `Product` class with `name: str`, `price: float`, and `stock: int` attributes.
    2.  Add type hints to its `__init__` method.
    3.  Add type hints to an instance method (e.g., `is_available(self, quantity: int) -> bool`).
    4.  Add a class variable `currency_symbol: str = "$"` with its type hint.

- **Exercise 13.3: Optional and Union Types:**

  - **Goal:** Use `Optional` and `Union` for flexible type hints.
  - **Task:**
    1.  Create a `Contact` class with `name: str`.
    2.  Add an `email: Optional[str] = None` attribute with a type hint for optional string.
    3.  Add a `phone: Union[str, int, None] = None` attribute with a type hint for a string, integer, or None.
    4.  Create contacts with different combinations of email and phone, and show how the hints work.

- **Exercise 13.4: List and Dictionary Type Hints:**

  - **Goal:** Hinting for collections.
  - **Task:**
    1.  Create a `Library` class.
    2.  It should have an attribute `books: List[str]` (a list of book titles).
    3.  It should have an attribute `borrowed_by: Dict[str, str]` (a dictionary mapping book titles to borrower names).
    4.  Add methods `add_book(title: str)`, `borrow_book(title: str, borrower: str)`, `return_book(title: str)`.
    5.  Add appropriate return type hints for these methods (e.g., `-> None`, `-> bool`).

- **Exercise 13.5: Return Type Hints for Complex Objects:**
  - **Goal:** Hinting for returning instances of other classes.
  - **Task:**
    1.  Create a `Date` class (year, month, day).
    2.  Create a `Calendar` class.
    3.  Add a method `get_today() -> Date` that returns a `Date` object representing the current day.
    4.  Add a method `get_date_info(year: int, month: int, day: int) -> Tuple[int, str, bool]` that returns a tuple (day_of_week_number, month_name, is_leap_year). (You'll need `datetime` module for current date and `calendar` module for info).

#### 6. **Design Patterns (Introductory):**

- **Exercise 14.1: Simple Factory Method for `Animal`:**

  - **Goal:** Understand the basic idea of a factory function/method.
  - **Task:**
    1.  Revisit your `Dog` and `Cat` classes from earlier.
    2.  Create a `AnimalFactory` class with a static method `create_animal(type: str, name: str)` that returns an instance of `Dog` or `Cat` based on the `type` string. Raise `ValueError` for unknown types.
    3.  Use the factory to create animals.

- **Exercise 14.2: Strategy Pattern for Tax Calculation:**

  - **Goal:** Implement interchangeable algorithms using composition.
  - **Task:**
    1.  Create an `ABC` `TaxStrategy` with an abstract method `calculate_tax(amount: float) -> float`.
    2.  Create concrete strategies `USTaxStrategy` (e.g., 5% tax) and `EuropeanTaxStrategy` (e.g., 20% tax).
    3.  Create an `Invoice` class. Its `__init__` takes an `amount` and a `tax_strategy: TaxStrategy` object.
    4.  Add a `get_total()` method to `Invoice` that uses the injected `tax_strategy` to calculate total.
    5.  Create invoices with different tax strategies and observe the different totals.

- **Exercise 14.3: Iterator Pattern for Custom Range:**

  - **Goal:** Understand `__iter__` and `__next__` for custom iterators.
  - **Task:**
    1.  Create a class `MyRange` that works similar to Python's `range()` (takes `start`, `end`, `step`).
    2.  Implement `__iter__` to return `self`.
    3.  Implement `__next__` to return the next number in the sequence and raise `StopIteration` when done.
    4.  Use your `MyRange` in a `for` loop.

- **Exercise 14.4: Observer Pattern (Basic Notification System):**

  - **Goal:** Implement basic publish-subscribe.
  - **Task:**
    1.  Create an `ABC` `Observer` with an abstract `update(message)` method.
    2.  Create a `Subject` class (or `Publisher`). It should maintain a list of `observers`.
    3.  `Subject` needs `attach(observer)`, `detach(observer)`, and `notify(message)` methods. `notify` calls `update` on all attached observers.
    4.  Create concrete `EmailNotifier` and `SMSNotifier` classes that implement `Observer` and print their respective notifications.
    5.  Create a `Subject`, attach both notifiers, and `notify` them. Detach one and notify again.

- **Exercise 14.5: Singleton Pattern (Module-Level is Idiomatic):**
  - **Goal:** Understand how Python typically handles singletons (often implicitly).
  - **Task:**
    1.  **Non-idiomatic way (for learning):** Create a class `ConfigManager` and implement a basic Singleton pattern using `__new__` (checking if `_instance` already exists).
    2.  **Idiomatic way:** Instead of the class, create a Python module `my_settings.py`. Inside it, define a dictionary `SETTINGS = {"debug_mode": True, "log_file": "app.log"}`.
    3.  In another file, `import my_settings`. Show that `my_settings.SETTINGS` is the _same object_ wherever it's imported (e.g., `id(my_settings.SETTINGS)`).
    4.  Reflect on why the module-level approach is often preferred in Python for simple singletons compared to complex `__new__` implementations.

---

This extensive list should keep you busy and progressively build your OOP skills in Python. Remember to test your code thoroughly and refer back to the explanations in the roadmap as you work through these!
