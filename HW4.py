# 1
print("#1")


class Vehicle:
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
SchoolBus = Bus(80, 14235)
print(isinstance(SchoolBus, Bus), isinstance(SchoolBus, Vehicle))

# 5
print("#5")


class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def shool_adress(self):
        print('Cursor education')

    def main_subject(self):
        print('Main')


# 6
print("#6")


class SchoolBus2(Bus, School):
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


class Bear:
    def __init__(self):
        pass

    def eat(self):
        print('Bear eat')


Bear()


class Wolf:
    def __init__(self):
        pass

    def eat(self):
        print('Wolf eat')


Wolf()

bear = Bear()

wolf = Wolf()

for Animal in (bear, wolf):
    Animal.eat()

# 8*
print("#8*\n")


class City:
    def __new__(cls, name: str, population: int):

        if population > 1500:
            cls.name = name
            cls.population = population
            return super(City, cls).__new__(cls)
            # return print(f'{name} has {population} inhabitants')
        else:
            return print(f'The {name} is too small')

    def info(self):
        print(f'{self.name} has {self.population} inhabitants')


Lutsk = City('Lutsk', 1501)
Lutsk.info()

Kovel = City('Kovel', 1200)
Kovel.info()
