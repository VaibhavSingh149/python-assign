#--------------easy-----------------
#basic class design
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Example usage:
rect = Rectangle(5, 10)
print(rect.area())        # Output: 50
print(rect.perimeter())   # Output: 30


#counter class
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0

# Example usage:
counter = Counter()
counter.increment()
counter.increment()
print(counter.value)  # Output: 2
counter.decrement()
print(counter.value)  # Output: 1
counter.reset()
print(counter.value)  # Output: 0



#--------------medium-------------
#vehicle base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel_type = fuel_type

# Example usage:
car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(car.make)   # Output: "Toyota"
print(car.doors)  # Output: 4


#Bank account class 
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Example usage:
account = BankAccount("123456", 1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(200)
print(account.get_balance())  # Output: 1300
print(account.get_account_number())  # Output: "123456"

# Direct access is discouraged and will not work correctly
try:
    account.__balance = 2000  # This does not modify the real private attribute
    print(account.get_balance())  # Still returns 1300
except AttributeError:
    print("Cannot directly access private attribute")
