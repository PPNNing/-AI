import battle_array
from battle_array import *
import pyautogui
import pygetwindow as gw

def capture_full_screen(filename="C:/Users/gyp/Desktop/project/pythorch_env/temp_screenshot.png"):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return screenshot

def capture_specific_window(title, filename="C:/Users/gyp/Desktop/project/pythorch_env/temp_screenshot.png"):
    # 获取窗口信息
    window = gw.getWindowsWithTitle(title)
    if not window:
        print(f"No window with title {title} found!")
        return None
    
    window = window[0]  # 获取第一个匹配的窗口
    
    # 使用pyautogui捕获指定的窗口区域
    screenshot = pyautogui.screenshot(region=(
        window.left, window.top, window.width, window.height))
    
    screenshot.save(filename)
    return screenshot

class teams:
    def __init__(self):
        self.core_teams = [] #用5个列表记录5个阵容并将每个阵容的综合排名记录依次在下面的列表中
        self.flex_teams = []
        self.teams_rate = []

    def find_best_match(self,now_team):#比较已有队伍与上面那五个阵容的匹配率存入下面这个列表并取其中最大值对应的阵容返回
        matching_rate = []
        max = 0
        return self.core_teams[max],self.flex_teams[max]
    
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
