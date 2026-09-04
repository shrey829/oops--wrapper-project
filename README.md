# oops--wrapper-project
employee management system
# Employee Management System

A simple **Employee Management System** built in Python using **Object-Oriented Programming (OOP)** concepts.

This project demonstrates **classes, inheritance, encapsulation, method overriding, constructors, getters/setters, and destructors**.

## Features

The program provides the following options:

1. Create Person
2. Create Employee
3. Create Manager
4. Create Developer
5. Show Details
6. Exit

### Person

* Stores name and age.
* Provides a `display()` method to show personal information.

### Employee

* Inherits from `Person`.
* Stores:

  * Employee ID
  * Salary
* Uses `_employee_id` to demonstrate encapsulation.
* Provides getter and setter methods for the employee ID.
* Overrides the `display()` method.
* Contains a destructor using `__del__()`.

### Manager

* Inherits from `Employee`.
* Stores the manager's department.
* Overrides the `display()` method.

### Developer

* Inherits from `Employee`.
* Stores the developer's programming language.
* Overrides the `display()` method.

## OOP Concepts Used

### 1. Inheritance

The project uses multiple levels of inheritance:

```text
Person
  |
Employee
 /      \
Manager  Developer
```

* `Employee` inherits from `Person`.
* `Manager` inherits from `Employee`.
* `Developer` inherits from `Employee`.

### 2. Encapsulation

The employee ID is stored as:

```python
self._employee_id
```

Getter and setter methods are provided:

```python
def get_employee_id(self):
    return self._employee_id

def set_employee_id(self, employee_id):
    self._employee_id = employee_id
```

### 3. Method Overriding

`Employee`, `Manager`, and `Developer` each provide their own implementation of `display()`.

For example:

```python
def display(self):
    super().display()
    print(f"Department: {self.department}")
```

### 4. `super()`

The `super()` function is used to call methods and constructors from the parent class.

Example:

```python
super().__init__(name, age, employee_id, salary)
```

### 5. Constructor

Each class uses `__init__()` to initialize its attributes.

### 6. Destructor

The `Employee` class contains:

```python
def __del__(self):
    print(
        f"Employee {self.name} with ID "
        f"{self._employee_id} has been deleted."
    )
```

The destructor is called when the object is being destroyed by Python.

## Employee ID Validation

The program checks whether an employee ID already exists before creating:

* Employee
* Manager
* Developer

This prevents duplicate employee IDs.

## How to Run

Make sure Python is installed on your system.

Check your Python version:

```bash
python --version
```

Run the program:

```bash
python employee_management.py
```

Depending on your system, you may need:

```bash
python3 employee_management.py
```

## Example

```text
oops-wrapper-project
employee --management --system
1. create person
2. create employee
3. create manager
4. create developer
5. show details
6. exit

Enter your choice (1-6): 2
Enter employee ID: E101
Enter name: John
Enter age: 25
Enter salary: 50000

Employee created successfully.
```

Displaying the employee:

```text
Enter your choice (1-6): 5
Enter type (person/employee/manager/developer): employee
Enter ID of employee: E101

Name: John, Age: 25
Employee ID: E101, Salary: 50000.0
```

## Project Structure

A simple project structure can be:

```text
employee-management-system/
│
├── employee_management.py
└── README.md
```

## Future Improvements

Possible improvements include:

* Add employee deletion functionality.
* Add search by employee name.
* Add update employee information.
* Add input validation using `try-except`.
* Prevent negative ages and salaries.
* Store employee information in a file or database.
* Add a graphical user interface (GUI).
* Refactor repeated code into reusable functions.
* Add unit tests.

## Technologies Used

* **Python 3**
* Object-Oriented Programming

## Author
shrey shah

Created as a Python OOP practice project.

