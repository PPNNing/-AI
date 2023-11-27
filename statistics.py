import math
import numpy

#level = [2,2,6,10,20,36,56,80,100]

class Hero:
    def __init__(self, name, cost, attributes, skill_type,rate):
        self.name = name
        self.cost = cost
        self.attributes = attributes
        self.skill_type = skill_type
        self.synergies = []
        self.weapon = []
        self.rate = rate
        self.each_value = self.cost * (self.rate * self.rate - 5.0)
    def add_synergy(self, synergy):
        if synergy not in self.synergies:
            self.synergies.append(synergy)
            synergy.add_hero(self)

    def get_attributes(self, stage):
        if 1 <= stage <= 3:
            return {attr: values[stage - 1] for attr, values in self.attributes.items()}
        else:
            raise ValueError("Stage must be 1, 2, or 3")

    def add_weapon(self,weapon):
        if weapon not in self.weapon:
            self.weapon.append(weapon)
    
    #def add_rate(self,rate):
    #    self.rate.append(rate)

    #def cal_each_value(self):
       # self.each_value = self.cost * (self.rate * self.rate - 5.0)
      #  return self.each_value

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
    
    def add_stage(self,stage):
        self.stages.append(stage)

    def add_rate(self,rate):
        self.rate.append(rate)
    
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
############################
class teams:
    def __init__(self):
        self.core_teams = [] #用5个列表记录5个阵容并将每个阵容的综合排名记录依次在下面的列表中
        self.flex_teams = []
        self.teams_rate = []

    def find_best_match(self,now_team):#比较已有队伍与上面那五个阵容的匹配率存入下面这个列表并取其中最大值对应的阵容返回
        matching_rate = []
        max = 0
        ######
        return self.core_teams[max],self.flex_teams[max]


############################
class Low_Weapon:
    def __init__(self,name):
        self.name=name
        self.father= []
    
    def add_Father(self, father):
        if father not in self.father:
            self.father.append(father)
            father.add_child(self)


class High_Weapon:
    def __init__(self,name):
        self.name=name
        self.child= []
    def add_child(self,child):
        if child not in self.child:
            self.child.append(child)

class WeaponManager:
    def __init__(self):
        self.weapon= []
    def add_weapon(self, weapon):
        self.weapon.append(weapon)

    def get_weapon(self, name):
        for weapon in self.weapon:
            if weapon.name == name:
                return weapon
        return None
    
    def __repr__(self):
        return ", ".join([weapon.name for weapon in self.weapon])
    
synergy_manager = SynergyManager()

weapon_manager = WeaponManager()

