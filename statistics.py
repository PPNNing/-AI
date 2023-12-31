import math
import numpy


class Hero:
    def __init__(self, name, cost, attributes, skill_type, rate):
        self.name = name
        self.cost = cost
        self.attributes = attributes
        self.skill_type = skill_type
        self.synergies = []
        self.weapon = []
        self.rate = rate

    def add_rate(self, rate):
        self.rate = rate

    def add_synergy(self, synergy):
        if synergy not in self.synergies:
            self.synergies.append(synergy)
            # synergy.add_hero(self)

    def get_attributes(self, stage):
        if 1 <= stage <= 3:
            return {attr: values[stage - 1] for attr, values in self.attributes.items()}
        else:
            raise ValueError("Stage must be 1, 2, or 3")

    def add_weapon(self, weapon):
        if weapon not in self.weapon:
            self.weapon.append(weapon)

    def get_cost(self):
        return self.cost

    def __repr__(self):
        return f"{self.name} (Cost: {self.cost}, Skill Type: {self.skill_type})"


class Synergy:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.stages = []
        self.rate = []

    def add_hero(self, hero):
        if hero not in self.heroes:
            self.heroes.append(hero)

    def add_stage(self, stage):
        self.stages = stage

    def add_rate(self, rate):
        self.rate = rate

    def check_stage(self):
        active_stages = []
        for stage in self.stages:
            if len(self.heroes) >= stage["required_heroes"]:
                active_stages.append(stage)
        return active_stages

    def __repr__(self):
        return self.name


class SynergyManager:
    def __init__(self):
        self.synergies = []

    def add_synergy(self, synergy):
        self.synergies.append(synergy)

    def get_synergy(self, name):
        for synergy in self.synergies:
            if synergy.name == name:
                return synergy
        return None

    def __repr__(self):
        return ", ".join([synergy.name for synergy in self.synergies])


class Low_Weapon:
    def __init__(self, name, number):
        self.name = name
        self.father = []
        self.number = number

    def add_Father(self, father):
        if father not in self.father:
            self.father.append(father)
            father.add_child(self)


class High_Weapon:
    def __init__(self, name, number):
        self.name = name
        self.child = []
        self.number = number

    def add_child(self, child):
        if child not in self.child:
            self.child.append(child)


class WeaponManager:
    def __init__(self):
        self.weapon = []

    def add_weapon(self, weapon):
        self.weapon.append(weapon)

    def get_weapon(self, name):
        for weapon in self.weapon:
            if weapon.name == name:
                return weapon
        return None

    def __repr__(self):
        return ", ".join([weapon.name for weapon in self.weapon])


class array:
    def __init__(self, rate):
        self.core_hero = []
        self.flex_hero = []
        self.rate = rate
        self.hero_weapon_recommendations = {}
        self.weapon_recommendations = []

    def add_core_hero(self, heroes):
        for hero in heroes:
            if hero not in self.core_hero:
                self.core_hero.append(hero)

    def add_flex_hero(self, heroes):
        for hero in heroes:
            if hero not in self.flex_hero:
                self.flex_hero.append(hero)

    def recommend_weapon_for_hero(self, hero, weapons):
        self.hero_weapon_recommendations[hero] = weapons

    def get_weapon_recommendation(self, hero):
        return self.hero_weapon_recommendations.get(hero, [])

    def weapon_recommend(self, weapons):
        self.weapon_recommendations = weapons


synergy_manager = SynergyManager()

weapon_manager = WeaponManager()

l_weapon1 = Low_Weapon("Low_weapon1", 1)
l_weapon2 = Low_Weapon("Low_weapon2", 2)
l_weapon3 = Low_Weapon("Low_weapon3", 3)
l_weapon4 = Low_Weapon("Low_weapon4", 4)
l_weapon5 = Low_Weapon("Low_weapon5", 5)
l_weapon6 = Low_Weapon("Low_weapon6", 6)
l_weapon7 = Low_Weapon("Low_weapon7", 7)
l_weapon8 = Low_Weapon("Low_weapon8", 8)
l_weapon9 = Low_Weapon("Low_weapon9", 9)
h_weapon1 = High_Weapon("High_weapon1", 1)
h_weapon2 = High_Weapon("High_weapon2", 2)
h_weapon3 = High_Weapon("High_weapon3", 3)
h_weapon4 = High_Weapon("High_weapon4", 4)
h_weapon5 = High_Weapon("High_weapon5", 5)
h_weapon6 = High_Weapon("High_weapon6", 6)
h_weapon7 = High_Weapon("High_weapon7", 7)
h_weapon8 = High_Weapon("High_weapon8", 8)
h_weapon9 = High_Weapon("High_weapon9", 9)
h_weapon10 = High_Weapon("High_weapon10", 10)
h_weapon11 = High_Weapon("High_weapon11", 11)
h_weapon12 = High_Weapon("High_weapon12", 12)
h_weapon13 = High_Weapon("High_weapon13", 13)
h_weapon14 = High_Weapon("High_weapon14", 14)
h_weapon15 = High_Weapon("High_weapon15", 15)
h_weapon16 = High_Weapon("High_weapon16", 16)
h_weapon17 = High_Weapon("High_weapon17", 17)
h_weapon18 = High_Weapon("High_weapon18", 18)
h_weapon19 = High_Weapon("High_weapon19", 19)
h_weapon20 = High_Weapon("High_weapon20", 20)
h_weapon21 = High_Weapon("High_weapon21", 21)
h_weapon22 = High_Weapon("High_weapon22", 22)
h_weapon23 = High_Weapon("High_weapon23", 23)
h_weapon24 = High_Weapon("High_weapon24", 24)
h_weapon25 = High_Weapon("High_weapon25", 25)
h_weapon26 = High_Weapon("High_weapon26", 26)
h_weapon27 = High_Weapon("High_weapon27", 27)
h_weapon28 = High_Weapon("High_weapon28", 28)
h_weapon29 = High_Weapon("High_weapon29", 29)
h_weapon30 = High_Weapon("High_weapon30", 30)
h_weapon31 = High_Weapon("High_weapon31", 31)
h_weapon32 = High_Weapon("High_weapon32", 32)
h_weapon33 = High_Weapon("High_weapon33", 33)
h_weapon34 = High_Weapon("High_weapon34", 34)
h_weapon35 = High_Weapon("High_weapon35", 35)
h_weapon36 = High_Weapon("High_weapon36", 36)
h_weapon37 = High_Weapon("High_weapon37", 37)
h_weapon38 = High_Weapon("High_weapon38", 38)
h_weapon39 = High_Weapon("High_weapon39", 39)
h_weapon40 = High_Weapon("High_weapon40", 40)
h_weapon41 = High_Weapon("High_weapon41", 41)
h_weapon42 = High_Weapon("High_weapon42", 42)
h_weapon43 = High_Weapon("High_weapon43", 43)
h_weapon44 = High_Weapon("High_weapon44", 44)
h_weapon45 = High_Weapon("High_weapon45", 45)
l_weapon1.add_Father(h_weapon1)
l_weapon1.add_Father(h_weapon2)
l_weapon1.add_Father(h_weapon3)
l_weapon1.add_Father(h_weapon4)
l_weapon1.add_Father(h_weapon5)
l_weapon1.add_Father(h_weapon6)
l_weapon1.add_Father(h_weapon30)
l_weapon1.add_Father(h_weapon36)
l_weapon1.add_Father(h_weapon45)
l_weapon2.add_Father(h_weapon2)
l_weapon2.add_Father(h_weapon7)
l_weapon2.add_Father(h_weapon8)
l_weapon2.add_Father(h_weapon9)
l_weapon2.add_Father(h_weapon10)
l_weapon2.add_Father(h_weapon11)
l_weapon2.add_Father(h_weapon12)
l_weapon2.add_Father(h_weapon34)
l_weapon2.add_Father(h_weapon44)
l_weapon3.add_Father(h_weapon3)
l_weapon3.add_Father(h_weapon7)
l_weapon3.add_Father(h_weapon13)
l_weapon3.add_Father(h_weapon14)
l_weapon3.add_Father(h_weapon15)
l_weapon3.add_Father(h_weapon16)
l_weapon3.add_Father(h_weapon17)
l_weapon3.add_Father(h_weapon31)
l_weapon3.add_Father(h_weapon39)
l_weapon4.add_Father(h_weapon4)
l_weapon4.add_Father(h_weapon8)
l_weapon4.add_Father(h_weapon14)
l_weapon4.add_Father(h_weapon18)
l_weapon4.add_Father(h_weapon19)
l_weapon4.add_Father(h_weapon20)
l_weapon4.add_Father(h_weapon32)
l_weapon4.add_Father(h_weapon42)
l_weapon5.add_Father(h_weapon9)
l_weapon5.add_Father(h_weapon21)
l_weapon5.add_Father(h_weapon22)
l_weapon5.add_Father(h_weapon23)
l_weapon5.add_Father(h_weapon31)
l_weapon5.add_Father(h_weapon35)
l_weapon5.add_Father(h_weapon36)
l_weapon5.add_Father(h_weapon39)
l_weapon6.add_Father(h_weapon5)
l_weapon6.add_Father(h_weapon10)
l_weapon6.add_Father(h_weapon15)
l_weapon6.add_Father(h_weapon22)
l_weapon6.add_Father(h_weapon24)
l_weapon6.add_Father(h_weapon25)
l_weapon6.add_Father(h_weapon32)
l_weapon6.add_Father(h_weapon33)
l_weapon6.add_Father(h_weapon38)
l_weapon7.add_Father(h_weapon11)
l_weapon7.add_Father(h_weapon16)
l_weapon7.add_Father(h_weapon19)
l_weapon7.add_Father(h_weapon23)
l_weapon7.add_Father(h_weapon26)
l_weapon7.add_Father(h_weapon29)
l_weapon7.add_Father(h_weapon30)
l_weapon7.add_Father(h_weapon33)
l_weapon7.add_Father(h_weapon43)
l_weapon8.add_Father(h_weapon27)
l_weapon8.add_Father(h_weapon38)
l_weapon8.add_Father(h_weapon39)
l_weapon8.add_Father(h_weapon40)
l_weapon8.add_Father(h_weapon41)
l_weapon8.add_Father(h_weapon42)
l_weapon8.add_Father(h_weapon43)
l_weapon8.add_Father(h_weapon44)
l_weapon8.add_Father(h_weapon45)
l_weapon9.add_Father(h_weapon6)
l_weapon9.add_Father(h_weapon12)
l_weapon9.add_Father(h_weapon17)
l_weapon9.add_Father(h_weapon20)
l_weapon9.add_Father(h_weapon25)
l_weapon9.add_Father(h_weapon28)
l_weapon9.add_Father(h_weapon29)
l_weapon9.add_Father(h_weapon35)
l_weapon9.add_Father(h_weapon41)

