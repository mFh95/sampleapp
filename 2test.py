def sum(x, y, z=0):
    return x + y + z


print(sum(2, 3))

y = 'hello' 'world'


class Dog:
    animal_type = "Canis"

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age