l_weapon1 = Low_Weapon("Low_weapon1")
l_weapon2 = Low_Weapon("Low_weapon2")
l_weapon3 = Low_Weapon("Low_weapon3")
l_weapon4 = Low_Weapon("Low_weapon4")
l_weapon5 = Low_Weapon("Low_weapon5")
l_weapon6 = Low_Weapon("Low_weapon6")
l_weapon7 = Low_Weapon("Low_weapon7")
l_weapon8 = Low_Weapon("Low_weapon8")
l_weapon9 = Low_Weapon("Low_weapon9")
h_weapon1 = High_Weapon("High_weapon1")
h_weapon2 = High_Weapon("High_weapon2")
h_weapon3 = High_Weapon("High_weapon3")
h_weapon4 = High_Weapon("High_weapon4")
h_weapon5 = High_Weapon("High_weapon5")
h_weapon6 = High_Weapon("High_weapon6")
h_weapon7 = High_Weapon("High_weapon7")
h_weapon8 = High_Weapon("High_weapon8")
h_weapon9 = High_Weapon("High_weapon9")
h_weapon10 = High_Weapon("High_weapon10")
h_weapon11 = High_Weapon("High_weapon11")
h_weapon12 = High_Weapon("High_weapon12")
h_weapon13 = High_Weapon("High_weapon13")
h_weapon14 = High_Weapon("High_weapon14")
h_weapon15 = High_Weapon("High_weapon15")
h_weapon16 = High_Weapon("High_weapon16")
h_weapon17 = High_Weapon("High_weapon17")
h_weapon18 = High_Weapon("High_weapon18")
h_weapon19 = High_Weapon("High_weapon19")
h_weapon20 = High_Weapon("High_weapon20")
h_weapon21 = High_Weapon("High_weapon21")
h_weapon22 = High_Weapon("High_weapon22")
h_weapon23 = High_Weapon("High_weapon23")
h_weapon24 = High_Weapon("High_weapon24")
h_weapon25 = High_Weapon("High_weapon25")
h_weapon26 = High_Weapon("High_weapon26")
h_weapon27 = High_Weapon("High_weapon27")
h_weapon28 = High_Weapon("High_weapon28")
h_weapon29 = High_Weapon("High_weapon29")
h_weapon30 = High_Weapon("High_weapon30")
h_weapon31 = High_Weapon("High_weapon31")
h_weapon32 = High_Weapon("High_weapon32")
h_weapon33 = High_Weapon("High_weapon33")
h_weapon34 = High_Weapon("High_weapon34")
h_weapon35 = High_Weapon("High_weapon35")
h_weapon36 = High_Weapon("High_weapon36")
h_weapon37 = High_Weapon("High_weapon37")
h_weapon38 = High_Weapon("High_weapon38")
h_weapon39 = High_Weapon("High_weapon39")
h_weapon40 = High_Weapon("High_weapon40")
h_weapon41 = High_Weapon("High_weapon41")
h_weapon42 = High_Weapon("High_weapon42")
h_weapon43 = High_Weapon("High_weapon43")
h_weapon44 = High_Weapon("High_weapon44")
h_weapon45 = High_Weapon("High_weapon45")
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
synergy1.add_stage([1])
synergy1.add_rate([4.13])
synergy_manager.add_synergy(synergy1)
synergy2 = Synergy("Synergy2")
synergy2.add_stage([1,2])
synergy2.add_rate([4.27,3.92])
synergy_manager.add_synergy(synergy2)
synergy3 = Synergy("Synergy3")
synergy3.add_stage([3,5,7,9])
synergy3.add_rate([4.67,4.98,4.29,1.65])
synergy_manager.add_synergy(synergy3)
synergy4 = Synergy("Synergy4")
synergy4.add_stage([2,3])
synergy4.add_rate([4.34,4.14])
synergy_manager.add_synergy(synergy4)
synergy5 = Synergy("Synergy5")
synergy5.add_stage([3,6,9])
synergy5.add_rate([4.19,4.30,2.11])
synergy_manager.add_synergy(synergy5)
synergy6 = Synergy("Synergy6")
synergy6.add_stage([3,5,7,9])
synergy6.add_rate([4.58,5.37,4.82,2.10])
synergy_manager.add_synergy(synergy6)
synergy7 = Synergy("Synergy7")
synergy7.add_stage([3,6])
synergy7.add_rate([4.61,4.88])
synergy_manager.add_synergy(synergy7)
synergy8 = Synergy("Synergy8")
synergy8.add_stage([2,4,6,9])
synergy8.add_rate([4.50,4.97,5.00,2.62])
synergy_manager.add_synergy(synergy8)
synergy9 = Synergy("Synergy9")
synergy9.add_stage([2,3,4])
synergy9.add_rate([4.43,4.36,4.38])
synergy_manager.add_synergy(synergy9)
synergy10 = Synergy("Synergy10")
synergy10.add_stage([3,6,8])
synergy10.add_rate([4.55,5.00,3.62])
synergy_manager.add_synergy(synergy10)
synergy11 = Synergy("Synergy11")
synergy11.add_hero([2,4,6])
synergy11.add_rate([4.57,4.30,2.86])
synergy_manager.add_synergy(synergy11)
synergy12 = Synergy("Synergy12")
synergy12.add_stage([3,5,7,9])
synergy12.add_rate([4.25,4.78,4.80,2.12])
synergy_manager.add_synergy(synergy12)
synergy13 = Synergy("Synergy13")
synergy13.add_stage([2,3,4])
synergy13.add_rate([4.45,4.86,4.60])
synergy_manager.add_synergy(synergy13)
synergy14 = Synergy("Synergy14")
synergy14.add_stage([2,4,6,8])
synergy14.add_rate([4.43,4.44,4.57,3.74])
synergy_manager.add_synergy(synergy14)
synergy15 = Synergy("Synergy15")
synergy15.add_stage([2,4,6])
synergy15.add_rate([4.50,4.67,4.78,4.06])
synergy_manager.add_synergy(synergy15)
synergy16 = Synergy("Synergy16")
synergy16.add_stage([2,4,6,8])
synergy16.add_rate([4.46,4.65,4.64,4.05])
synergy_manager.add_synergy(synergy16)
synergy17 = Synergy("Synergy17")
synergy17.add_stage([1])
synergy17.add_rate([4.16])
synergy_manager.add_synergy(synergy17)
synergy18 = Synergy("Synergy18")
synergy18.add_stage([2,4,6])
synergy18.add_rate([4.32,4.52,3.46])
synergy_manager.add_synergy(synergy18)
synergy19 = Synergy("Synergy19")
synergy19.add_stage([2,4,6,8])
synergy19.add_rate([4.24,4.45,4.54,3.61])
synergy_manager.add_synergy(synergy19)
synergy20 = Synergy("Synergy20")
synergy20.add_stage([2,4,6])
synergy20.add_rate([4.26,4.52,4.27])
synergy_manager.add_synergy(synergy20)
synergy21 = Synergy("Synergy21")
synergy21.add_stage([2,3,4])
synergy21.add_rate([4.73,4.54,4.89])
synergy_manager.add_synergy(synergy21)
synergy22 = Synergy("Synergy22")
synergy22.add_stage([2,4])
synergy22.add_rate([4.55,4.45])
synergy_manager.add_synergy(synergy22)
synergy23 = Synergy("Synergy23")
synergy23.add_stage([2,4,6])
synergy23.add_rate([4.40,4.09,3.76])
synergy_manager.add_synergy(synergy23)
synergy24 = Synergy("Synergy24")
synergy24.add_stage([2,4,6,8])
synergy24.add_rate([4.39,5.10,4.50,3.22])
synergy_manager.add_synergy(synergy24)
synergy25 = Synergy("Synergy25")
synergy25.add_stage([2,3,4,5])
synergy25.add_rate([4.45,4.66,4.44,4.24])
synergy_manager.add_synergy(synergy25)
synergy26 = Synergy("Synergy26")
synergy26.add_stage([1])
synergy26.add_rate([4.21])
synergy_manager.add_synergy(synergy26)
synergy27 = Synergy("Synergy27")
synergy27.add_stage([1])
synergy27.add_rate([3.94])
synergy_manager.add_synergy(synergy27)
synergy28 = Synergy("Synergy28")
synergy28.add_stage({2,4,6})
synergy28.add_rate([4.55,4.58,3.86])
synergy_manager.add_synergy(synergy28)
synergy29 = Synergy("Synergy29")
hero_attributes_1 = {
    "health" : [500,900,1620],
    "defense" : [15,15,15],
    "sp_defense" : [15,15,15],
    "attack" : [30,45,68],
    "attack_speed" : [0.6,0.6,0.6],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [0,0,0],
    "power" : [0,0,0]
}
hero1 = Hero(name="Hero1",cost=1,attributes=hero_attributes_1,skill_type=1,rate=4.27)
hero1.add_synergy(synergy6)
hero1.add_synergy(synergy21)