synergy1 = Synergy("Synergy1")
synergy1.add_stage([2, 4, 6])
synergy1.add_rate([5.21, 5.22, 4.95])
synergy_manager.add_synergy(synergy1)
synergy2 = Synergy("Synergy2")
synergy2.add_stage([1])
synergy2.add_rate([4.15])
synergy_manager.add_synergy(synergy2)
synergy3 = Synergy("Synergy3")
synergy3.add_stage([3, 5, 7])
synergy3.add_rate([4.64, 4.13, 2.88])
synergy_manager.add_synergy(synergy3)
synergy4 = Synergy("Synergy4")
synergy4.add_stage([1])
synergy4.add_rate([3.89])
synergy_manager.add_synergy(synergy4)
synergy5 = Synergy("Synergy5")
synergy5.add_stage([2, 3, 4, 5])
synergy5.add_rate([4.70, 5.52, 5.29, 4.60])
synergy_manager.add_synergy(synergy5)
synergy6 = Synergy("Synergy6")
synergy6.add_stage([2, 4, 6])
synergy6.add_rate([4.18, 4.02, 3.77])
synergy_manager.add_synergy(synergy6)
synergy7 = Synergy("Synergy7")
synergy7.add_stage([3, 4, 5, 6])
synergy7.add_rate([4.86, 5.05, 4.50, 4.35])
synergy_manager.add_synergy(synergy7)
synergy8 = Synergy("Synergy8")
synergy8.add_stage([1, 2, 3, 4])
synergy8.add_rate([4.02, 3.75, 3.44, 2.74])
synergy_manager.add_synergy(synergy8)
synergy9 = Synergy("Synergy9")
synergy9.add_stage([2, 3, 4])
synergy9.add_rate([4.42, 4.04, 3.17])
synergy_manager.add_synergy(synergy9)
synergy10 = Synergy("Synergy10")
synergy10.add_stage([3, 5, 7, 10])
synergy10.add_rate([4.20, 4.39, 4.41, 1.18])
synergy_manager.add_synergy(synergy10)
synergy11 = Synergy("Synergy11")
synergy11.add_stage([3, 5, 7, 10])
synergy11.add_rate([4.77, 4.66, 4.08, 1.20])
synergy_manager.add_synergy(synergy11)
synergy12 = Synergy("Synergy12")
synergy12.add_stage([3, 5, 7, 10])
synergy12.add_rate([5.13, 5.96, 5.85, 3.14])
synergy_manager.add_synergy(synergy12)
synergy13 = Synergy("Synergy13")
synergy13.add_stage([2, 4, 6])
synergy13.add_rate([4.92, 4.87, 4.02])
synergy_manager.add_synergy(synergy13)
synergy14 = Synergy("Synergy14")
synergy14.add_stage([1])
synergy14.add_rate([3.77])
synergy_manager.add_synergy(synergy14)
synergy15 = Synergy("Synergy15")
synergy15.add_stage([2, 4, 6, 9])
synergy15.add_rate([4.18, 4.60, 4.32, 1.74])
synergy_manager.add_synergy(synergy15)
synergy16 = Synergy("Synergy16")
synergy16.add_stage([2, 4, 6])
synergy16.add_rate([4.46, 4.19, 4.08])
synergy_manager.add_synergy(synergy16)
synergy17 = Synergy("Synergy17")
synergy17.add_stage([2, 4, 6])
synergy17.add_rate([4.48, 5, 44, 2.73])
synergy_manager.add_synergy(synergy17)
synergy18 = Synergy("Synergy18")
synergy18.add_stage([1])
synergy18.add_rate([4.52])
synergy_manager.add_synergy(synergy18)
synergy19 = Synergy("Synergy19")
synergy19.add_stage([3, 5, 7])
synergy19.add_rate([4.91, 5.43, 4.38])
synergy_manager.add_synergy(synergy19)
synergy20 = Synergy("Synergy20")
synergy20.add_stage([2, 4, 6])
synergy20.add_rate([4.06, 4.36, 4.82])
synergy_manager.add_synergy(synergy20)
synergy21 = Synergy("Synergy21")
synergy21.add_stage([3, 5, 7, 10])
synergy21.add_rate([4, 17, 4, 11, 3.86, 2.80])
synergy_manager.add_synergy(synergy21)
synergy22 = Synergy("Synergy22")
synergy22.add_stage([2, 4, 6])
synergy22.add_rate([3.95, 4.13, 3.71])
synergy_manager.add_synergy(synergy22)
synergy23 = Synergy("Synergy23")
synergy23.add_stage([2, 4, 6])
synergy23.add_rate([4.32, 4.09, 3.61])
synergy_manager.add_synergy(synergy23)
synergy24 = Synergy("Synergy24")
synergy24.add_stage([2, 4, 6])
synergy24.add_rate([4.35, 4, 80, 4, 17])
synergy_manager.add_synergy(synergy24)
synergy25 = Synergy("Synergy25")
synergy25.add_stage([3, 4, 5])
synergy25.add_rate([4.354, 4, 28, 3.92])
synergy_manager.add_synergy(synergy25)
synergy26 = Synergy("Synergy26")
synergy26.add_stage([2, 4, 6, 8])
synergy26.add_rate([4.42, 5.01, 5.10, 3.03])
synergy_manager.add_synergy(synergy26)
synergy27 = Synergy("Synergy27")
synergy27.add_stage([2, 4, 6])
synergy27.add_rate([4.14, 4.19, 4.75])
synergy_manager.add_synergy(synergy27)
synergy28 = Synergy("Synergy28")
synergy28.add_stage([2, 4, 6])
synergy28.add_rate([4.27, 4.03, 4.16])
synergy_manager.add_synergy(synergy28)
synergy29 = Synergy("Synergy29")
synergy29.add_stage([1])
synergy29.add_rate([4.72])
hero_attributes_1 = {
    "health": [500, 900, 1620],
    "defense": [15, 15, 15],
    "sp_defense": [15, 15, 15],
    "attack": [30, 45, 68],
    "attack_speed": [0.6, 0.6, 0.6],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [0, 0, 0],
    "power": [0, 0, 0]
}
hero1 = Hero(name="Hero1", cost=1, attributes=hero_attributes_1, skill_type=1, rate=4.15)
hero1.add_synergy(6)
hero1.add_synergy(21)

