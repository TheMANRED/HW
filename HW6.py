# 1

print('\n#1\n')


class Iterator:

    def __init__(self, num):
        self.num = num
        self.number = 0
        self.a = 0
        self.b = 1
        self.c = self.a + self.b

    def __iter__(self):
        return self

    def __next__(self):
        if self.number >= self.num:
            raise StopIteration
        elif self.number == 0:
            self.number += 1
            return 0
        elif self.number == 1:
            self.number += 1
            return 1
        else:
            self.c = self.a + self.b
            self.a = self.b
            self.b = self.c
            self.number += 1
        return self.b


for i in Iterator(10):
    print(i)

# 2

print('\n#2\n')


def generator(num):
    a = 0
    b = 1
    c = a + b
    for i in range(num):

        if i >= num:
            break
        elif i == 0:
            yield 0
            i += 1
        elif i == 1:
            yield 1
            i += 1
        else:
            c = a + b
            a = b
            b = c
            yield b
            i += 1


for elem in generator(10):
    print(elem)

#3
print('\n#3\n')

g = (number * number for number in range(10))
for elem in g:
    print(elem)
    
# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

from abc import abstractmethod, ABC


class Laptop(ABC):

    @abstractmethod
    def Screen(self, screen: str):
        raise NotImplementedError

    @abstractmethod
    def Keyboard(self, key: str):
        raise NotImplementedError

    @abstractmethod
    def Touchpad(self, tpad: str):
        raise NotImplementedError

    @abstractmethod
    def WebCam(self, wcam: str):
        raise NotImplementedError

    @abstractmethod
    def Ports(self, ports: str):
        raise NotImplementedError

    @abstractmethod
    def Dynamics(self, dynamics: str):
        raise NotImplementedError


class HPlaptop(Laptop):

    def Screen(self, screen: str):
        pass

    def Keyboard(self, key: str):
        pass

    def Touchpad(self, tpad: str):
        pass

    def WebCam(self, wcam: str):
        pass

    def Ports(self, ports: str):
        pass

    def Dynamics(self, dynamics: str):
        pass


# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.

class Car(ABC):

    def drive(self):
        print('i\'m driving')

    def stop(self):
        print('i\'m stopping')

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError
