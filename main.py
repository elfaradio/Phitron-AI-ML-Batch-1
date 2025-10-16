# Getter and Setter MEthods
class Person:
    def __init__(self, name, age, balance):
        self.name = name  # public variables
        self._age = age  # protected variables -> Child class access
        self.__balance = balance  # private -> only nijer class

    def info(self):
        print("Balance ", self.__balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self, money):
        self.__balance += money

# bayrer method


def get_name(person):
    return person.name


person1 = Person("Rakib", 20, 10000)
person1.set_balance(500)
print(person1.name)
print(get_name(person1))