hero_attributes_2 = {
    "health": [700, 1260, 2268],
    "defense": [30, 30, 30],
    "sp_defense": [30, 30, 30],
    "attack": [65, 98, 146],
    "attack_speed": [0.5, 0.5, 0.5],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [40, 40, 40],
    "power": [100, 100, 100]
}
hero2 = Hero(name="Hero2", cost=1, attributes=hero_attributes_2, skill_type=1, rate=5.16)
hero2.add_synergy(11)
hero2.add_synergy(27)

hero_attributes_3 = {
    "health": [700, 1260, 2268],
    "defense": [25, 25, 25],
    "sp_dedense": [25, 25, 25],
    "attack": [50, 75, 113],
    "attack_speed": [0.65, 0.65, 0.65],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [40, 40, 40],
    "power": [80, 80, 80]
}
hero3 = Hero(name="Hero3", cost=1, attributes=hero_attributes_3, skill_type=2, rate=4.45)
hero3.add_synergy(10)
hero3.add_synergy(17)

hero_attributes_4 = {
    "health": [650, 1170, 2106],
    "defense": [45, 45, 45],
    "sp_defense": [45, 45, 45],
    "attack": [50, 75, 113],
    "attack_speed": [0.6, 0.6, 0.6],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [50, 50, 50],
    "power": [110, 110, 110]
}
hero4 = Hero(name="Hero4", cost=1, attributes=hero_attributes_4, skill_type=1, rate=4.43)
hero4.add_synergy(15)
hero4.add_synergy(25)
hero4.add_synergy(28)

hero_attributes_5 = {
    "health": [500, 900, 1620],
    "defense": [15, 15, 15],
    "sp_defense": [15, 15, 15],
    "attack": [35, 53, 79],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [20, 20, 20],
    "power": [70, 70, 70]
}
hero5 = Hero(name="Hero5", cost=1, attributes=hero_attributes_5, skill_type=3, rate=5.30)
hero5.add_synergy(1)
hero5.add_synergy(23)

hero_attributes_6 = {
    "health": [500, 900, 1620],
    "defense": [20, 20, 20],
    "sp_defense": [20, 20, 20],
    "attack": [40, 60, 90],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [0, 0, 0],
    "power": [30, 30, 30]
}
hero6 = Hero(name="Hero6", cost=1, attributes=hero_attributes_6, skill_type=1, rate=4.75)
hero6.add_synergy(7)
hero6.add_synergy(28)

hero_attributes_7 = {
    "health": [700, 1260, 2268],
    "defense": [40, 40, 40],
    "sp_defense": [40, 40, 40],
    "attack": [55, 83, 124],
    "attack_speed": [0.55, 0.55, 0.55],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [30, 30, 30],
    "power": [90, 90, 90]
}
hero7 = Hero(name="Hero7", cost=1, attributes=hero_attributes_7, skill_type=2, rate=5.21)
hero7.add_synergy(15)
hero7.add_synergy(19)

hero_attributes_8 = {
    "health": [500, 900, 1620],
    "defense": [15, 15, 15],
    "sp_defense": [15, 15, 15],
    "attack": [40, 60, 90],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [0, 0, 0],
    "power": [50, 50, 50]
}
hero8 = Hero(name="Hero8", cost=1, attributes=hero_attributes_8, skill_type=1, rate=4.74)
hero8.add_synergy(13)
hero8.add_synergy(24)

hero_attributes_9 = {
    "health": [504, 907, 1633],
    "defense": [14, 14, 14],
    "sp_defense": [14, 14, 14],
    "attack": [54, 81, 122],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [44, 44, 44],
    "power": [114, 114, 114]
}
hero9 = Hero(name="Hero9", cost=1, attributes=hero_attributes_9, skill_type=1, rate=4.32)
hero9.add_synergy(3)
hero9.add_synergy(27)

hero_attributes_10 = {
    "health": [500, 900, 1620],
    "defense": [15, 15, 15],
    "sp_defense": [15, 15, 15],
    "attack": [45, 68, 101],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [0, 0, 0],
    "power": [30, 30, 30]
}
hero10 = Hero(name="Hero10", cost=1, attributes=hero_attributes_10, skill_type=1, rate=4.77)
hero10.add_synergy(13)
hero10.add_synergy(20)

hero_attributes_11 = {
    "health": [700, 1260, 2268],
    "defense": [40, 40, 40],
    "sp_defense": [40, 40, 40],
    "attack": [55, 83, 124],
    "attack_speed": [0.65, 0.65, 0.65],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [30, 30, 30],
    "power": [80, 80, 80]
}
hero11 = Hero(name="Hero11", cost=1, attributes=hero_attributes_11, skill_type=3, rate=4.62)
hero11.add_synergy(7)
hero11.add_synergy(22)

hero_attributes_12 = {
    "health": [700, 1260, 2268],
    "defense": [40, 40, 40],
    "sp_defense": [40, 40, 40],
    "attack": [60, 90, 135],
    "attack_speed": [0.55, 0.55, 0.55],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [40, 40, 40],
    "power": [80, 80, 80]
}
hero12 = Hero(name="Hero12", cost=1, attributes=hero_attributes_12, skill_type=1, rate=4.37)
hero12.add_synergy(10)
hero12.add_synergy(25)
hero12.add_synergy(26)

hero_attributes_13 = {
    "health": [500, 900, 1620],
    "defense": [20, 20, 20],
    "sp_defense": [20, 20, 20],
    "attack": [40, 60, 90],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [20, 20, 20],
    "power": [70, 70, 70]
}
hero13 = Hero(name="Hero13", cost=1, attributes=hero_attributes_13, skill_type=1, rate=6.07)
hero13.add_synergy(12)
hero13.add_synergy(26)

hero_attributes_14 = {
    "health": [800, 1440, 2592],
    "defense": [45, 45, 45],
    "sp_defense": [45, 45, 45],
    "attack": [70, 205, 158],
    "attack_speed": [0.5, 0.5, 0.5],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [60, 60, 60],
    "power": [110, 110, 110]
}
hero14 = Hero(name="Hero14", cost=2, attributes=hero_attributes_14, skill_type=2, rate=4.89)
hero14.add_synergy(11)
hero14.add_synergy(19)

hero_attributes_15 = {
    "health": [700, 1260, 2268],
    "defense": [25, 25, 25],
    "sp_defense": [25, 25, 25],
    "attack": [55, 83, 124],
    "attack_speed": [0.65, 0.65, 0.65],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [30, 30, 30],
    "power": [90, 90, 90]
}
hero15 = Hero(name="Hero15", cost=2, attributes=hero_attributes_15, skill_type=3, rate=5.35)
hero15.add_synergy(1)
hero15.add_synergy(26)

hero_attributes_16 = {
    "health": [800, 1440, 2592],
    "defense": [50, 50, 50],
    "sp_defense": [50, 50, 50],
    "attack": [40, 60, 90],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [40, 40, 40],
    "power": [90, 90, 90]
}
hero16 = Hero(name="Hero16", cost=2, attributes=hero_attributes_16, skill_type=1, rate=5.06)
hero16.add_synergy(5)
hero16.add_synergy(20)

hero_attributes_17 = {
    "health": [600, 1080, 1944],
    "defense": [20, 20, 20],
    "sp_defense": [20, 20, 20],
    "attack": [55, 83, 124],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [20, 20, 20],
    "power": [70, 70, 70]
}
hero17 = Hero(name="Hero17", cost=2, attributes=hero_attributes_17, skill_type=1, rate=4.67)
hero17.add_synergy(13)
hero17.add_synergy(16)

hero_attributes_18 = {
    "health": [800, 1440, 2592],
    "defense": [45, 45, 45],
    "sp_defense": [45, 45, 45],
    "attack": [50, 75, 113],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [50, 50, 50],
    "power": [100, 100, 100]
}
hero18 = Hero(name="Hero18", cost=2, attributes=hero_attributes_18, skill_type=1, rate=4.47)
hero18.add_synergy(3)
hero18.add_synergy(17)

hero_attributes_19 = {
    "health": [800, 1440, 2592],
    "defense": [50, 50, 50],
    "sp_defense": [50, 50, 50],
    "attack": [45, 68, 101],
    "attack_speed": [0.65, 0.65, 0.65],
    "ct": [0.25, 0.25, 0.25],
    "distance": [2, 2, 2],
    "pre_power": [60, 60, 60],
    "power": [135, 135, 135]
}
hero19 = Hero(name="Hero19", cost=2, attributes=hero_attributes_19, skill_type=2, rate=4.84)
hero19.add_synergy(13)
hero19.add_synergy(28)

