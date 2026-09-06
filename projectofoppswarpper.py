
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    @classmethod
    def create_person(cls):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        return cls(name, age)


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)

        # Private attributes
        self.__employee_id = employee_id
        self.__salary = salary

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"Employee ID: {self.get_employee_id()}, "
            f"Salary: {self.get_salary()}"
        )

    @classmethod
    def create_employee(cls):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        employee_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))

        return cls(name, age, employee_id, salary)

    # Getter for employee ID
    def get_employee_id(self):
        return self.__employee_id

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        self.__salary = salary

    def __del__(self):
        print(
            f"Employee {self.name} with ID "
            f"{self.get_employee_id()} has been deleted."
        )


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"Department: {self.department}"
        )

    @classmethod
    def create_manager(cls):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        employee_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        department = input("Enter department: ")

        return cls(
            name,
            age,
            employee_id,
            salary,
            department
        )


class Developer(Employee):
    def __init__(
        self,
        name,
        age,
        employee_id,
        salary,
        programming_language
    ):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"Programming Language: {self.programming_language}"
        )

    @classmethod
    def create_developer(cls):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        employee_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        programming_language = input(
            "Enter programming language: "
        )

        return cls(
            name,
            age,
            employee_id,
            salary,
            programming_language
        )


# List to store all objects
employee = []


while True:
    print("\n1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Create Developer")
    print("5. Show Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        person = Person.create_person()
        employee.append(person)

    elif choice == "2":
        employee_id = input("Enter employee ID: ")

        # Check duplicate ID
        duplicate = False

        for i in employee:
            if isinstance(i, Employee):
                if i.get_employee_id() == employee_id:
                    duplicate = True
                    break

        if duplicate:
            print(
                "Employee ID already exists. "
                "Please enter a unique ID."
            )
        else:
            emp = Employee.create_employee()
            employee.append(emp)

    elif choice == "3":
        employee_id = input("Enter employee ID: ")

        # Check duplicate ID
        duplicate = False

        for i in employee:
            if isinstance(i, Employee):
                if i.get_employee_id() == employee_id:
                    duplicate = True
                    break

        if duplicate:
            print(
                "Employee ID already exists. "
                "Please enter a unique ID."
            )
        else:
            manager = Manager.create_manager()
            employee.append(manager)

    elif choice == "4":
        employee_id = input("Enter employee ID: ")

        # Check duplicate ID
        duplicate = False

        for i in employee:
            if isinstance(i, Employee):
                if i.get_employee_id() == employee_id:
                    duplicate = True
                    break

        if duplicate:
            print(
                "Employee ID already exists. "
                "Please enter a unique ID."
            )
        else:
            developer = Developer.create_developer()
            employee.append(developer)

    elif choice == "5":

        if len(employee) == 0:
            print("No records found.")

        else:
            d = int(
                input(
                    "Enter 1 for employees, "
                    "2 for developers, "
                    "3 for managers: "
                )
            )

            if d == 1:
                for obj in employee:
                    if (
                        isinstance(obj, Employee)
                        and not isinstance(obj, Manager)
                        and not isinstance(obj, Developer)
                    ):
                        print(obj)

            elif d == 2:
                for obj in employee:
                    if (
                        isinstance(obj, Developer)
                        and issubclass(Developer, Employee)
                    ):
                        print(obj)

            elif d == 3:
                for obj in employee:
                    if (
                        isinstance(obj, Manager)
                        and issubclass(Manager, Employee)
                    ):
                        print(obj)

            else:
                print("Invalid choice.")

    elif choice == "6":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")
