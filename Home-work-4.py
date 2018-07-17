class animal:
    name = ""
    weight = 0
    food = 0
    weight_all = 0

    def feed(self, value):
        self.food += value


class milk_animals:
    milk_liter = 0
    def milk(self, value):
        self.milk_liter += value

class bird:
    eggs = 0

    def collect_eggs(self, egg):
        self.eggs += egg

class cow(milk_animals, animal):
    voice = "mu mu"

    def __init__(self, name, weight):
       self.name = name
       self.weight = weight
       all_weight[name] = weight

class goat(milk_animals, animal):
    voice = "be be"
    def __init__(self, name, weight):
       self.name = name
       self.weight = weight
       all_weight[name] = weight


class sheep(animal):
    voice = "me me"
    wools = 0

    def __init__(self, name, weight):
       self.name = name
       self.weight = weight
       all_weight[name] = weight


    def shear(self, wool):
        self.wools += wool

class goose(bird, animal):
    voice = "ga ga ga"
    def __init__(self, name, weight):
       self.name = name
       self.weight = weight
       all_weight[name] = weight


class chiken(bird, animal):
    voice = "ko ko ko"
    def __init__(self, name, weight):
       self.name = name
       self.weight = weight
       all_weight[name] = weight


class duck(bird, animal):
    voice = "cria cria"
    def __init__(self, name, weight):
       self.name = name
       self.weight = weight
       all_weight[name] = weight


# print(cow.mro())

all_weight = {}

cow = cow("Манька", 400)
cow.feed(20)
cow.milk(50)

Sheep1 = sheep("Барашек", 50)
Sheep1.shear(10)
Sheep1.feed(10)

Sheep2 = sheep("Кудрявый", 45)
Sheep1.shear(15)
Sheep2.feed(10)

goat1 = goat("Рога", 40)
goat1.milk(10)
goat1.feed(8)

goat2 = goat("Копыта", 42)
goat2.milk(10)
goat2.feed(8)

goose1 = goose("Серый", 5)
goose1.collect_eggs(2)
goose1.feed(3)

goose2 = goose("Белый", 4)
goose2.collect_eggs(3)
goose2.feed(3)

chiken1 = chiken("Кукареку", 3)
chiken1.collect_eggs(5)
chiken1.feed(3)

chiken2 = chiken("Ко-Ко", 2)
chiken2.collect_eggs(4)
chiken2.feed(3)

duck = duck("Кряква", 2)
duck.collect_eggs(3)
duck.feed(3)

max_weight = 0
max_animal_name = ""
for animal_names, animal_weight in all_weight.items():
    if animal_weight > max_weight:
        max_weight = animal_weight
        max_animal_name = animal_names

print("{} {}".format(max_animal_name, max_weight))