hero_attributes_20 = {
    "health": [550, 990, 1782],
    "defense": [20, 20, 20],
    "sp_defense": [20, 20, 20],
    "attack": [40, 60, 90],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [20, 20, 20],
    "power": [60, 60, 60]
}
hero20 = Hero(name="Hero20", cost=2, attributes=hero_attributes_20, skill_type=3, rate=4.60)
hero20.add_synergy(7)
hero20.add_synergy(21)
hero20.add_synergy(27)

hero_attributes_21 = {
    "health": [600, 1080, 1944],
    "defense": [20, 20, 20],
    "sp_defense": [20, 20, 20],
    "attack": [50, 75, 113],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [10, 10, 10],
    "power": [70, 70, 70]
}
hero21 = Hero(name="Hero21", cost=2, attributes=hero_attributes_21, skill_type=1, rate=4.35)
hero21.add_synergy(10)
hero21.add_synergy(23)

hero_attributes_22 = {
    "health": [800, 1440, 2592],
    "defense": [50, 50, 50],
    "sp_defense": [50, 50, 50],
    "attack": [60, 90, 135],
    "attack_speed": [0.6, 0.6, 0.6],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [0, 0, 0],
    "power": [80, 80, 80]
}
hero22 = Hero(name="Hero22", cost=2, attributes=hero_attributes_22, skill_type=2, rate=4.67)
hero22.add_synergy(10)
hero22.add_synergy(21)

hero_attributes_23 = {
    "health": [750, 1350, 2430],
    "defense": [40, 40, 40],
    "sp_defense": [40, 40, 40],
    "attack": [60, 90, 135],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [0, 0, 0],
    "power": [50, 50, 50]
}
hero23 = Hero(name="Hero23", cost=2, attributes=hero_attributes_23, skill_type=1, rate=4.66)
hero23.add_synergy(11)
hero23.add_synergy(25)
hero23.add_synergy(20)

hero_attributes_24 = {
    "health": [650, 1170, 2106],
    "defense": [35, 35, 35],
    "sp_defense": [35, 35, 35],
    "attack": [55, 83, 124],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [40, 40, 40],
    "power": [100, 100, 100]
}
hero24 = Hero(name="Hero24", cost=2, attributes=hero_attributes_24, skill_type=3, rate=4.72)
hero24.add_synergy(15)
hero24.add_synergy(24)

hero_attributes_25 = {
    "health": [550, 990, 1782],
    "defense": [20, 20, 20],
    "sp_defense": [20, 20, 20],
    "attack": [40, 60, 90],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [25, 25, 25],
    "power": [75, 75, 75]
}
hero25 = Hero(name="Hero25", cost=2, attributes=hero_attributes_25, skill_type=1, rate=4.13)
hero25.add_synergy(9)
hero25.add_synergy(22)

hero_attributes_26 = {
    "health": [800, 1440, 2592],
    "defense": [45, 45, 45],
    "sp_defense": [45, 45, 45],
    "attack": [60, 90, 135],
    "attack_speed": [0.6, 0.6, 0.6],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [60, 60, 60],
    "power": [110, 110, 110]
}
hero26 = Hero(name="Hero26", cost=2, attributes=hero_attributes_26, skill_type=1, rate=5.49)
hero26.add_synergy(12)
hero26.add_synergy(24)

hero_attributes_27 = {
    "health": [700, 1260, 2268],
    "defense": [25, 25, 25],
    "sp_defense": [25, 25, 25],
    "attack": [40, 60, 90],
    "attack_speed": [0.65, 0.65, 0.65],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [35, 35, 35],
    "power": [80, 80, 80]
}
hero27 = Hero(name="Hero27", cost=3, attributes=hero_attributes_27, skill_type=1, rate=4.32)
hero27.add_synergy(3)
hero27.add_synergy(20)

hero_attributes_28 = {
    "health": [700, 1260, 2268],
    "defense": [25, 25, 25],
    "sp_defense": [25, 25, 25],
    "attack": [45, 68, 101],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [0, 0, 0],
    "power": [50, 50, 50]
}
hero28 = Hero(name="Hero28", cost=3, attributes=hero_attributes_28, skill_type=1, rate=4.21)
hero28.add_synergy(9)
hero28.add_synergy(23)

hero_attributes_29 = {
    "health": [800, 1440, 2592],
    "defense": [50, 50, 50],
    "sp_defense": [50, 50, 50],
    "attack": [60, 90, 135],
    "attack_speed": [0.6, 0.6, 0.6],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [0, 0, 0],
    "power": [65, 65, 65]
}
hero29 = Hero(name="Hero29", cost=3, attributes=hero_attributes_29, skill_type=2, rate=4.39)
hero29.add_synergy(6)
hero29.add_synergy(28)

hero_attributes_30 = {
    "health": [800, 1440, 2592],
    "defense": [40, 40, 40],
    "sp_defense": [40, 40, 40],
    "attack": [50, 75, 113],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [20, 20, 20],
    "power": [80, 80, 80]
}
hero30 = Hero(name="Hero30", cost=3, attributes=hero_attributes_30, skill_type=1, rate=4.78)
hero30.add_synergy(11)
hero30.add_synergy(26)

hero_attributes_31 = {
    "health": [750, 1350, 2430],
    "defense": [50, 50, 50],
    "sp_defense": [50, 50, 50],
    "attack": [65, 98, 146],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [30, 30, 30],
    "power": [90, 90, 90]
}
hero31 = Hero(name="Hero31", cost=3, attributes=hero_attributes_31, skill_type=1, rate=5.44)
hero31.add_synergy(1)
hero31.add_synergy(19)

hero_attributes_32 = {
    "health": [700, 1260, 2268],
    "defense": [25, 25, 25],
    "sp_defense": [25, 25, 25],
    "attack": [60, 90, 135],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [30, 30, 30],
    "power": [80, 80, 80]
}
hero32 = Hero(name="Hero32", cost=3, attributes=hero_attributes_32, skill_type=3, rate=4.85)
hero32.add_synergy(5)
hero32.add_synergy(22)

hero_attributes_33 = {
    "health": [700, 1260, 2268],
    "defense": [30, 30, 30],
    "sp_defense": [30, 30, 30],
    "attack": [40, 60, 90],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [0, 0, 0],
    "power": [60, 60, 60]
}
hero33 = Hero(name="Hero33", cost=3, attributes=hero_attributes_33, skill_type=1, rate=4.35)
hero33.add_synergy(8)
hero33.add_synergy(21)

hero_attributes_34 = {
    "health": [800, 1440, 2592],
    "defense": [40, 40, 40],
    "sp_defense": [40, 40, 40],
    "attack": [50, 75, 113],
    "attack_speed": [0.8, 0.8, 0.8],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [0, 0, 0],
    "power": [45, 45, 45]
}
hero34 = Hero(name="Hero34", cost=3, attributes=hero_attributes_34, skill_type=1, rate=4.43)
hero34.add_synergy(15)
hero34.add_synergy(21)
hero34.add_synergy(26)

hero_attributes_35 = {
    "health": [800, 1440, 2592],
    "defense": [45, 45, 45],
    "sp_defense": [45, 45, 45],
    "attack": [60, 90, 135],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [50, 50, 50],
    "power": [70, 70, 70]
}
hero35 = Hero(name="Hero35", cost=3, attributes=hero_attributes_35, skill_type=1, rate=4.32)
hero35.add_synergy(3)
hero35.add_synergy(16)

hero_attributes_36 = {
    "health": [650, 1170, 2106],
    "defense": [25, 25, 25],
    "sp_defense": [25, 25, 25],
    "attack": [50, 75, 113],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [10, 10, 10],
    "power": [60, 60, 60]
}
hero36 = Hero(name="Hero36", cost=3, attributes=hero_attributes_36, skill_type=1, rate=4.44)
hero36.add_synergy(10)
hero36.add_synergy(25)
hero36.add_synergy(28)

hero_attributes_37 = {
    "health": [950, 1710, 3078],
    "defense": [35, 35, 35],
    "sp_defense": [35, 35, 35],
    "attack": [80, 120, 180],
    "attack_speed": [0.5, 0.5, 0.5],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [80, 80, 80],
    "power": [140, 140, 140]
}
hero37 = Hero(name="Hero37", cost=3, attributes=hero_attributes_37, skill_type=3, rate=4.26)
hero37.add_synergy(6)
hero37.add_synergy(16)

hero_attributes_38 = {
    "health": [800, 1440, 2592],
    "defense": [45, 45, 45],
    "sp_defense": [45, 45, 45],
    "attack": [50, 75, 113],
    "attack_speed": [0.65, 0.65, 0.65],
    "ct": [0.25, 0.25, 0.25],
    "distance": [2, 2, 2],
    "pre_power": [50, 50, 50],
    "power": [120, 120, 120]
}
hero38 = Hero(name="Hero38", cost=3, attributes=hero_attributes_38, skill_type=3, rate=5.03)
hero38.add_synergy(12)
hero38.add_synergy(19)
hero38.add_synergy(17)