hero_attributes_2 = {
    "health" : [700,1260,2268],
    "defense" : [30,30,30],
    "sp_defense" : [30,30,30],
    "attack" : [65,98,146],
    "attack_speed" : [0.5,0.5,0.5],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [40,40,40],
    "power" : [100,100,100]
}
hero2 = Hero(name="Hero2",cost=1,attributes=hero_attributes_2,skill_type=1,rate=4.56)
hero2.add_synergy(synergy11)
hero2.add_synergy(synergy27)

hero_attributes_3 = {
    "health" : [700,1260,2268],
    "defense" : [25,25,25],
    "sp_dedense" : [25,25,25],
    "attack" : [50,75,113],
    "attack_speed" : [0.65,0.65,0.65],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [40,40,40],
    "power" : [80,80,80]
}
hero3 = Hero(name="Hero3",cost=1,attributes=hero_attributes_3,skill_type=2,rate=4.65)
hero3.add_synergy(synergy10)
hero3.add_synergy(synergy17)

hero_attributes_4 = {
    "health" : [650,1170,2106],
    "defense" : [45,45,45],
    "sp_defense" : [45,45,45],
    "attack" : [50,75,113],
    "attack_speed" : [0.6,0.6,0.6],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [50,50,50],
    "power" : [110,110,110]
}
hero4 = Hero(name="Hero4",cost=1,attributes=hero_attributes_4,skill_type=1,rate=4.80)
hero4.add_synergy(synergy15)
hero4.add_synergy(synergy25)
hero4.add_synergy(synergy28)

hero_attributes_5 = {
    "health" : [500,900,1620],
    "defense" : [15,15,15],
    "sp_defense" : [15,15,15],
    "attack" : [35,53,79],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [20,20,20],
    "power" : [70,70,70]
}
hero5 = Hero(name="Hero5",cost=1,attributes=hero_attributes_5,skill_type=3,rate=4.37)
hero5.add_synergy(synergy1)
hero5.add_synergy(synergy23)

hero_attributes_6 = {
    "health" : [500,900,1620],
    "defense" : [20,20,20],
    "sp_defense" : [20,20,20],
    "attack" : [40,60,90],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [0,0,0],
    "power" : [30,30,30]
}
hero6 = Hero(name="Hero6",cost=1,attributes=hero_attributes_6,skill_type=1,rate=4.57)
hero6.add_synergy(synergy7)
hero6.add_synergy(synergy28)

hero_attributes_7 = {
    "health" : [700,1260,2268],
    "defense" : [40,40,40],
    "sp_defense" : [40,40,40],
    "attack" : [55,83,124],
    "attack_speed" : [0.55,0.55,0.55],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [30,30,30],
    "power" : [90,90,90]
}
hero7 = Hero(name="Hero7",cost=1,attributes=hero_attributes_7,skill_type=2,rate=4.46)
hero7.add_synergy(synergy15)
hero7.add_synergy(synergy19)

hero_attributes_8 = {
    "health" : [500,900,1620],
    "defense" : [15,15,15],
    "sp_defense" : [15,15,15],
    "attack" : [40,60,90],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [0,0,0],
    "power" : [50,50,50]
}
hero8 = Hero(name="Hero8",cost=1,attributes=hero_attributes_8,skill_type=1,rate=4.39)
hero8.add_synergy(synergy13)
hero8.add_synergy(synergy24)

hero_attributes_9 = {
    "health" : [504,907,1633],
    "defense" : [14,14,14],
    "sp_defense" : [14,14,14],
    "attack" : [54,81,122],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [44,44,44],
    "power" : [114,114,114]
}
hero9 = Hero(name="Hero9",cost=1,attributes=hero_attributes_9,skill_type=1,rate=4.32)
hero9.add_synergy(synergy3)
hero9.add_synergy(synergy27)

