print("oops-wrapper-project")
print("employee --management --system")
print("1. create person")
print("2. create employee")
print("3. create manager")
print("4. create developer")
print("5. show details")
print("6. exit")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self._employee_id = employee_id
        self.salary = salary

    def display(self):
        super().display()
        print(f"Employee ID: {self._employee_id}, Salary: {self.salary}")

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def __del__(self):
        print(
            f"Employee {self.name} with ID "
            f"{self._employee_id} has been deleted."
        )


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(
        self, name, age, employee_id, salary, programming_language
    ):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


employees = []


while True:
    choice = input("Enter your choice (1-6): ")

    # Create Person
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        person = Person(name, age)
        employees.append(person)

        print("Person created successfully.")

    # Create Employee
    elif choice == "2":
        employee_id = input("Enter employee ID: ")

        # Check duplicate ID
        duplicate = False

        for i in employees:
            if isinstance(i, Employee):
                if i.get_employee_id() == employee_id:
                    duplicate = True
                    break

        if duplicate:
            print("Employee ID already exists. Please enter a unique ID.")
        else:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))

            employee = Employee(
                name, age, employee_id, salary
            )

            employees.append(employee)
            print("Employee created successfully.")

    # Create Manager
    elif choice == "3":
        employee_id = input("Enter employee ID: ")

        duplicate = False

        for i in employees:
            if isinstance(i, Employee):
                if i.get_employee_id() == employee_id:
                    duplicate = True
                    break

        if duplicate:
            print("Employee ID already exists. Please enter a unique ID.")
        else:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            department = input("Enter department: ")

            manager = Manager(
                name,
                age,
                employee_id,
                salary,
                department
            )

            employees.append(manager)
            print("Manager created successfully.")

    # Create Developer
    elif choice == "4":
        employee_id = input("Enter employee ID: ")

        duplicate = False

        for i in employees:
            if isinstance(i, Employee):
                if i.get_employee_id() == employee_id:
                    duplicate = True
                    break

        if duplicate:
            print("Employee ID already exists. Please enter a unique ID.")
        else:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            programming_language = input(
                "Enter programming language: "
            )

            developer = Developer(
                name,
                age,
                employee_id,
                salary,
                programming_language
            )

            employees.append(developer)
            print("Developer created successfully.")

    # Show details
    elif choice == "5":
        if not employees:
            print("No employees or persons to display.")
        else:
            c = input(
                "Enter type "
                "(person/employee/manager/developer): "
            ).lower()

            d = input("Enter ID of employee: ")

            found = False

            if c == "person":
                for i in employees:
                    if type(i) == Person:
                        i.display()
                        found = True

            elif c == "employee":
                for i in employees:
                    if (
                        type(i) == Employee
                        and i.get_employee_id() == d
                    ):
                        i.display()
                        found = True

            elif c == "manager":
                for i in employees:
                    if (
                        isinstance(i, Manager)
                        and i.get_employee_id() == d
                    ):
                        i.display()
                        found = True

            elif c == "developer":
                for i in employees:
                    if (
                        isinstance(i, Developer)
                        and i.get_employee_id() == d
                    ):
                        i.display()
                        found = True

            else:
                print("Invalid employee type.")

            if not found and c in [
                "employee",
                "manager",
                "developer"
            ]:
                print("No matching employee found.")

    # Exit
    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")