hero_attributes_39 = {
    "health": [700, 1260, 2268],
    "defense": [25, 25, 25],
    "sp_defense": [25, 25, 25],
    "attack": [60, 90, 135],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [30, 30, 30],
    "power": [90, 90, 90]
}
hero39 = Hero(name="Hero39", cost=3, attributes=hero_attributes_39, skill_type=1, rate=4.49)
hero39.add_synergy(12)
hero39.add_synergy(27)
hero39.add_synergy(20)

hero_attributes_40 = {
    "health": [1000, 1800, 3240],
    "defense": [60, 60, 60],
    "sp_defense": [60, 60, 60],
    "attack": [60, 90, 135],
    "attack_speed": [0.65, 0.65, 0.65],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [100, 100, 100],
    "power": [180, 180, 180]
}
hero40 = Hero(name="Hero40", cost=4, attributes=hero_attributes_40, skill_type=1, rate=4.59)
hero40.add_synergy(7)
hero40.add_synergy(22)

hero_attributes_41 = {
    "health": [1000, 1800, 3240],
    "defense": [50, 50, 50],
    "sp_defense": [50, 50, 50],
    "attack": [60, 90, 135],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [70, 70, 70],
    "power": [150, 150, 150]
}
hero41 = Hero(name="Hero41", cost=4, attributes=hero_attributes_41, skill_type=2, rate=4.58)
hero41.add_synergy(11)
hero41.add_synergy(16)

hero_attributes_42 = {
    "health": [1000, 1800, 3240],
    "defense": [60, 60, 60],
    "sp_defense": [60, 60, 60],
    "attack": [60, 90, 135],
    "attack_speed": [0.6, 0.6, 0.6],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [90, 90, 90],
    "power": [170, 170, 170]
}
hero42 = Hero(name="Hero42", cost=4, attributes=hero_attributes_42, skill_type=3, rate=4.56)
hero42.add_synergy(6)
hero42.add_synergy(20)

hero_attributes_43 = {
    "health": [1100, 1980, 3564],
    "defense": [60, 60, 60],
    "sp_defense": [60, 60, 60],
    "attack": [60, 90, 135],
    "attack_speed": [0.6, 0.6, 0.6],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [60, 60, 60],
    "power": [120, 120, 120]
}
hero43 = Hero(name="Hero43", cost=4, attributes=hero_attributes_43, skill_type=2, rate=4.88)
hero43.add_synergy(1)
hero43.add_synergy(24)

hero_attributes_44 = {
    "health": [850, 1530, 2754],
    "defense": [35, 35, 35],
    "sp_defense": [35, 35, 35],
    "attack": [45, 68, 101],
    "attack_speed": [0.8, 0.8, 0.8],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [60, 60, 60],
    "power": [120, 120, 120]
}
hero44 = Hero(name="Hero40", cost=4, attributes=hero_attributes_44, skill_type=1, rate=4.65)
hero44.add_synergy(7)
hero44.add_synergy(26)

hero_attributes_45 = {
    "health": [750, 1350, 2430],
    "defense": [30, 30, 30],
    "sp_defense": [30, 30, 30],
    "attack": [30, 45, 68],
    "attack_speed": [0.8, 0.8, 0.8],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [40, 40, 40],
    "power": [50, 50, 50]
}
hero45 = Hero(name="Hero45", cost=4, attributes=hero_attributes_45, skill_type=1, rate=5.10)
hero45.add_synergy(12)
hero45.add_synergy(23)

hero_attributes_46 = {
    "health": [750, 1350, 2430],
    "defense": [25, 25, 25],
    "sp_defense": [25, 25, 25],
    "attack": [65, 98, 146],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [50, 50, 50],
    "power": [100, 100, 100]
}
hero46 = Hero(name="Hero46", cost=4, attributes=hero_attributes_46, skill_type=1, rate=4.47)
hero46.add_synergy(6)
hero46.add_synergy(18)
hero46.add_synergy(16)

hero_attributes_47 = {
    "health": [850, 1530, 2754],
    "defense": [45, 45, 45],
    "sp_defense": [45, 45, 45],
    "attack": [75, 113, 169],
    "attack_speed": [0.9, 0.9, 0.9],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [70, 70, 70],
    "power": [160, 160, 160]
}
hero47 = Hero(name="Hero47", cost=4, attributes=hero_attributes_47, skill_type=1, rate=4.27)
hero47.add_synergy(10)
hero47.add_synergy(21)

hero_attributes_48 = {
    "health": [1000, 1800, 3240],
    "defense": [50, 50, 50],
    "sp_defense": [50, 50, 50],
    "attack": [70, 105, 158],
    "attack_speed": [0.55, 0.55, 0.55],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [30, 30, 30],
    "power": [80, 80, 80]
}
hero48 = Hero(name="Hero48", cost=4, attributes=hero_attributes_48, skill_type=1, rate=4.86)
hero48.add_synergy(5)
hero48.add_synergy(27)

hero_attributes_49 = {
    "health": [950, 1710, 3078],
    "defense": [45, 45, 45],
    "sp_defense": [45, 45, 45],
    "attack": [75, 113, 169],
    "attack_speed": [0.8, 0.8, 0.8],
    "ct": [0.25, 0.25, 0.25],
    "distance": [2, 2, 2],
    "pre_power": [20, 20, 20],
    "power": [60, 60, 60]
}
hero49 = Hero(name="Hero49", cost=4, attributes=hero_attributes_49, skill_type=1, rate=4.67)
hero49.add_synergy(11)
hero49.add_synergy(19)

hero_attributes_50 = {
    "health": [750, 1350, 2430],
    "defense": [30, 30, 30],
    "sp_defense": [30, 30, 30],
    "attack": [45, 68, 101],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [0, 0, 0],
    "power": [50, 50, 50]
}
hero50 = Hero(name="Hero50", cost=4, attributes=hero_attributes_50, skill_type=3, rate=4.30)
hero50.add_synergy(5)
hero50.add_synergy(17)

hero_attributes_51 = {
    "health": [750, 1350, 2430],
    "defense": [25, 25, 25],
    "sp_defense": [25, 25, 25],
    "attack": [65, 98, 146],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [20, 20, 20],
    "power": [100, 100, 100]
}
hero51 = Hero(name="Hero51", cost=4, attributes=hero_attributes_51, skill_type=1, rate=4.19)
hero51.add_synergy(3)
hero51.add_synergy(28)

hero_attributes_52 = {
    "health": [1111, 2000, 3600],
    "defense": [30, 30, 30],
    "sp_defense": [30, 30, 30],
    "attack": [50, 75, 113],
    "attack_speed": [0.85, 0.85, 0.85],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [0, 0, 0],
    "power": [0, 0, 0]
}
hero52 = Hero(name="Hero52", cost=4, attributes=hero_attributes_52, skill_type=3, rate=4.79)
hero52.add_synergy(15)
hero52.add_synergy(18)
hero52.add_synergy(16)

hero_attributes_53 = {
    "health": [900, 1620, 2916],
    "defense": [65, 65, 65],
    "sp_defense": [65, 65, 65],
    "attack": [70, 105, 158],
    "attack_speed": [0.6, 0.6, 0.6],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [70, 70, 70],
    "power": [160, 160, 160]
}
hero53 = Hero(name="Hero53", cost=5, attributes=hero_attributes_53, skill_type=1, rate=3.89)
hero53.add_synergy(4)
hero53.add_synergy(21)

hero_attributes_54 = {
    "health": [750, 1350, 2430],
    "defense": [30, 30, 30],
    "sp_defense": [30, 30, 30],
    "attack": [40, 60, 90],
    "attack_speed": [0.75, 0.75, 0.75],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [80, 80, 80],
    "power": [140, 140, 140]
}
hero54 = Hero(name="Hero54", cost=5, attributes=hero_attributes_54, skill_type=1, rate=3.87)
hero54.add_synergy(11)
hero54.add_synergy(20)
hero54.add_synergy(28)

hero_attributes_55 = {
    "health": [850, 1530, 2754],
    "defense": [40, 40, 40],
    "sp_defense": [40, 40, 40],
    "attack": [50, 75, 113],
    "attack_speed": [0.85, 0.85, 0.85],
    "ct": [0.25, 0.25, 0.25],
    "distance": [4, 4, 4],
    "pre_power": [0, 0, 0],
    "power": [50, 50, 50]
}
hero55 = Hero(name="Hero55", cost=5, attributes=hero_attributes_55, skill_type=1, rate=3.72)
hero55.add_synergy(8)
hero55.add_synergy(22)