hero_attributes_10 = {
    "health" : [500,900,1620],
    "defense" : [15,15,15],
    "sp_defense" : [15,15,15],
    "attack" : [45,68,101],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [0,0,0],
    "power" : [30,30,30]
}
hero10 = Hero(name="Hero10",cost=1,attributes=hero_attributes_10,skill_type=1,rate=4.57)
hero10.add_synergy(synergy13)
hero10.add_synergy(synergy20)

hero_attributes_11 = {
    "health" : [700,1260,2268],
    "defense" : [40,40,40],
    "sp_defense" : [40,40,40],
    "attack" : [55,83,124],
    "attack_speed" : [0.65,0.65,0.65],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [30,30,30],
    "power" : [80,80,80]
}
hero11 = Hero(name="Hero11",cost=1,attributes=hero_attributes_11,skill_type=3,rate=4.47)
hero11.add_synergy(synergy7)
hero11.add_synergy(synergy22)

hero_attributes_12 = {
    "health" : [700,1260,2268],
    "defense" : [40,40,40],
    "sp_defense" : [40,40,40],
    "attack" : [60,90,135],
    "attack_speed" : [0.55,0.55,0.55],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [40,40,40],
    "power" : [80,80,80]
}
hero12 = Hero(name="Hero12",cost=1,attributes=hero_attributes_12,skill_type=1,rate=4.60)
hero12.add_synergy(synergy10)
hero12.add_synergy(synergy25)
hero12.add_synergy(synergy26)

hero_attributes_13 = {
    "health" : [500,900,1620],
    "defense" : [20,20,20],
    "sp_defense" : [20,20,20],
    "attack" : [40,60,90],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [20,20,20],
    "power" : [70,70,70]
}
hero13 = Hero(name="Hero13",cost=1,attributes=hero_attributes_13,skill_type=1,rate=4.55)
hero13.add_synergy(synergy12)
hero13.add_synergy(synergy26)

hero_attributes_14 = {
    "health" : [800,1440,2592],
    "defense" : [45,45,45],
    "sp_defense" : [45,45,45],
    "attack" : [70,205,158],
    "attack_speed" : [0.5,0.5,0.5],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [60,60,60],
    "power" : [110,110,110]
}
hero14 = Hero(name="Hero14",cost=2,attributes=hero_attributes_14,skill_type=2,rate=4.40)
hero14.add_synergy(synergy11)
hero14.add_synergy(synergy19)

hero_attributes_15 = {
    "health" : [700,1260,2268],
    "defense" : [25,25,25],
    "sp_defense" : [25,25,25],
    "attack" : [55,83,124],
    "attack_speed" : [0.65,0.65,0.65],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [30,30,30],
    "power" : [90,90,90]
}
hero15 = Hero(name="Hero15",cost=2,attributes=hero_attributes_15,skill_type=3,rate=4.42)
hero15.add_synergy(synergy1)
hero15.add_synergy(synergy26)

hero_attributes_16 = {
    "health" : [800,1440,2592],
    "defense" : [50,50,50],
    "sp_defense" : [50,50,50],
    "attack" : [40,60,90],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [40,40,40],
    "power" : [90,90,90]
}
hero16 = Hero(name="Hero16",cost=2,attributes=hero_attributes_16,skill_type=1,rate=4.50)
hero16.add_synergy(synergy5)
hero16.add_synergy(synergy20)

hero_attributes_17 = {
    "health" : [600,1080,1944],
    "defense" : [20,20,20],
    "sp_defense" : [20,20,20],
    "attack" : [55,83,124],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [20,20,20],
    "power" : [70,70,70]
}
hero17 = Hero(name="Hero17",cost=2,attributes=hero_attributes_17,skill_type=1,rate=4.35)
hero17.add_synergy(synergy13)
hero17.add_synergy(synergy16)

hero_attributes_18 = {
    "health" : [800,1440,2592],
    "defense" : [45,45,45],
    "sp_defense" : [45,45,45],
    "attack" : [50,75,113],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [50,50,50],
    "power" : [100,100,100]
}
hero18 = Hero(name="Hero18",cost=2,attributes=hero_attributes_18,skill_type=1,rate=4.61)
hero18.add_synergy(synergy3)
hero18.add_synergy(synergy17)

hero_attributes_19 = {
    "health" : [800,1440,2592],
    "defense" : [50,50,50],
    "sp_defense" : [50,50,50],
    "attack" : [45,68,101],
    "attack_speed" : [0.65,0.65,0.65],
    "ct" : [0.25,0.25,0.25],
    "distance" : [2,2,2],
    "pre_power" : [60,60,60],
    "power" : [135,135,135]
}
hero19 = Hero(name="Hero19",cost=2,attributes=hero_attributes_19,skill_type=2,rate=4.45)
hero19.add_synergy(synergy13)
hero19.add_synergy(synergy28)

