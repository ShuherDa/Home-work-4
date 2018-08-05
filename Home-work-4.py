class Animal:
    name = ""
    weight = 0
    food = 0
    weight_all = 0

    def __init__(self, name, weight):
       self.name = name
       self.weight = weight
       all_weight[name] = weight

    def feed(self, value):
        self.food += value

class MilkAnimals:
    milk_liter = 0
    def milk(self, value):
        self.milk_liter += value

class Bird(Animal):
    eggs = 0

    def collect_eggs(self, egg):
        self.eggs += egg

class Cow(MilkAnimals, Animal):
    voice = "mu mu"

class Goat(MilkAnimals, Animal):
    voice = "be be"

class Sheep(Animal):
    voice = "me me"
    wools = 0

    def shear(self, wool):
        self.wools += wool

class Goose(Bird):
    voice = "ga ga ga"

class Chiken(Bird):
    voice = "ko ko ko"

class Duck(Bird):
    voice = "cria cria"



# print(cow.mro())

all_weight = {}

cow = Cow("Манька", 400)
cow.feed(20)
cow.milk(50)

Sheep1 = Sheep("Барашек", 50)
Sheep1.shear(10)
Sheep1.feed(10)

Sheep2 = Sheep("Кудрявый", 45)
Sheep1.shear(15)
Sheep2.feed(10)

goat1 = Goat("Рога", 40)
goat1.milk(10)
goat1.feed(8)

goat2 = Goat("Копыта", 42)
goat2.milk(10)
goat2.feed(8)

goose1 = Goose("Серый", 5)
goose1.collect_eggs(2)
goose1.feed(3)

goose2 = Goose("Белый", 4)
goose2.collect_eggs(3)
goose2.feed(3)

chiken1 = Chiken("Кукареку", 3)
chiken1.collect_eggs(5)
chiken1.feed(3)

chiken2 = Chiken("Ко-Ко", 2)
chiken2.collect_eggs(4)
chiken2.feed(3)

duck = Duck("Кряква", 2)
duck.collect_eggs(3)
duck.feed(3)

max_weight = 0
max_animal_name = ""
for animal_names, animal_weight in all_weight.items():
    if animal_weight > max_weight:
        max_weight = animal_weight
        max_animal_name = animal_names

print("{} {}".format(max_animal_name, max_weight))