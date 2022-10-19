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


class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self):
        pass


print(issubclass(Bus, Vehicle))

School_bus = Bus(80, 14235)

print(isinstance(School_bus, Bus), isinstance(School_bus, Vehicle))


class School():
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_adress(self):
        print('Cursor education')

    def main_subject(self):
        print('Main')


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

    def info(self):
        print('School id is -', self.get_school_id)
        print('Number of students is -', self.number_of_students)
        print('Max speed for bus is -', self.max_speed)
        print('His mileage is -', self.mileage)


kBus = school_bus2(1, 300, 80, 12312)
kBus.info()


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