hero_attributes_56 = {
    "health": [1100, 1980, 3564],
    "defense": [50, 50, 50],
    "sp_defense": [50, 50, 50],
    "attack": [80, 120, 180],
    "attack_speed": [0.85, 0.85, 0.85],
    "ct": [0.25, 0.25, 0.25],
    "distance": [2, 2, 2],
    "pre_power": [20, 20, 20],
    "power": [70, 70, 70]
}
hero56 = Hero(name="Hero56", cost=5, attributes=hero_attributes_56, skill_type=1, rate=4.72)
hero56.add_synergy(12)
hero56.add_synergy(19)
hero56.add_synergy(29)

hero_attributes_57 = {
    "health": [900, 1620, 2916],
    "defense": [70, 70, 70],
    "sp_defense": [70, 70, 70],
    "attack": [80, 120, 180],
    "attack_speed": [0.8, 0.8, 0.8],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [0, 0, 0],
    "power": [50, 50, 50]
}
hero57 = Hero(name="Hero57", cost=5, attributes=hero_attributes_57, skill_type=1, rate=4.15)
hero57.add_synergy(2)
hero57.add_synergy(23)

hero_attributes_58 = {
    "health": [1000, 1800, 3240],
    "defense": [30, 30, 30],
    "sp_defense": [30, 30, 30],
    "attack": [80, 120, 180],
    "attack_speed": [0.85, 0.85, 0.85],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [90, 90, 90],
    "power": [180, 180, 180]
}
hero58 = Hero(name="Hero58", cost=5, attributes=hero_attributes_58, skill_type=1, rate=3.65)
hero58.add_synergy(9)
hero58.add_synergy(24)

hero_attributes_59 = {
    "health": [1000, 1800, 3240],
    "defense": [50, 50, 50],
    "sp_defense": [50, 50, 50],
    "attack": [60, 90, 135],
    "attack_speed": [0.7, 0.7, 0.7],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [0, 0, 0],
    "power": [70, 70, 70]
}
hero59 = Hero(name="Hero59", cost=5, attributes=hero_attributes_59, skill_type=3, rate=3.84)
hero59.add_synergy(15)
hero59.add_synergy(17)

hero_attributes_60 = {
    "health": [1200, 2160, 3888],
    "defense": [65, 65, 65],
    "sp_defense": [65, 65, 65],
    "attack": [70, 105, 158],
    "attack_speed": [0.8, 0.8, 0.8],
    "ct": [0.25, 0.25, 0.25],
    "distance": [1, 1, 1],
    "pre_power": [70, 70, 70],
    "power": [150, 150, 150]
}
hero60 = Hero(name="Hero60", cost=5, attributes=hero_attributes_60, skill_type=1, rate=3.77)
hero60.add_synergy(14)
hero60.add_synergy(27)

array1 = array(5.30)  # K/DA 厄运小姐&妮寇
array1.add_core_hero([hero4, hero12, hero25, hero21, hero34, hero28, hero36])
array1.add_flex_hero([hero58])
array1.recommend_weapon_for_hero(hero25, [h_weapon17])
array1.recommend_weapon_for_hero(hero21, [h_weapon38])
array1.recommend_weapon_for_hero(hero34, [h_weapon23, h_weapon26])
array1.recommend_weapon_for_hero(hero28, [h_weapon7, h_weapon12, h_weapon20])
array1.recommend_weapon_for_hero(hero36, [h_weapon38, h_weapon26, h_weapon23])
array1.weapon_recommend([l_weapon5, l_weapon7, l_weapon6, l_weapon3, l_weapon2, l_weapon4])

array2 = array(5.30)  # K/DA 巴德&妮寇
array2.add_core_hero([hero4, hero12, hero25, hero34, hero36])
array2.add_flex_hero([hero21, hero28, hero55])
array2.recommend_weapon_for_hero(hero25, [h_weapon17, h_weapon4, h_weapon14])
array2.recommend_weapon_for_hero(hero34, [h_weapon23, h_weapon26])
array2.recommend_weapon_for_hero(hero36, [h_weapon38, h_weapon23, h_weapon26])
array2.recommend_weapon_for_hero(hero21, [h_weapon38])
array2.recommend_weapon_for_hero(hero28, [h_weapon7])
array2.weapon_recommend([l_weapon5, l_weapon7, l_weapon6, l_weapon9, l_weapon2, l_weapon3])

array3 = array(4.10)  # 乡村乐 沙弥啦&厄加特
array3.add_core_hero({hero9, hero29, hero35, hero39, hero27, hero37, hero51})
array3.add_flex_hero([hero60])
array3.recommend_weapon_for_hero(hero29, [h_weapon19, h_weapon23, h_weapon24])
array3.recommend_weapon_for_hero(hero35, [h_weapon6, h_weapon12, h_weapon2])
array3.recommend_weapon_for_hero(hero27, [h_weapon2, h_weapon34])
array3.recommend_weapon_for_hero(hero51, [h_weapon28])
array3.recommend_weapon_for_hero(hero39, [h_weapon19])
array3.weapon_recommend([l_weapon2, l_weapon7, l_weapon9, l_weapon1, l_weapon4, l_weapon5])

array4 = array(4.30)  # 音浪刺客 卡特琳娜&劫
array4.add_core_hero([hero3, hero12, hero18, hero36, hero50, hero59])
array4.add_flex_hero([hero4, hero38])
array4.recommend_weapon_for_hero(hero18, [h_weapon17, h_weapon13, h_weapon14])
array4.recommend_weapon_for_hero(hero36, [h_weapon26, h_weapon19])
array4.recommend_weapon_for_hero(hero50, [h_weapon5, h_weapon30, h_weapon20])
array4.recommend_weapon_for_hero(hero59, [h_weapon20])
array4.recommend_weapon_for_hero(hero38, [h_weapon5])
array4.weapon_recommend([l_weapon1, l_weapon9, l_weapon7, l_weapon5, l_weapon6, l_weapon4])

array5 = array(4.82)  # K/DA 阿狸&阿卡丽
array5.add_core_hero([hero12, hero22, hero34, hero36, hero47, hero46])
array5.add_flex_hero([hero4, hero21])
array5.recommend_weapon_for_hero(hero22, [h_weapon4])
array5.recommend_weapon_for_hero(hero34, [h_weapon23])
array5.recommend_weapon_for_hero(hero36, [h_weapon23, h_weapon26])
array5.recommend_weapon_for_hero(hero47, [h_weapon18, h_weapon4, h_weapon3])
array5.recommend_weapon_for_hero(hero46, [h_weapon20, h_weapon9, h_weapon5])
array5.weapon_recommend([l_weapon4, l_weapon5, l_weapon7, l_weapon6, l_weapon1, l_weapon2])

array6 = array(4.77)  # 护卫 金克丝&潘森
array6.add_core_hero([hero8, hero10, hero19, hero17, hero29])
array6.add_flex_hero([hero36, hero37, hero51])
array6.recommend_weapon_for_hero(hero8, [h_weapon12, h_weapon7, h_weapon2])
array6.recommend_weapon_for_hero(hero19, [h_weapon21, h_weapon24, h_weapon26])
array6.recommend_weapon_for_hero(hero17, [h_weapon2, h_weapon12])
array6.recommend_weapon_for_hero(hero29, [h_weapon41])
array6.recommend_weapon_for_hero(hero51, [h_weapon41])
array6.weapon_recommend([l_weapon9, l_weapon2, l_weapon5, l_weapon6, l_weapon7, l_weapon8])

array7 = array(4.13)  # K/DA 安妮
array7.add_core_hero([hero1, hero4, hero12, hero34, hero36, hero47])
array7.add_flex_hero([hero29, hero33])
array7.recommend_weapon_for_hero(hero1, [h_weapon11, h_weapon7])
array7.recommend_weapon_for_hero(hero34, [h_weapon15, h_weapon23])
array7.recommend_weapon_for_hero(hero47, [h_weapon4, h_weapon18])
array7.recommend_weapon_for_hero(hero29, [h_weapon23])
array7.recommend_weapon_for_hero(hero33, [h_weapon18])
array7.weapon_recommend([l_weapon4, l_weapon7, l_weapon5, l_weapon2, l_weapon6, l_weapon3])

array8 = array(3.99)  # K/DA 安妮&阿木木
array8.add_core_hero([hero1, hero4, hero12, hero29, hero34, hero36, hero47])
array8.add_flex_hero([hero33])
array8.recommend_weapon_for_hero(hero1, [h_weapon11, h_weapon7])
array8.recommend_weapon_for_hero(hero29, [h_weapon15, h_weapon23, h_weapon24])
array8.recommend_weapon_for_hero(hero34, [h_weapon15])
array8.recommend_weapon_for_hero(hero47, [h_weapon4, h_weapon18])
array8.weapon_recommend([l_weapon4, l_weapon6, l_weapon7, l_weapon2, l_weapon3, l_weapon5])