hero_attributes_20 = {
    "health" : [550,990,1782],
    "defense" : [20,20,20],
    "sp_defense" : [20,20,20],
    "attack" : [40,60,90],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [20,20,20],
    "power" : [60,60,60]
}
hero20 = Hero(name="Hero20",cost=2,attributes=hero_attributes_20,skill_type=3,rate=4.79)
hero20.add_synergy(synergy7)
hero20.add_synergy(synergy21)
hero20.add_synergy(synergy27)

hero_attributes_21 = {
    "health" : [600,1080,1944],
    "defense" : [20,20,20],
    "sp_defense" : [20,20,20],
    "attack" : [50,75,113],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [10,10,10],
    "power" : [70,70,70]
}
hero21 = Hero(name="Hero21",cost=2,attributes=hero_attributes_21,skill_type=1,rate=4.49)
hero21.add_synergy(synergy10)
hero21.add_synergy(synergy23)

hero_attributes_22 = {
    "health" : [800,1440,2592],
    "defense" : [50,50,50],
    "sp_defense" : [50,50,50],
    "attack" : [60,90,135],
    "attack_speed" : [0.6,0.6,0.6],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [0,0,0],
    "power" : [80,80,80]
}
hero22 = Hero(name="Hero22",cost=2,attributes=hero_attributes_22,skill_type=2,rate=4.76)
hero22.add_synergy(synergy10)
hero22.add_synergy(synergy21)

hero_attributes_23 = {
    "health" : [750,1350,2430],
    "defense" : [40,40,40],
    "sp_defense" : [40,40,40],
    "attack" : [60,90,135],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [0,0,0],
    "power" : [50,50,50]
}
hero23 = Hero(name="Hero23",cost=2,attributes=hero_attributes_23,skill_type=1,rate=4.68)
hero23.add_synergy(synergy11)
hero23.add_synergy(synergy25)
hero23.add_synergy(synergy20)

hero_attributes_24 = {
    "health" : [650,1170,2106],
    "defense" : [35,35,35],
    "sp_defense" : [35,35,35],
    "attack" : [55,83,124],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [40,40,40],
    "power" : [100,100,100]
}
hero24 = Hero(name="Hero24",cost=2,attributes=hero_attributes_24,skill_type=3,rate=4.71)
hero24.add_synergy(synergy15)
hero24.add_synergy(synergy24)

hero_attributes_25 = {
    "health" : [550,990,1782],
    "defense" : [20,20,20],
    "sp_defense" : [20,20,20],
    "attack" : [40,60,90],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [25,25,25],
    "power" : [75,75,75]
}
hero25 = Hero(name="Hero25",cost=2,attributes=hero_attributes_25,skill_type=1,rate=4.61)
hero25.add_synergy(synergy9)
hero25.add_synergy(synergy22)

hero_attributes_26 = {
    "health" : [800,1440,2592],
    "defense" : [45,45,45],
    "sp_defense" : [45,45,45],
    "attack" : [60,90,135],
    "attack_speed" : [0.6,0.6,0.6],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [60,60,60],
    "power" : [110,110,110]
}
hero26 = Hero(name="Hero26",cost=2,attributes=hero_attributes_26,skill_type=1,rate=4.45)
hero26.add_synergy(synergy12)
hero26.add_synergy(synergy24)

hero_attributes_27 = {
    "health" : [700,1260,2268],
    "defense" : [25,25,25],
    "sp_defense" : [25,25,25],
    "attack" : [40,60,90],
    "attack_speed" : [0.65,0.65,0.65],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [35,35,35],
    "power" : [80,80,80]
}
hero27 = Hero(name="Hero27",cost=3,attributes=hero_attributes_27,skill_type=1,rate=4.27)
hero27.add_synergy(synergy3)
hero27.add_synergy(synergy20)

hero_attributes_28 = {
    "health" : [700,1260,2268],
    "defense" : [25,25,25],
    "sp_defense" : [25,25,25],
    "attack" : [45,68,101],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [0,0,0],
    "power" : [50,50,50]
}
hero28 = Hero(name="Hero28",cost=3,attributes=hero_attributes_28,skill_type=1,rate=4.27)
hero28.add_synergy(synergy9)
hero28.add_synergy(synergy23)

hero_attributes_29 = {
    "health" : [800,1440,2592],
    "defense" : [50,50,50],
    "sp_defense" : [50,50,50],
    "attack" : [60,90,135],
    "attack_speed" : [0.6,0.6,0.6],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [0,0,0],
    "power" : [65,65,65]
}
hero29 = Hero(name="Hero29",cost=3,attributes=hero_attributes_29,skill_type=2,rate=4.51)
hero29.add_synergy(synergy6)
hero29.add_synergy(synergy28)

hero_attributes_30 = {
    "health" : [800,1440,2592],
    "defense" : [40,40,40],
    "sp_defense" : [40,40,40],
    "attack" : [50,75,113],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [20,20,20],
    "power" : [80,80,80]
}
hero30 = Hero(name="Hero30",cost=3,attributes=hero_attributes_30,skill_type=1,rate=4.49)
hero30.add_synergy(synergy11)
hero30.add_synergy(synergy26)


