# Занятие № 4 задение 2
# Написать класс у которого будет отдел и зарплата, которые так же задаются.
# Сделать поля удачных и неудачных поступков сотрудника которые можно через вызовы методов наращивать.
# Реализовать метод считающее итоговую зарплату = зп + 2*(удачные действия) - 3* (неудачные действия)
# У менеджера зарплата считается как зп + 4*(удачные действия) - 5* (неудачные действия)

class Emploee:
    def __init__(self, firt_name, last_name, division, manager, salary):
        self.first_name = firt_name
        self.last_name = last_name
        self.division = division
        self.salary = salary;
        self.manager = manager;
        self.__good_act = 0
        self.__bad_act = 0
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise Exception("Заработная плата - положитльное число")
        else:
            self.__salary = salary
    @property
    def itog_salary(self):
        if self.manager == False:
            self.__itog_salary = self.__salary + 2 * self.__good_act - 3 * self.__bad_act
        else:
            self.__itog_salary = self.__salary + 4 * self.__good_act - 5 * self.__bad_act
        return(self.__itog_salary)
    @property
    def good_act(self):
        return self.__good_act
    @property
    def bad_act(self):
        return self.__bad_act
    def inc_good_act(self, inc_value):
        if inc_value < 0:
            raise Exception("inc_value при вызове inc_good_act должно быть > 0")
        else:
            self.__good_act += inc_value
    def dec_good_act(self, dec_value):
        if dec_value < 0:
            raise Exception("dec_value при вызове dec_good_act должно быть > 0")
        else:
            self.__good_act -= dec_value
    def inc_bad_act(self, inc_value):
        if inc_value < 0:
            raise Exception("inc_value при вызове inc_bad_act должно быть > 0")
        else:
            self.__bad_act += inc_value
    def dec_bad_act(self, dec_value):
        if dec_value < 0:
            raise Exception("dec_value при вызове dec_bad_act должно быть > 0")
        else:
            self.__bad_act -= dec_value
    def print(self):
        print("{fist_name: %s, last_name: %s, division: %s, manager: %s, salary: %s, good_act %s, bad_act: %s, itog_salary: %s}" % (
        self.first_name, self.last_name, self.division, str(self.manager), str(self.salary), str(self.__good_act),
        str(self.__bad_act), str(self.itog_salary)))

# Рабочий
Worker = Emploee('John', 'Smith', 'DOMCLICK', False, 10000.00)
Worker.inc_good_act(5)
Worker.dec_good_act(1)
Worker.inc_bad_act(3)
Worker.dec_bad_act(1)
Worker.print()

# Менеджер
Manager = Emploee('Bill', 'Lewis', 'DOMCLICK', True, 20000.00)
Manager.inc_good_act(6)
Manager.inc_bad_act(3)
Manager.print()