array9 = array(4.25)  # K/DA 厄运小姐&艾克
array9.add_core_hero([hero4, hero12, hero21, hero34, hero28, hero36])
array9.add_flex_hero([hero25, hero58])
array9.recommend_weapon_for_hero(hero21, [h_weapon38])
array9.recommend_weapon_for_hero(hero34, [h_weapon25, h_weapon19, h_weapon32])
array9.recommend_weapon_for_hero(hero28, [h_weapon7, h_weapon12, h_weapon6])
array9.recommend_weapon_for_hero(hero36, [h_weapon23, h_weapon26])
array9.recommend_weapon_for_hero(hero25, [h_weapon4])
array9.weapon_recommend([l_weapon7, l_weapon5, l_weapon6, l_weapon2, l_weapon9, l_weapon8])

array10 = array(4.11)  # 超级粉丝 卡尔萨斯&阿卡丽
array10.add_core_hero([hero12, hero23, hero36, hero46, hero41, hero54])
array10.add_flex_hero([hero4, hero37])
array10.recommend_weapon_for_hero(hero36, [h_weapon23])
array10.recommend_weapon_for_hero(hero46, [h_weapon20, h_weapon9, h_weapon34])
array10.recommend_weapon_for_hero(hero41, [h_weapon4, h_weapon17])
array10.recommend_weapon_for_hero(hero54, [h_weapon28, h_weapon5])
array10.weapon_recommend([l_weapon9, l_weapon4, l_weapon7, l_weapon3, l_weapon1, l_weapon5])

array11 = array(4.58)  # 迪斯科 崔斯特&布里茨
array11.add_core_hero([hero20, hero34, hero44, hero40, hero60, hero55])
array11.add_flex_hero({hero11, hero6})
array11.recommend_weapon_for_hero(hero44, [h_weapon35, h_weapon19, h_weapon22])
array11.recommend_weapon_for_hero(hero40, [h_weapon4, h_weapon3, h_weapon17])
array11.recommend_weapon_for_hero(hero60, [h_weapon28])
array11.recommend_weapon_for_hero(hero55, [h_weapon4, h_weapon11])
array11.weapon_recommend([l_weapon4, l_weapon2, l_weapon7, l_weapon9, l_weapon1, l_weapon3])

array12 = array(4.77)  # 真实伤害 赛娜&艾克
array12.add_core_hero([hero4, hero12, hero24, hero34, hero36, hero52, hero59])
array12.add_flex_hero([hero7])
array12.recommend_weapon_for_hero(hero24, [h_weapon4, h_weapon7, h_weapon11])
array12.recommend_weapon_for_hero(hero34, [h_weapon19, h_weapon23, h_weapon26])
array12.recommend_weapon_for_hero(hero36, [h_weapon19])
array12.recommend_weapon_for_hero(hero52, [h_weapon5, h_weapon20])
array12.weapon_recommend([l_weapon7, l_weapon1, l_weapon6, l_weapon4, l_weapon5, l_weapon9])

array13 = array(5.01)  # 电子舞曲 拉克丝&扎克
array13.add_core_hero([hero20, hero16, hero32, hero48, hero50])
array13.add_flex_hero([hero11, hero40, hero55])
array13.recommend_weapon_for_hero(hero32, [h_weapon13, h_weapon14])
array13.recommend_weapon_for_hero(hero48, [h_weapon26, h_weapon24, h_weapon19])
array13.recommend_weapon_for_hero(hero50, [h_weapon5, h_weapon28])
array13.recommend_weapon_for_hero(hero40, [h_weapon8])
array13.weapon_recommend([l_weapon6, l_weapon2, l_weapon3, l_weapon4, l_weapon7, l_weapon1])

array14 = array(4.92)  # 护卫 薇古丝&阿木木
array14.add_core_hero([hero4, hero12, hero29, hero36, hero37, hero46, hero51])
array14.add_flex_hero([hero42])
array14.recommend_weapon_for_hero(hero29, [h_weapon23, h_weapon26, h_weapon28])
array14.recommend_weapon_for_hero(hero37, [h_weapon17, h_weapon14, h_weapon4])
array14.recommend_weapon_for_hero(hero46, [h_weapon28, h_weapon20])
array14.weapon_recommend([l_weapon9, l_weapon4, l_weapon1, l_weapon5, l_weapon3, l_weapon7])

array15 = array(5.16)  # 舞者 厄加特&波比
array15.add_core_hero([hero14, hero39, hero27, hero42])
array15.add_flex_hero([hero35, hero41, hero51, hero54])
array15.recommend_weapon_for_hero(hero39, [h_weapon23, h_weapon22])
array15.recommend_weapon_for_hero(hero27, [h_weapon28, h_weapon6, h_weapon34])
array15.recommend_weapon_for_hero(hero35, [h_weapon6])
array15.recommend_weapon_for_hero(hero51, [h_weapon19])
array15.recommend_weapon_for_hero(hero54, [h_weapon5])
array15.weapon_recommend([l_weapon2, l_weapon9, l_weapon1, l_weapon5, l_weapon6, l_weapon4])
######################
Heros = [hero1, hero1, hero2, hero3, hero4, hero5, hero6, hero7, hero8, hero9, hero10,
         hero11, hero12, hero13, hero14, hero15, hero16, hero17, hero18, hero19, hero20,
         hero21, hero22, hero23, hero24, hero25, hero26, hero27, hero28, hero29, hero30,
         hero31, hero32, hero33, hero34, hero35, hero36, hero37, hero38, hero39, hero40,
         hero41, hero42, hero43, hero44, hero45, hero46, hero47, hero48, hero49, hero50,
         hero51, hero52, hero53, hero54, hero55, hero56, hero57, hero58, hero59, hero60]
Synergies = [synergy1, synergy1, synergy2, synergy3, synergy4, synergy5, synergy6, synergy7, synergy8, synergy9,
             synergy10,
             synergy11, synergy12, synergy13, synergy14, synergy15, synergy16, synergy17, synergy18, synergy19,
             synergy20,
             synergy21, synergy22, synergy23, synergy24, synergy25, synergy26, synergy27, synergy28, synergy29]
############################
#########################
team1 = [[4, 3, 1], [12, 3, 1], [25, 3, 1], [21, 3, 1], [34, 3, 1], [28, 3, 1], [36, 3, 1],
         [58, 3, 0]]  # [[序号，数量，core(1)/flex(0)],]
team2 = [[4, 3, 1], [12, 3, 1], [25, 3, 1], [34, 3, 1], [36, 3, 1], [21, 3, 0], [28, 3, 0], [55, 3, 0]]
team3 = [[9, 3, 1], [29, 3, 1], [35, 3, 1], [39, 3, 1], [27, 3, 1], [37, 3, 1], [51, 3, 1], [60, 3, 0]]
team4 = [[3, 3, 1], [12, 3, 1], [18, 3, 1], [36, 3, 1], [50, 3, 1], [59, 3, 1], [4, 3, 0],
         [38, 3, 0]]  # [[序号，数量，core(1)/flex(0)],]
team5 = [[12, 3, 1], [22, 3, 1], [34, 3, 1], [36, 3, 1], [47, 3, 1], [46, 3, 1], [4, 3, 0], [21, 3, 0]]
team6 = [[8, 3, 1], [10, 3, 1], [19, 3, 1], [17, 3, 1], [29, 3, 1], [36, 3, 0], [37, 3, 0], [51, 3, 0]]
team7 = [[1, 3, 1], [4, 3, 1], [12, 3, 1], [34, 3, 1], [36, 3, 1], [47, 3, 1], [29, 3, 0],
         [33, 3, 0]]  # [[序号，数量，core(1)/flex(0)],]
team8 = [[1, 3, 1], [4, 3, 1], [12, 3, 1], [29, 3, 1], [34, 3, 1], [36, 3, 1], [47, 3, 1], [33, 3, 0]]
team9 = [[4, 3, 1], [12, 3, 1], [21, 3, 1], [34, 3, 1], [28, 3, 1], [36, 3, 1], [25, 3, 0], [58, 3, 0]]
team10 = [[12, 3, 1], [23, 3, 1], [36, 3, 1], [46, 3, 1], [41, 3, 1], [54, 3, 1], [4, 3, 0],
          [37, 3, 0]]  # [[序号，数量，core(1)/flex(0)],]