hero_attributes_31 = {
    "health" : [750,1350,2430],
    "defense" : [50,50,50],
    "sp_defense" : [50,50,50],
    "attack" : [65,98,146],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [30,30,30],
    "power" : [90,90,90]
}
hero31 = Hero(name="Hero31",cost=3,attributes=hero_attributes_31,skill_type=1,rate=4.50)
hero31.add_synergy(synergy1)
hero31.add_synergy(synergy19)

hero_attributes_32 = {
    "health" : [700,1260,2268],
    "defense" : [25,25,25],
    "sp_defense" : [25,25,25],
    "attack" : [60,90,135],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [30,30,30],
    "power" : [80,80,80]
}
hero32 = Hero(name="Hero32",cost=3,attributes=hero_attributes_32,skill_type=3,rate=4.64)
hero32.add_synergy(synergy5)
hero32.add_synergy(synergy22)

hero_attributes_33 = {
    "health" : [700,1260,2268],
    "defense" : [30,30,30],
    "sp_defense" : [30,30,30],
    "attack" : [40,60,90],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [0,0,0],
    "power" : [60,60,60]
}
hero33 = Hero(name="Hero33",cost=3,attributes=hero_attributes_33,skill_type=1,rate=4.36)
hero33.add_synergy(synergy8)
hero33.add_synergy(synergy21)

hero_attributes_34 = {
    "health" : [800,1440,2592],
    "defense" : [40,40,40],
    "sp_defense" : [40,40,40],
    "attack" : [50,75,113],
    "attack_speed" : [0.8,0.8,0.8],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [0,0,0],
    "power" : [45,45,45]
}
hero34 = Hero(name="Hero34",cost=3,attributes=hero_attributes_34,skill_type=1,rate=4.55)
hero34.add_synergy(synergy15)
hero34.add_synergy(synergy21)
hero34.add_synergy(synergy26)

hero_attributes_35 = {
    "health" : [800,1440,2592],
    "defense" : [45,45,45],
    "sp_defense" : [45,45,45],
    "attack" : [60,90,135],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [50,50,50],
    "power" : [70,70,70]
}
hero35 = Hero(name="Hero35",cost=3,attributes=hero_attributes_35,skill_type=1,rate=4.55)
hero35.add_synergy(synergy3)
hero35.add_synergy(synergy16)

hero_attributes_36 = {
    "health" : [650,1170,2106],
    "defense" : [25,25,25],
    "sp_defense" : [25,25,25],
    "attack" : [50,75,113],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [10,10,10],
    "power" : [60,60,60]
}
hero36 = Hero(name="Hero36",cost=3,attributes=hero_attributes_36,skill_type=1,rate=4.42)
hero36.add_synergy(synergy10)
hero36.add_synergy(synergy25)
hero36.add_synergy(synergy28)

hero_attributes_37 = {
    "health" : [950,1710,3078],
    "defense" : [35,35,35],
    "sp_defense" : [35,35,35],
    "attack" : [80,120,180],
    "attack_speed" : [0.5,0.5,0.5],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [80,80,80],
    "power" : [140,140,140]
}
hero37 = Hero(name="Hero37",cost=3,attributes=hero_attributes_37,skill_type=3,rate=4.56)
hero37.add_synergy(synergy6)
hero37.add_synergy(synergy16)

hero_attributes_38 = {
    "health" : [800,1440,2592],
    "defense" : [45,45,45],
    "sp_defense" : [45,45,45],
    "attack" : [50,75,113],
    "attack_speed" : [0.65,0.65,0.65],
    "ct" : [0.25,0.25,0.25],
    "distance" : [2,2,2],
    "pre_power" : [50,50,50],
    "power" : [120,120,120]
}
hero38 = Hero(name="Hero38",cost=3,attributes=hero_attributes_38,skill_type=3,rate=4.63)
hero38.add_synergy(synergy12)
hero38.add_synergy(synergy19)
hero38.add_synergy(synergy17)

hero_attributes_39 = {
    "health" : [700,1260,2268],
    "defense" : [25,25,25],
    "sp_defense" : [25,25,25],
    "attack" : [60,90,135],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [30,30,30],
    "power" : [90,90,90]
}
hero39 = Hero(name="Hero39",cost=3,attributes=hero_attributes_39,skill_type=1,rate=4.34)
hero39.add_synergy(synergy12)
hero39.add_synergy(synergy27)
hero39.add_synergy(synergy20)

hero_attributes_40 = {
    "health" : [1000,1800,3240],
    "defense" : [60,60,60],
    "sp_defense" : [60,60,60],
    "attack" : [60,90,135],
    "attack_speed" : [0.65,0.65,0.65],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [100,100,100],
    "power" : [180,180,180]
}
hero40 = Hero(name="Hero40",cost=4,attributes=hero_attributes_40,skill_type=1,rate=4.35)
hero40.add_synergy(synergy7)
hero40.add_synergy(synergy22)

