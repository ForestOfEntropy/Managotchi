class Managotchi:
    """"""

    def __init__(self, name):
        self.name = str(name)
        self.hp = 100
        self.max_hp = 100
        self.saturation = 50
        self.happiness = 65
        self.hygiene = 100
        self.satisfaction = 100
        self.age = 0
        self.mana = 0
        self.max_mana = 100

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if len(new_name) < 15:
            self.name = new_name

    def get_hp(self):
        return self.hp

    def heal(self, heal=10):
        self.hp = min(self.hp + heal, self.max_hp)
        return True

    def hurt(self, damage=10):
        self.hp -= damage
        if self.hp <= 0:
            raise Exception(f'Your managotchi {self.name} succumbed to its injuries at the poor age of {self.age}, please do NOT get a real pet.')
        return True

    def get_saturation(self):
        return self.saturation

    def feed(self, nutrition=10):
        self.saturation = min(self.saturation + nutrition, 100)
        if self.saturation > 99:
            print("I'm full")
        return True

    def starve(self, nutrition=10):
        self.saturation -= nutrition
        if self.saturation <= 0:
            raise Exception(f'Your managotchi {self.name} starved at the poor age of {self.age}, please do NOT get a real pet.')
        return True


    def get_happiness(self):
        return self.happiness

    def emotion_happy(self, happiness=10):
        self.happiness = min(self.happiness + happiness, 100)
        return True

    def emotion_sad(self, sadness=10):
        self.happiness -= sadness
        if self.happiness <= 0:
            raise Exception(f'Your managotchi {self.name} was so sad it died at the age of {self.age}, what did you do?')
        return True

    def get_hygiene(self):
        return self.hygiene

    def clean(self, intensity=10):
        self.hygiene = min(self.hygiene + intensity, 100)
        return True

    def verdrecken(self, intensity=10):
        self.hygiene = max(self.hygiene - intensity, 0)
        if self.hygiene == 0:
            self.hurt(round(intensity/2))
        return True

    def get_entertained(self):
        return self.satisfaction

    def excite(self, entertainment=10):
        self.satisfaction = min(self.satisfaction + entertainment, 100)
        if self.satisfaction == 100:
            print("Wuhhuuu this is so EXCITING!")
        return True

    def bore(self, boredom=10):
        self.satisfaction -= boredom
        if self.satisfaction <= 0:
            raise Exception(f'Your managotchi {self.name} ran away, because you are too boring.')
        return True

    def get_age(self):
        return self.age

    def pass_time(self, time=1):
        if not self.verdrecken(time):
            return False
        self.age += time
        if not self.bore(time):
            return False
        if not self.starve(time):
            return False
        self.heal(time)
        return True

    def sense_mana(self):
        return self.mana

    def gain_mana(self, time=1):
        self.mana += time
        if self.mana > self.max_mana:
            self.hurt(1)
            print("Arg too much mana")
            self.mana = self.max_mana
        return True

    def use_mana(self, mana):
        self.mana -= mana
        if self.mana >= mana:
            self.mana -= mana
            return True
        else:
            self.hp -= ((mana-self.mana)//2)
            print('kzzssss manaburn')
            return False