team11 = [[20, 3, 1], [34, 3, 1], [44, 3, 1], [40, 3, 1], [60, 3, 1], [55, 3, 1], [11, 3, 0], [6, 3, 0]]
team12 = [[4, 3, 1], [12, 3, 1], [24, 3, 1], [34, 3, 1], [36, 3, 1], [52, 3, 1], [59, 3, 1], [7, 3, 0]]
team13 = [[20, 3, 1], [16, 3, 1], [32, 3, 1], [48, 3, 1], [50, 3, 1], [11, 3, 0], [40, 3, 0],
          [55, 3, 0]]  # [[序号，数量，core(1)/flex(0)],]
team14 = [[4, 3, 1], [12, 3, 1], [29, 3, 1], [36, 3, 1], [37, 3, 1], [46, 3, 1], [51, 3, 1], [42, 3, 0]]
team15 = [[14, 3, 1], [39, 3, 1], [27, 3, 1], [42, 3, 1], [35, 3, 0], [41, 3, 0], [51, 3, 0], [54, 3, 0]]


class find_team:
    def __init__(self):
        self.teams = [team1, team2, team3]
        self.matching_rate = []

    def find_best_match(self, now_team):  # now_team:[61个数量]
        for team in self.teams:
            temp = 0
            for role in team:
                if role[2] == 1:
                    temp = temp + now_team[role[0]] * 2
                else:
                    temp = temp + now_team[role[0]] * 1
            self.matching_rate.append(temp)

        big = 0
        for index, item in enumerate(self.matching_rate):
            if (self.matching_rate[big] < item):
                big = index
        return self.teams[big]


f = find_team()
#######################################

level = [2, 2, 6, 10, 20, 36, 56, 80, 100]


class control:
    def __init__(self):
        self.coin = 2
        self.target = []  # [[序号，数量，core(1)/flex(0)]]下同
        self.current = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]  # 61个0
        self.coin_value = 2.2  #
        self.level = 1
        self.state = 0

    def get_state(self):
        return self.state
    def renew_current(self,now):
        self.current = now[:]
    def renew_state(self):
        self.state = 1

    def get_current(self):
        ans = []
        for i, role in enumerate(self.current):
            if role > 0:
                temp = []
                temp.append(i)
                temp.append(role)
                ans.append(temp)
        return ans

    def renew_coin(self, coin):
        self.coin = coin

    def renew_coin_value(self, value):
        self.coin_value = value

    def upgrade(self):
        if self.coin > level[self.level - 1]:
            if 7 <= self.level <= 9:
                if self.coin - level[self.level - 1] >= 40:
                    self.coin = self.coin - level[self.level - 1]
                    self.level = self.level + 1
                    return 1

            elif self.level < 7:
                if self.level <= 3:
                    if self.coin - level[self.level - 1] > 0:
                        self.coin = self.coin - level[self.level - 1]
                        self.level = self.level + 1
                        return 1
                    else:
                        if self.coin - level[self.level - 1] >= 10:
                            self.coin = self.coin - level[self.level - 1]
                            self.level = self.level + 1
                            return 1
        return 0

    def add_buyed_hero(self, buy):  # buy = [序号，]
        for num in buy:
            self.current[num] = self.current[num] + 1

    def sell_hero(self, sold_num):  # sold_num为单个序号
        self.current[sold_num] = self.current[sold_num] - 1
        self.coin = self.coin + Heros[sold_num].get_cost()

    def add_target(self):
        self.target = f.find_best_match(self.current)

    def sort_best(self, shop):  # 选择牌与刷新,升级->选牌->刷新#shop = [序号,]
        choices = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 1],
                   [0, 0, 1, 1, 0], [0, 0, 1, 1, 1],
                   [0, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 1, 1, 0, 1],
                   [0, 1, 1, 1, 0], [0, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0], [1, 0, 0, 0, 1], [1, 0, 0, 1, 0], [1, 0, 0, 1, 1], [1, 0, 1, 0, 0], [1, 0, 1, 0, 1],
                   [1, 0, 1, 1, 0], [1, 0, 1, 1, 1],
                   [1, 1, 0, 0, 0], [1, 1, 0, 0, 1], [1, 1, 0, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 0, 1],
                   [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

        values = []
        ii = 0
        choice = choices[ii]
        while ii < 32:
            ########
            temp_value = 0.0
            temp_coin = self.coin
            temp_team = self.current[:]
            for index, item in enumerate(shop):
                if choice[index] == 1:
                    temp_coin = temp_coin - Heros[item].get_cost()
                    temp_team[item] = temp_team[item] + 1
            temp_relation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 30个0
            total = 0
            for index1, item1 in enumerate(temp_team):
                if item1 > 0:
                    total = total + 1
                    for relation in Heros[index].synergies:
                        temp_relation[relation] = temp_relation[relation] + 1
                    if item1 >= 9:
                        temp_value = temp_value + Heros[index1].rate * Heros[index1].rate * 9 + 36.0
                    elif item1 < 9 and item1 >= 6:
                        temp_value = temp_value + Heros[index1].rate * Heros[index1].rate * item1 + 18.0
                    elif item1 < 6 and item1 >= 3:
                        temp_value = temp_value + Heros[index1].rate * Heros[index1].rate * item1 + 8.0
                    else:
                        temp_value = temp_value + Heros[index1].rate * Heros[index1].rate * item1
            for index2, item2 in enumerate(temp_relation):
                if index2 < len(Synergies) and len(Synergies[index2].stages) > 0:
                    if item2 >= Synergies[index2].stages[0]:
                        for i in range(len(Synergies[index2].stages) - 1, -1, -1):
                            if item2 >= (Synergies[index2].stages[i]):
                                temp_value = temp_value + Synergies[index2].rate[i] * Synergies[index2].rate[
                                    i] * 4 + 6.0
            temp_value = temp_value + temp_coin * self.coin_value
            ##########
            if temp_coin >= 0:
                values.append(temp_value)
            else:
                values.append(0)
            ########
            ii = ii + 1
            choice = choices[ii]
        #######
        big = 0
        for index3, item3 in enumerate(values):
            if (values[big] < item3):
                big = index3
        ##########
        # test = big
        #########
        choice = [0, 0, 0, 0, 0]
        if big >= 16:
            choice[0] = 1
            big = big - 16
        else:
            choice[0] = 0
        if big >= 8:
            choice[1] = 1
            big = big - 8
        else:
            choice[1] = 0
        if big >= 4:
            choice[2] = 1
            big = big - 4
        else:
            choice[2] = 0
        if big >= 2:
            choice[3] = 1
            big = big - 2
        else:
            choice[3] = 0
        if big >= 1:
            choice[4] = 1
            big = big - 1
        else:
            choice[4] = 0
        return choice


def get_high(x):
    h_list = []
    if f == team1:
        for i in array1.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team2:
        for i in array2.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team3:
        for i in array3.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team4:
        for i in array4.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team5:
        for i in array5.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team6:
        for i in array6.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team7:
        for i in array7.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team8:
        for i in array8.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team9:
        for i in array9.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team10:
        for i in array10.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team11:
        for i in array11.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team12:
        for i in array12.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team13:
        for i in array13.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team14:
        for i in array14.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    elif f == team15:
        for i in array15.get_weapon_recommendation(Heros[x]):
            h_list.append(i.number)
    return h_list

def get_low():
    l_list=[]
    if f == team1:
        for i in array1.weapon_recommendations:
            l_list.append(i.number)
    elif f == team2:
        for i in array2.weapon_recommendations:
            l_list.append(i.number)
    elif f == team3:
        for i in array3.weapon_recommendations:
            l_list.append(i.number)
    elif f == team4:
        for i in array4.weapon_recommendations:
            l_list.append(i.number)
    elif f ==team5:
        for i in array5.weapon_recommendations:
            l_list.append(i.number)
    elif f == team6:
        for i in array6.weapon_recommendations:
            l_list.append(i.number)
    elif f == team7:
        for i in array7.weapon_recommendations:
            l_list.append(i.number)
    elif f == team8:
        for i in array8.weapon_recommendations:
            l_list.append(i.number)
    elif f == team9:
        for i in array9.weapon_recommendations:
            l_list.append(i.number)
    elif f == team10:
        for i in array10.weapon_recommendations:
            l_list.append(i.number)
    elif f == team11:
        for i in array11.weapon_recommendations:
            l_list.append(i.number)
    elif f == team12:
        for i in array12.weapon_recommendations:
            l_list.append(i.number)
    elif f == team13:
        for i in array13.weapon_recommendations:
            l_list.append(i.number)
    elif f == team14:
        for i in array14.weapon_recommendations:
            l_list.append(i.number)
    elif f == team15:
        for i in array15.weapon_recommendations:
            l_list.append(i.number)
    return l_list