# coding: utf-8

from termcolor import cprint
from random import randint


class Human:
    def __init__(self):
        self.hunger = 30
        self.happen = 100

    def __str__(self):
        return 'голод: {}, счаcтье: {}'.format(self.hunger, self.happen)

    def eat(self):
        if self.house.eats <= 0:
            self.hunger = self.hunger
        else:
            if self.hunger > 150:
                pass
            else:
                self.house.eats -= 30
                self.hunger += 30


class House:

    def __init__(self):
        self.eats = 50
        self.money = 100
        self.mud = 0
        self.coat = 0
        self.mud += 5
        self.eats_cat = 20

    def __str__(self):
        return 'В доме осталось еды: {}, кошачей еды: {}, денег: {}, грязи: {}, шуб: {}'.format(self.eats,
                                                                                                self.eats_cat,
                                                                                                self.money, self.mud,
                                                                                                self.coat)


class Husband(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def go_into_the_home(self, house):
        self.house = house
        print('Въехал в дом: {}'.format(self.name))

    def __str__(self):
        res = super().__str__()
        return '{}: '.format(self.name) + res

    def act(self):
        dice = randint(1, 6)
        if self.hunger < 0:
            print('{} умер от голода...'.format(self.name))
            return
        if self.happen < 10:
            print('{} умер от депрессии...'.format(self.name))
            return
        if self.house.mud > 90:
            self.happen -= 10
        if self.house.money < 50:
            self.work()
        elif 1 <= dice <= 2:
            self.gaming()
        elif 3 <= dice < 4:
            self.work()
        elif dice == 4:
            self.stroking_cat()
        else:
            self.eat()

    def eat(self):
        super().eat()
        self.house.mud += 10
        print('{} поел.'.format(self.name))

    def stroking_cat(self):
        self.happen += 5
        print('{} погладил кота'.format(self.name))

    def work(self):
        self.hunger -= 10
        self.house.money += 150
        print('{} сходил на работу.'.format(self.name))

    def gaming(self):
        self.hunger -= 10
        self.house.mud += 20
        self.happen += 20
        print('{} играет в WoT'.format(self.name))


class Wife(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def go_into_the_home(self, house):
        self.house = house
        print('Въехал в дом: {}'.format(self.name))

    def __str__(self):
        res = super().__str__()
        return '{}: '.format(self.name) + res

    def act(self):
        dice = randint(1, 6)
        if self.hunger < 0:
            print('{} умерла от голода...'.format(self.name))
            return
        if self.happen < 10:
            print('{} умерла от депрессии...'.format(self.name))
            return
        if self.house.mud > 90:
            self.happen -= 10
        if self.hunger < 50:
            self.eat()
        elif self.house.eats < 50:
            self.shopping()
        elif self.house.mud > 50:
            self.clean_house()
        elif 1 <= dice <= 2:
            self.clean_house()
        elif 3 <= dice < 4:
            self.shopping()
        elif dice == 4:
            self.stroking_cat()
        elif dice == 5:
            self.buy_fur_coat()
        else:
            self.eat()

    def go_into_the_home(self, house):
        self.house = house
        print('Въехал в дом: {}'.format(self.name))

    def stroking_cat(self):
        self.happen += 5
        print('{} погладил кота'.format(self.name))

    def eat(self):
        super().eat()
        self.house.mud += 10
        print('{} поела'.format(self.name))

    def shopping(self):
        self.hunger -= 10
        if self.house.money < 20:
            print('Нет денег...')
        else:
            self.house.money -= 70
            self.house.eats += 50
            self.house.eats_cat += 20
            print('{} сходила в магазин за едой.'.format(self.name))

    def buy_fur_coat(self):
        if self.house.money < 400:
            self.hunger -= 10
            print('Нет денег на шубу')
        else:
            self.house.money -= 350
            self.happen += 60
            self.hunger -= 10
            self.house.coat += 1
        print('{} купила новую шубу'.format(self.name))

    def clean_house(self):
        self.hunger -= 10
        self.house.mud -= 100
        if self.house.mud < 0:
            self.house.mud = 0
        print('{} убрала дом'.format(self.name))


class Cat:

    def __init__(self, name):
        self.name = name
        self.hunger = 30

    def __str__(self):
        return 'Я кот {} сытость: {}'.format(self.name, self.hunger)

    def go_into_the_home(self, house):
        self.house = house
        print('Въехал в дом: {}'.format(self.name))

    def act(self):
        dice = randint(1, 6)
        if self.hunger < 0:
            print('{} умер от голода...'.format(self.name))
            return
        if 0 < self.hunger < 20:
            self.eat()
        elif 1 <= dice <= 2:
            self.sleep()
        elif 2 < dice <= 4:
            self.soil()
        else:
            self.eat()

    def eat(self):
        if self.house.eats_cat < 10:
            print('Нет кошачей еды!')
        else:
            self.house.eats_cat -= 10
            self.hunger += 20
            print('Кот {} поел.'.format(self.name))

    def sleep(self):
        self.hunger -= 10
        print('Кот {} спит.'.format(self.name))

    def soil(self):
        self.hunger -= 10
        self.house.mud -= 5
        print('Кот {} дерет обои.'.format(self.name))


class Child(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return super().__str__()

    def go_into_the_home(self, house):
        self.house = house
        print('Въехал в дом: {}'.format(self.name))

    def act(self):
        dice = randint(1, 6)
        if self.hunger < 10:
            self.eat()
        elif 1 <= dice <= 3:
            self.sleep()
        else:
            if self.hunger > 100:
                print('Ребенок сытый')
            else:
                self.eat()

    def eat(self):
        if self.house.eats < 10:
            print('Нет еды...')
        else:
            self.hunger += 10
            self.house.eats -= 10
            print('Ребенок {} поел.'.format(self.name))

    def sleep(self):
        self.hunger -= 10
        print('Ребенок {} поспал'.format(self.name))


home = House()
serge = Husband(name='Сережа')
serge.go_into_the_home(house=home)
masha = Wife(name='Маша')
masha.go_into_the_home(house=home)
cat = Cat(name='Мурзик')
cat.go_into_the_home(house=home)
kolya = Child(name='Коля')
kolya.go_into_the_home(house=home)

for day in range(1, 366):
    print('================== День {} =================='.format(day))
    serge.act()
    masha.act()
    cat.act()
    kolya.act()
    cprint(serge, color='blue')
    cprint(masha, color='cyan')
    cprint(home, color='red')
    cprint(cat, color='magenta')
    cprint(kolya, color='yellow')



######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)



# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
