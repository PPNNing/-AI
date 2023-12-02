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

array1 = array(5.30) # K/DA 厄运小姐&妮寇
array1.add_core_hero([hero4,hero12,hero25,hero21,hero34,hero28,hero36])
array1.add_flex_hero([hero58])
array1.recommend_weapon_for_hero(hero25,[h_weapon17])
array1.recommend_weapon_for_hero(hero21,[h_weapon38])
array1.recommend_weapon_for_hero(hero34,[h_weapon23,h_weapon26])
array1.recommend_weapon_for_hero(hero28,[h_weapon7,h_weapon12,h_weapon20])
array1.recommend_weapon_for_hero(hero36,[h_weapon38,h_weapon26,h_weapon23])
array1.weapon_recommend([l_weapon5,l_weapon7,l_weapon6,l_weapon3,l_weapon2,l_weapon4])

array2 = array(5.30) # K/DA 巴德&妮寇
array2.add_core_hero([hero4,hero12,hero25,hero34,hero36])
array2.add_flex_hero([hero21,hero28,hero55])
array2.recommend_weapon_for_hero(hero25,[h_weapon17,h_weapon4,h_weapon14])
array2.recommend_weapon_for_hero(hero34,[h_weapon23,h_weapon26])
array2.recommend_weapon_for_hero(hero36,[h_weapon38,h_weapon23,h_weapon26])
array2.recommend_weapon_for_hero(hero21,[h_weapon38])
array2.recommend_weapon_for_hero(hero28,[h_weapon7])
array2.weapon_recommend([l_weapon5,l_weapon7,l_weapon6,l_weapon9,l_weapon2,l_weapon3])

array3 = array(4.10) # 乡村乐 沙弥啦&厄加特
array3.add_core_hero({hero9,hero29,hero35,hero39,hero27,hero37,hero51})
array3.add_flex_hero([hero60])
array3.recommend_weapon_for_hero(hero29,[h_weapon19,h_weapon23,h_wapon24])
array3.recommend_weapon_for_hero(hero35,[h_weapon6,h_weapon12,h_weapon2])
array3.recommend_weapon_for_hero(hero27,[h_weapon2,h_weapon34])
array3.recommend_weapon_for_hero(hero51,[h_weapon28])
array3.recommend_weapon_for_hero(hero39,[h_weapon19])
array3.weapon_recommend([l_weapon2,l_weapon7,l_weapon9,l_weapon1,l_weapon4,l_weapon5])

array4 = array(4.30) # 音浪刺客 卡特琳娜&劫
array4.add_core_hero([hero3,hero12,hero18,hero36,hero50,hero59])
array4.add_flex_hero([hero4,hero38])
array4.recommend_weapon_for_hero(hero18,[h_weapon17,h_weapon13,h_weapon14])
array4.recommend_weapon_for_hero(hero36,[h_weapon26,h_weapon19])
array4.recommend_weapon_for_hero(hero50,[h_weapon5,h_weapon30,h_weapon20])
array4.recommend_weapon_for_hero(hero59,[h_weapon20])
array4.recommend_weapon_for_hero(hero38,[h_weapon5])
array4.weapon_recommend([l_weapon1,l_weapon9,l_weapon7,l_weapon5,l_weapon6,l_weapon4])

array5 = array(4.82) # K/DA 阿狸&阿卡丽
array5.add_core_hero([hero12,hero22,hero34,hero36,hero47,hero46])
array5.add_flex_hero([hero4,hero21])
array5.recommend_weapon_for_hero(hero22,[h_weapon4])
array5.recommend_weapon_for_hero(hero34,[h_weapon23])
array5.recommend_weapon_for_hero(hero36,[h_weapon23,h_weapon26])
array5.recommend_weapon_for_hero(hero47,[h_weapon18,h_weapon4,h_weapon3])
array5.recommend_weapon_for_hero(hero46,[h_weapon20,h_weapon9,h_weapon5])
array5.weapon_recommend([l_weapon4,l_weapon5,l_weapon7,l_weapon6,l_weapon1,l_weapon2])

array6 = array(4.77) # 护卫 金克丝&潘森
array6.add_core_hero([hero8,hero10,hero19,hero17,hero29])
array6.add_flex_hero([hero36,hero37,hero51])
array6.recommend_weapon_for_hero(hero8,[h_weapon12,h_weapon7,h_weapon2])
array6.recommend_weapon_for_hero(hero19,[h_weapon21,h_weapon24,h_weapon26])
array6.recommend_weapon_for_hero(hero17,[h_weapon2,h_weapon12])
array6.recommend_weapon_for_hero(hero29,[h_weapon41])
array6.recommend_weapon_for_hero(hero51,[h_weapon41])
array6.weapon_recommend([l_weapon9,l_weapon2,l_weapon5,l_weapon6,l_weapon7,l_weapon8])

array7 = array(4.13) # K/DA 安妮
array7.add_core_hero([hero1,hero4,hero12,hero34,hero36,hero47])
array7.add_flex_hero([hero29,hero33])
array7.recommend_weapon_for_hero(hero1,[h_weapon11,h_weapon7])
array7.recommend_weapon_for_hero(hero34,[h_weapon15,h_weapon23])
array7.recommend_weapon_for_hero(hero47,[h_waepon4,h_weapon18])
array7.recommend_weapon_for_hero(hero29,[h_weapon23])
array7.recommend_weapon_for_hero(hero33,[h_weapon18])
array7.weapon_recommend([l_weapon4,l_weapon7,l_weapon5,l_weapon2,l_weapon6,l_weapon3])

