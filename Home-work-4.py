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

class goat(milk_animals, animal):
    voice = "be be"

class sheep(animal):
    voice = "me me"
    wools = 0

    def shear(self, wool):
        self.wools += wool

class goose(bird, animal):
    voice = "ga ga ga"

class chiken(bird, animal):
    voice = "ko ko ko"

class duck(bird, animal):
    voice = "cria cria"

# print(cow.mro())
cow = cow()
cow.name = "Манька"
cow.weight = 400
cow.feed(20)
cow.milk(50)

Sheep1 = sheep()
Sheep1.name = "Барашек"
Sheep1.weight = 50
Sheep1.shear(10)
Sheep1.feed(10)

Sheep2 = sheep()
Sheep2.name = "Кудрявый"
Sheep2.weight = 45
Sheep1.shear(15)
Sheep2.feed(10)

goat1 = goat()
goat1.name = "Рога"
goat1.weight = 40
goat1.milk(10)
goat1.feed(8)

goat2 = goat()
goat2.name = "Копыта"
goat2.weight = 42
goat2.milk(10)
goat2.feed(8)

goose1 = goose()
goose1.name = "Серый"
goose1.weight = 5
goose1.collect_eggs(2)
goose1.feed(3)

goose2 = goose()
goose2.name = "Белый"
goose2.weight = 4
goose2.collect_eggs(3)
goose2.feed(3)

chiken1 = chiken()
chiken1.name = "Кукареку"
chiken1.weight = 3
chiken1.collect_eggs(5)
chiken1.feed(3)

chiken2 = chiken()
chiken2.name = "Ко-Ко"
chiken2.weight = 2
chiken2.collect_eggs(4)
chiken2.feed(3)

duck = duck()
duck.name = "Кряква"
duck.weight = 2
duck.collect_eggs(3)
duck.feed(3)


print(Sheep2.weight)