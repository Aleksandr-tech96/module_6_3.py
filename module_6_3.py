import random

# Родительский класс "Животное"
class Animal:
    live = True
    sound = None # звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0 # (степень опасности существа)

    def __init__(self, speed):
        self.speed = speed  # (скорость передвижения существа)
        self._cords = [0, 0, 0] # (координаты в пространстве)

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    def get_cords(self):
        x, y, z = self._cords
        print(f"X: {x}, Y: {y}, Z: {z}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz_adjusted = abs(dz) * self.speed / 2
        new_z = int(self._cords[2] - dz_adjusted)
        if new_z < 0:
            self._cords[2] = 0
        else:
            self._cords[2] = new_z

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    _DEGREE_OF_DANGER = 5
    sound = "Click-click-click"

# Тестовый код
if __name__ == "__main__":
    db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()