array8 = array(3.99) #K/DA 安妮&阿木木
array8.add_core_hero([hero1,hero4,hero12,hero29,hero34,hero36,hero47])
array8.add_flex_hero([hero33])
array8.recommend_weapon_for_hero(hero1,[h_weapon11,h_weapon7])
array8.recommend_weapon_for_hero(hero29,[h_weapon15,h_weapon23,h_weapon24])
array8.recommend_weapon_for_hero(hero34,[h_weapon15])
array8.recommend_weapon_for_hero(hero47,[h_weapon4,h_weapon18])
array8.weapon_recommend([l_weapon4,l_weapon6,l_weapon7,l_weapon2,l_weapon3,l_weapon5])

array9 = array(4.25) #K/DA 厄运小姐&艾克
array9.add_core_hero([hero4,hero12,hero21,hero34,hero28,hero36])
array9.add_flex_hero([hero25,hero58])
array9.recommend_weapon_for_hero(hero21,[h_weapon38])
array9.recommend_weapon_for_hero(hero34,[h_weapon25,h_weapon19,h_weapon32])
array9.recommend_weapon_for_hero(hero28,[h_weapon7,h_weapon12,h_weapon6])
array9.recommend_weapon_for_hero(hero36,[h_weapon23,h_weapon26])
array9.recommend_weapon_for_hero(hero25,[h_weapon4])
array9.weapon_recommend([l_weapon7,l_weapon5,l_weapon6,l_weapon2,l_weapon9,l_weapon8])

array10 = array(4.11) #超级粉丝 卡尔萨斯&阿卡丽
array10.add_core_hero([hero12,hero23,hero36,hero46,hero41,hero54])
array10.add_flex_hero([hero4,hero37])
array10.recommend_weapon_for_hero(hero36,[h_weapon23])
array10.recommend_weapon_for_hero(hero46,[h_weapon20,h_weapon9,h_weapon34])
array10.recommend_weapon_for_hero(hero41,[h_weapon4,h_weapon17])
array10.recommend_weapon_for_hero(hero54,[h_weapon28,h_weapon5])
array10.weapon_recommend([l_weapon9,l_weapon4,l_weapon7,l_weapon3,l_weapon1,l_weapon5])

array11 = array(4.58) #迪斯科 崔斯特&布里茨
array11.add_core_hero([hero20,hero34,hero44,hero40,hero60,hero55])
array11.add_flex_hero({hero11,hero6})
array11.recommend_weapon_for_hero(hero44,[h_weapon35,h_weapon19,h_weapon22])
array11.recommend_weapon_for_hero(hero40,[h_weapon4,h_weapon3,h_weapon17])
array11.recommend_weapon_for_hero(hero60,[h_weapon28])
array11.recommend_weapon_for_hero(hero55,[h_weapon4,h_weapon11])
array11.weapon_recommend([l_weapon4,l_weapon2,l_weapon7,l_weapon9,l_weapon1,l_weapon3])

array12 = array(4.77) #真实伤害 赛娜&艾克
array12.add_core_hero([hero4,hero12,hero24,hero34,hero36,hero52,hero59])
array12.add_flex_hero([hero7])
array12.recommend_weapon_for_hero(hero24,[h_weapon4,h_weapon7,h_weapon11])
array12.recommend_weapon_for_hero(hero34,[h_weapon19,h_weapon23,h_weapon26])
array12.recommend_weapon_for_hero(hero36,[h_weapon19])
array12.recommend_weapon_for_hero(hero52,[h_weapon5,h_weapon20])
array12.weapon_recommend([l_weapon7,l_weapon1,l_weapon6,l_weapon4,l_weapon5,l_weapon9])

array13 = array(5.01) #电子舞曲 拉克丝&扎克
array13.add_core_hero([hero20,hero16,hero32,hero48,hero50])
array13.add_flex_hero([hero11,hero40,hero55])
array13.recommend_weapon_for_hero(hero32,[h_weapon13,h_weapon14])
array13.recommend_weapon_for_hero(hero48,[h_weapon26,h_weapon24,h_weapon19])
array13.recommend_weapon_for_hero(hero50,[h_weapon5,h_weapon28])
array13.recommend_weapon_for_hero(hero40,[h_weapon8])
array13.weapon_recommend([l_weapon6,l_weapon2,l_weapon3,l_weapon4,l_weapon7,l_weapon1])

array14 = array(4.92) #护卫 薇古丝&阿木木
array14.add_core_hero([hero4,hero12,hero29,hero36,hero37,hero46,hero51])
array14.add_flex_hero([hero42])
array14.recommend_weapon_for_hero(hero29,[h_weapon23,h_weapon26,h_weapon28])
array14.recommend_weapon_for_hero(hero37,[h_weapon17,h_weapon14,h_weapon4])
array14.recommend_weapon_for_hero(hero46,[h_weapon28,h_weapon20])
array14.weapon_recommend([l_weapon9,l_weapon4,l_weapon1,l_weapon5,l_weapon3,l_weapon7])

array15 = array(5.16) #舞者 厄加特&波比
array15.add_core_hero([hero14,hero39,hero27,hero42])
array15.add_flex_hero([hero35,hero41,hero51,hero54])
array15.recommend_weapon_for_hero(hero39,[h_weapon23,h_weapon22])
array15.recommend_weapon_for_hero(hero27,[h_weapon28,h_weapon6,h_weapon34])
array15.recommend_weapon_for_hero(hero35,[h_weapon6])
array15.recommend_weapon_for_hero(hero51,[h_weapon19])
array15.recommend_weapon_for_hero(hero54,[h_weapon5])
array15.weapon_recommend([l_weapon2,l_weapon9,l_weapon1,l_weapon5,l_weapon6,l_weapon4])