hero_attributes_41 = {
    "health" : [1000,1800,3240],
    "defense" : [50,50,50],
    "sp_defense" : [50,50,50],
    "attack" : [60,90,135],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [70,70,70],
    "power" : [150,150,150]
}
hero41 = Hero(name="Hero41",cost=4,attributes=hero_attributes_41,skill_type=2,rate=4.60)
hero41.add_synergy(synergy11)
hero41.add_synergy(synergy16)

hero_attributes_42 = {
    "health" : [1000,1800,3240],
    "defense" : [60,60,60],
    "sp_defense" : [60,60,60],
    "attack" : [60,90,135],
    "attack_speed" : [0.6,0.6,0.6],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [90,90,90],
    "power" : [170,170,170]
}
hero42 = Hero(name="Hero42",cost=4,attributes=hero_attributes_42,skill_type=3,rate=4.36)
hero42.add_synergy(synergy6)
hero42.add_synergy(synergy20)

hero_attributes_43 = {
    "health" : [1100,1980,3564],
    "defense" : [60,60,60],
    "sp_defense" : [60,60,60],
    "attack" : [60,90,135],
    "attack_speed" : [0.6,0.6,0.6],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [60,60,60],
    "power" : [120,120,120]
}
hero43 = Hero(name="Hero43",cost=4,attributes=hero_attributes_43,skill_type=2,rate=4.52)
hero43.add_synergy(synergy1)
hero43.add_synergy(synergy24)

hero_attributes_44 = {
    "health" : [850,1530,2754],
    "defense" : [35,35,35],
    "sp_defense" : [35,35,35],
    "attack" : [45,68,101],
    "attack_speed" : [0.8,0.8,0.8],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [60,60,60],
    "power" : [120,120,120]
}
hero44 = Hero(name="Hero40",cost=4,attributes=hero_attributes_44,skill_type=1,rate=4.42)
hero44.add_synergy(synergy7)
hero44.add_synergy(synergy26)

hero_attributes_45 = {
    "health" : [750,1350,2430],
    "defense" : [30,30,30],
    "sp_defense" : [30,30,30],
    "attack" : [30,45,68],
    "attack_speed" : [0.8,0.8,0.8],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [40,40,40],
    "power" : [50,50,50]
}
hero45 = Hero(name="Hero45",cost=4,attributes=hero_attributes_45,skill_type=1,rate=4.55)
hero45.add_synergy(synergy12)
hero45.add_synergy(synergy23)

hero_attributes_46 = {
    "health" : [750,1350,2430],
    "defense" : [25,25,25],
    "sp_defense" : [25,25,25],
    "attack" : [65,98,146],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [50,50,50],
    "power" : [100,100,100]
}
hero46 = Hero(name="Hero46",cost=4,attributes=hero_attributes_46,skill_type=1,rate=4.43)
hero46.add_synergy(synergy6)
hero46.add_synergy(synergy18)
hero46.add_synergy(synergy16)

hero_attributes_47 = {
    "health" : [850,1530,2754],
    "defense" : [45,45,45],
    "sp_defense" : [45,45,45],
    "attack" : [75,113,169],
    "attack_speed" : [0.9,0.9,0.9],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [70,70,70],
    "power" : [160,160,160]
}
hero47 = Hero(name="Hero47",cost=4,attributes=hero_attributes_47,skill_type=1,rate=4.29)
hero47.add_synergy(synergy10)
hero47.add_synergy(synergy21)

hero_attributes_48 = {
    "health" : [1000,1800,3240],
    "defense" : [50,50,50],
    "sp_defense" : [50,50,50],
    "attack" : [70,105,158],
    "attack_speed" : [0.55,0.55,0.55],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [30,30,30],
    "power" : [80,80,80]
}
hero48 = Hero(name="Hero48",cost=4,attributes=hero_attributes_48,skill_type=1,rate=4.30)
hero48.add_synergy(synergy5)
hero48.add_synergy(synergy27)

hero_attributes_49 = {
    "health" : [950,1710,3078],
    "defense" : [45,45,45],
    "sp_defense" : [45,45,45],
    "attack" : [75,113,169],
    "attack_speed" : [0.8,0.8,0.8],
    "ct" : [0.25,0.25,0.25],
    "distance" : [2,2,2],
    "pre_power" : [20,20,20],
    "power" : [60,60,60]
}
hero49 = Hero(name="Hero49",cost=4,attributes=hero_attributes_49,skill_type=1,rate=4.41)
hero49.add_synergy(synergy11)
hero49.add_synergy(synergy19)

hero_attributes_50 = {
    "health" : [750,1350,2430],
    "defense" : [30,30,30],
    "sp_defense" : [30,30,30],
    "attack" : [45,68,101],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [0,0,0],
    "power" : [50,50,50]
}
hero50 = Hero(name="Hero50",cost=4,attributes=hero_attributes_50,skill_type=3,rate=4.20)
hero50.add_synergy(synergy5)
hero50.add_synergy(synergy17)

hero_attributes_51 = {
    "health" : [750,1350,2430],
    "defense" : [25,25,25],
    "sp_defense" : [25,25,25],
    "attack" : [65,98,146],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [20,20,20],
    "power" : [100,100,100]
}
hero51 = Hero(name="Hero51",cost=4,attributes=hero_attributes_51,skill_type=1,rate=4.34)
hero51.add_synergy(synergy3)
hero51.add_synergy(synergy28)

