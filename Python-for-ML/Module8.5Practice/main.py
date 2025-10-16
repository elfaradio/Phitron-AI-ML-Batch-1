class Vehicle:
    def __init__(self, typ, name, speed):
        self.typ = typ
        self._name = name
        self.__speed = speed

    def classify(self):
        if self.__speed > 100:
            return "High-speed Vehicle"
        else:
            return "Normal Vehicle"

    def show_info(self):
        print(f"{self.typ} {self._name}  {self.__speed}")

    def get_speed(self):
        return self.__speed

    def get_name(self):
        return self._name


class Car(Vehicle):
    def __init__(self, typ, name, speed):
        super().__init__(typ, name, speed)

    def show_info(self):
        print(
            f"Type:{self.typ} Name:{self._name}  Speed:{self.get_speed()}KM/H {self.classify()}")


class Bike(Vehicle):
    def __init__(self, typ, name, speed):
        super().__init__(typ, name, speed)

    def show_info(self):
        print(
            f"Type:{self.typ} Name:{self._name}  Speed:{self.get_speed()}KM/H {self.classify()}")


n = int(input())
lst = []

db = []
for _ in range(n):
    s = input().split()
    # print(s[0])
    lst.append(s)

for i in lst:

    typ = i[0].capitalize()

    if typ == "Car":
        cr = Car(typ, i[1].capitalize(), int(i[2]))
        print(f"Car Addeded: {cr.get_name()}")
        db.append(cr)
    elif typ == "Bike":
        bk = Bike(typ, i[1].capitalize(), int(i[2]))
        print(f"Bike Addeded: {bk.get_name()}")
        db.append(bk)
    else:
        pass


print()
print()

print("---Vehicle Details ---")


for i in db:
    (i.show_info())
