def add(*arasass):
    return sum(arasass)

def caculate(**kwargs):
    print(kwargs)

caculate(add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        print(self.make)
        print(self.model)
        print(kw)
my_car = Car(make="hello")