hero_attributes_52 = {
    "health" : [1111,2000,3600],
    "defense" : [30,30,30],
    "sp_defense" : [30,30,30],
    "attack" : [50,75,113],
    "attack_speed" : [0.85,0.85,0.85],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [0,0,0],
    "power" : [0,0,0]
}
hero52 = Hero(name="Hero52",cost=4,attributes=hero_attributes_52,skill_type=3,rate=4.15)
hero52.add_synergy(synergy15)
hero52.add_synergy(synergy18)
hero52.add_synergy(synergy16)

hero_attributes_53 = {
    "health" : [900,1620,2916],
    "defense" : [65,65,65],
    "sp_defense" : [65,65,65],
    "attack" : [70,105,158],
    "attack_speed" : [0.6,0.6,0.6],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [70,70,70],
    "power" : [160,160,160]
}
hero53 = Hero(name="Hero53",cost=5,attributes=hero_attributes_53,skill_type=1,rate=4.04)
hero53.add_synergy(synergy4)
hero53.add_synergy(synergy21)

hero_attributes_54 = {
    "health" : [750,1350,2430],
    "defense" : [30,30,30],
    "sp_defense" : [30,30,30],
    "attack" : [40,60,90],
    "attack_speed" : [0.75,0.75,0.75],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [80,80,80],
    "power" : [140,140,140]
}
hero54 = Hero(name="Hero54",cost=5,attributes=hero_attributes_54,skill_type=1,rate=4.23)
hero54.add_synergy(synergy11)
hero54.add_synergy(synergy20)
hero54.add_synergy(synergy28)

hero_attributes_55 = {
    "health" : [850,1530,2754],
    "defense" : [40,40,40],
    "sp_defense" : [40,40,40],
    "attack" : [50,75,113],
    "attack_speed" : [0.85,0.85,0.85],
    "ct" : [0.25,0.25,0.25],
    "distance" : [4,4,4],
    "pre_power" : [0,0,0],
    "power" : [50,50,50]
}
hero55 = Hero(name="Hero55",cost=5,attributes=hero_attributes_55,skill_type=1,rate=3.84)
hero55.add_synergy(synergy8)
hero55.add_synergy(synergy22)

hero_attributes_56 = {
    "health" : [1100,1980,3564],
    "defense" : [50,50,50],
    "sp_defense" : [50,50,50],
    "attack" : [80,120,180],
    "attack_speed" : [0.85,0.85,0.85],
    "ct" : [0.25,0.25,0.25],
    "distance" : [2,2,2],
    "pre_power" : [20,20,20],
    "power" : [70,70,70]
}
hero56 = Hero(name="Hero56",cost=5,attributes=hero_attributes_56,skill_type=1,rate=4.16)
hero56.add_synergy(synergy12)
hero56.add_synergy(synergy19)
hero56.add_synergy(synergy29)

hero_attributes_57 = {
    "health" : [900,1620,2916],
    "defense" : [70,70,70],
    "sp_defense" : [70,70,70],
    "attack" : [80,120,180],
    "attack_speed" : [0.8,0.8,0.8],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [0,0,0],
    "power" : [50,50,50]
}
hero57 = Hero(name="Hero57",cost=5,attributes=hero_attributes_57,skill_type=1,rate=3.80)
hero57.add_synergy(synergy2)
hero57.add_synergy(synergy23)

hero_attributes_58 = {
    "health" : [1000,1800,3240],
    "defense" : [30,30,30],
    "sp_defense" : [30,30,30],
    "attack" : [80,120,180],
    "attack_speed" : [0.85,0.85,0.85],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [90,90,90],
    "power" : [180,180,180]
}
hero58 = Hero(name="Hero58",cost=5,attributes=hero_attributes_58,skill_type=1,rate=3.95)
hero58.add_synergy(synergy9)
hero58.add_synergy(synergy24)

hero_attributes_59 = {
    "health" : [1000,1800,3240],
    "defense" : [50,50,50],
    "sp_defense" : [50,50,50],
    "attack" : [60,90,135],
    "attack_speed" : [0.7,0.7,0.7],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [0,0,0],
    "power" : [70,70,70]
}
hero59 = Hero(name="Hero59",cost=5,attributes=hero_attributes_59,skill_type=3,rate=4.25)
hero59.add_synergy(synergy15)
hero59.add_synergy(synergy17)

hero_attributes_60 = {
    "health" : [1200,2160,3888],
    "defense" : [65,65,65],
    "sp_defense" : [65,65,65],
    "attack" : [70,105,158],
    "attack_speed" : [0.8,0.8,0.8],
    "ct" : [0.25,0.25,0.25],
    "distance" : [1,1,1],
    "pre_power" : [70,70,70],
    "power" : [150,150,150]
}
hero60 = Hero(name="Hero60",cost=5,attributes=hero_attributes_60,skill_type=1,rate=4.00)
hero60.add_synergy(synergy14)
hero60.add_synergy(synergy27)