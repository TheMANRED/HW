import dataclasses
import collections


# 1.
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """

class Laptop:
    def __init__(self):
        device_1 = Battery('99%')
        device_2 = Battery('40%')
        self.laptop = [device_1.state, device_2.state]


class Battery:
    def __init__(self, state):
        self.state = state


laptop = Laptop()
print(laptop.laptop)


# 2.
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """

class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self, size):
        self.size = size


string = GuitarString('30 inch')
rock_guitar = Guitar(string)


# 3
# class Calc:
#     """
#     Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
#     """

class Calc:

    def __init__(self):
        self.sum = 0

    def add_nums(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.sum = self.num1 + self.num2 + self.num3
        return self.sum


calc1 = Calc()
print(calc1.add_nums(150, 5, 7))


# 4*.
# class Pasta:
#     """
#     Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
#     Він повинен мати 2 методи:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """

class Pasta:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon, parmesan, eggs'])


pasta1 = Pasta(["tomato, cucumber"])
print(pasta1.ingredients)

pasta2 = Pasta.bolognaise()
print(pasta2.ingredients)

pasta3 = Pasta.carbonara()
print(pasta3.ingredients)


# *5.1
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """

class Concert:
    def __init__(self, max_visitors_num):
        self.max_visitors_num = max_visitors_num

    def visitors_count(self, visitors_count):
        if self.max_visitors_num < visitors_count:
            visitors_count = self.max_visitors_num
            return self.max_visitors_num
        else:
            return visitors_count


concert = Concert(50)
print(concert.visitors_count(30))

#*5.2

class Concert:
    max_visitor_num = None

    def __setattr__(self, key, value):
        if key == "visitors_count" and value < self.max_visitor_num:
            return object.__setattr__(self, key, value)
        else:
            return object.__setattr__(self, key, self.max_visitor_num)


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 30
print(concert.visitors_count)


# 6.
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
#     """


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


# 7. Create the same class (6) but using NamedTuple

AddressBookDataClassTuple = collections.namedtuple('AddressBookDataClass',
                                                   ['key', 'name', 'phone_number', 'address', 'email', 'birthday',
                                                    'age'])


# 8.
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='',
#     email='', birthday= '', age='')
#     """

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def address_book_info(self):
        return (
            f"AddressBook (key='{self.key}', name='{self.name}', phone_number='{self.phone_number}', address='{self.address}', "
            f"email='{self.email}', birthday='{self.birthday}', age='{self.age}'")


book = AddressBook(0, 'Ukrainochka', 102, 'State Ukraine', 'Ukrainochka@mail.com', '24.08.1991', 31)
print(book.address_book_info())


# 9.
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"

class Person:
    name = "John"
    age = 36
    country = "USA"


human = Person
print(human.age)
human.age = 20
print(human.age)
Person.age = 15
print(Person.age)

# 10.
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
# 
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
        
 # Не зрозумів суті завдання. Напишіть у коментарі що від мене вимагається.
