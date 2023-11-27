import statistics
from statistics import *

class array:
    def __init__(self,rate):
        self.core_hero = []
        self.flex_hero = []
        self.rate = rate
        self.hero_weapon_recommendations = {}
        self.weapon_recommendations = []
    def add_core_hero(self,heroes):
        for hero in heroes:
            if hero not in self.core_hero:
                self.core_hero.append(hero)

    def add_flex_hero(self,heroes):
        for hero in heroes:
            if hero not in self.flex_hero:
                self.flex_hero.append(hero)
    
    def recommend_weapon_for_hero(self,hero,weapons):
        self.hero_weapon_recommendations[hero] = weapons

    def get_weapon_recommendation(self,hero):
        return self.hero_weapon_recommendations.get(hero,None)
    
    def weapon_recommend(self,weapons):
        self.weapon_recommendations = weapons



level = [2,2,6,10,20,36,56,80,100]

class control:
    def __init__(self):
        self.coin = 2
        self.core_hero = []
        self.flex_hero = []
        self.current = []
        self.coin_value = 110.0 
        self.level = 1

    def renew_coin(self,coin):
        self.coin = coin

    def renew_coin_value(self,value):
        self.coin_value = value

    def add_buyed_hero(self,buy):
        self.current = self.current.append(buy)

    def add_team(self,core,flex):
        self.core_hero = self.core_hero.append(core)
        self.flex_hero = self.flex_hero.append(flex)

    def upgrade(self):
        if self.coin > level[self.level - 1]:
            if 7 <=self.level <= 9:
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
                
    def cal_three_value(self,hero):
        total_value = hero.each_value
        for i in self.core_hero:
            if i == hero:
                total_value = total_value + 200
        for i in self.flex_hero:
            if i == hero:
                total_value = total_value + 100
        for i in self.current:
            if i == hero:
                total_value = total_value + 50
            for t in i.synergies:
                if t in hero.synergies:
                    total_value = total_value + (t.rate[0] * t.rate[0] -12) * 10
        return total_value
        

    def sort_best(self,shop):
        choice = [0,0,0,0,0]
        tap = 0
        for i in shop:
            if self.cal_three_value(i) >= self.coin_value:
                choice[tap] = self.cal_three_value(i)
            tap = tap + 1

array1 = array(3.54) # K/DA 厄运小姐&妮寇
array1.add_core_hero([hero4,hero12,hero25,hero21,hero34,hero28,hero36])
array1.add_flex_hero([hero58])
array1.recommend_weapon_for_hero(hero25,[h_weapon17])
array1.recommend_weapon_for_hero(hero21,[h_weapon38])
array1.recommend_weapon_for_hero(hero34,[h_weapon23,h_weapon26])
array1.recommend_weapon_for_hero(hero28,[h_weapon7,h_weapon12,h_weapon20])
array1.recommend_weapon_for_hero(hero36,[h_weapon38,h_weapon26,h_weapon23])
array1.weapon_recommend([l_weapon5,l_weapon7,l_weapon6,l_weapon3,l_weapon2,l_weapon4])

array2 = array(3.43) # K/DA 巴德&妮寇
array2.add_core_hero([hero4,hero12,hero25,hero34,hero36])
array2.add_flex_hero([hero21,hero28,hero55])
array2.recommend_weapon_for_hero(hero25,[h_weapon17,h_weapon4,h_weapon14])
array2.recommend_weapon_for_hero(hero34,[h_weapon23,h_weapon26])
array2.recommend_weapon_for_hero(hero36,[h_weapon38,h_weapon23,h_weapon26])
array2.recommend_weapon_for_hero(hero21,[h_weapon38])
array2.recommend_weapon_for_hero(hero28,[h_weapon7])
array2.weapon_recommend([l_weapon5,l_weapon7,l_weapon6,l_weapon9,l_weapon2,l_weapon3])

array3 = array(3.88) # 乡村乐 沙弥啦&厄加特
array3.add_core_hero({hero9,hero29,hero35,hero27,hero37,hero51})
array3.add_flex_hero([hero39,hero60])
array3.recommend_weapon_for_hero(hero29,[h_weapon21,h_weapon19])
array3.recommend_weapon_for_hero(hero35,[h_weapon6,h_weapon12,h_weapon2])
array3.recommend_weapon_for_hero(hero27,[h_weapon9,h_weapon2,h_weapon5])
array3.recommend_weapon_for_hero(hero37,[h_weapon28])
array3.recommend_weapon_for_hero(hero39,[h_weapon19])
array3.weapon_recommend([l_weapon7,l_weapon5,l_weapon9,l_weapon2,l_weapon1,l_weapon4])

array4 = array(4.02) # 音浪刺客 卡特琳娜&劫
array4.add_core_hero([hero3,hero12,hero18,hero36,hero50,hero59])
array4.add_flex_hero([hero4,hero38])
array4.recommend_weapon_for_hero(hero18,[h_weapon17,h_weapon13,h_weapon14])
array4.recommend_weapon_for_hero(hero36,[h_weapon26,h_weapon19])
array4.recommend_weapon_for_hero(hero50,[h_weapon5,h_weapon30,h_weapon20])
array4.recommend_weapon_for_hero(hero59,[h_weapon20])
array4.recommend_weapon_for_hero(hero38,[h_weapon5])
array4.weapon_recommend([l_weapon1,l_weapon9,l_weapon7,l_weapon5,l_weapon6,l_weapon4])

array5 = array(4.18) # K/DA 阿狸&阿卡丽
array5.add_core_hero([hero12,hero22,hero34,hero36,hero47,hero46])
array5.add_flex_hero([hero4,hero21])
array5.recommend_weapon_for_hero(hero22,[h_weapon4])
array5.recommend_weapon_for_hero(hero34,[h_weapon23])
array5.recommend_weapon_for_hero(hero36,[h_weapon23,h_weapon26])
array5.recommend_weapon_for_hero(hero47,[h_weapon18,h_weapon4,h_weapon3])
array5.recommend_weapon_for_hero(hero46,[h_weapon20,h_weapon9,h_weapon5])
array5.weapon_recommend([l_weapon4,l_weapon5,l_weapon7,l_weapon6,l_weapon1,l_weapon2])

array6 = array(4.19) # 护卫 金克丝&潘森
array6.add_core_hero([hero8,hero10,hero19,hero17,hero29])
array6.add_flex_hero([hero36,hero37,hero51])
array6.recommend_weapon_for_hero(hero8,[h_weapon12,h_weapon7,h_weapon2])
array6.recommend_weapon_for_hero(hero19,[h_weapon21,h_weapon24,h_weapon26])
array6.recommend_weapon_for_hero(hero17,[h_weapon2,h_weapon12])
array6.recommend_weapon_for_hero(hero29,[h_weapon41])
array6.recommend_weapon_for_hero(hero51,[h_weapon41])
array6.weapon_recommend([l_weapon9,l_weapon2,l_weapon5,l_weapon6,l_weapon7,l_weapon8])




