# Занятие № 4 задение 1
# Написать класс человек в котором можно хранить имя и фамилию человека, возраст, менять и получать их. Возраст должен быть между 0 и 120 годами
#

class People:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age;

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 120 < age or age < 0:
            raise Exception("Возраст должен быть в диапазоне от 0 до 120 лет")
        else:
            self.__age = age

    def print(self):
        print("{fist_name: %s, last_name: %s, age: %s}" %(self.first_name, self.last_name, self.age))


man = People('Dmitry', 'Melchenkov', 33)
man.print()
man.age += 1
man.print()
man.age = 199
man.print()
