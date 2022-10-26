# 1
print("#1")


class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print('increase speed')

    def break_speed(self):
        print('break speed')

    def mileage_info(self):
        print('mileage')


# 2
print("#2")


class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self):
        pass


# 3
print("#3")
print(issubclass(Bus, Vehicle))

# 4
print("#4")
School_bus = Bus(80, 14235)
print(isinstance(School_bus, Bus), isinstance(School_bus, Vehicle))


# 5
print("#5")

class School():
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_adress(self):
        print('Cursor education')

    def main_subject(self):
        print('Main')

#6
print("#6")
class school_bus2(Bus, School):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage):
        # super().__init__(max_speed, mileage)
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage)
        # self.max_speed = max_speed
        # self.mileage = mileage
        # self.get_school_id = get_school_id
        # self.number_of_students = number_of_students

        pass

    def bus_school_color(self):
        print("school bus color")

    def info(self):
        print('School id is -', self.get_school_id)
        print('Number of students is -', self.number_of_students)
        print('Max speed for bus is -', self.max_speed)
        print('His mileage is -', self.mileage)


# 7
print("#7")
class bear():
    def __init__(self):
        pass

    def eat(self):
        print('Bear eat')


bear()


class wolf():
    def __init__(self):
        pass

    def eat(self):
        print('Wolf eat')


wolf()

Bear = bear()

Wolf = wolf()

for animal in (Bear, Wolf):
    animal.eat()

# 8*
print("#8*")


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __lt__(self, other=1500):
        if other < self.population:
            return f'{self.name} has {self.population} inhabitants.'
        else:
            return 'Your city is too small'


Lutsk = City('Lutsk', 1600)
Kovel = City('Kyiv', 1200)
print(Lutsk.__lt__())
print(Kovel.__lt__())
