import tkinter as tk  # 导入tkinter模块
import PIL  # 导入PIL模块
from PIL import ImageTk, Image  # 导入ImageTk模块
import statistics
import pyautogui
import pygetwindow as gw
import screenshot
import pyscreenshot
import card
import re
import number


con = statistics.control()


def show_images(path=r"C:\Users\王坤明\Desktop\card\%d.png",now = None):
    """now是第一次执行时已经购买的阵容,path是cards文件的路径"""
    # cards是一个列表展示现有角色以及星级,path为图片路径注意%d.png是图片的命名格式，
    # 截图
    image = pyscreenshot.grab()
    # 商店英雄
    x = card.card(image)
    # 金币
    y = number.get_number(image)
    # 更新金币
    con.renew_coin(y)

    if con.get_state() == 0: # 一开始执行时
        con.renew_current(now)
        con.add_target()
        con.renew_state()
    # 是否升级
    upgrade = con.upgrade()
    # 推荐决策是否选择英雄

    # 创建一个窗口对象
    window = tk.Tk()
    window.title("云顶之弈AI辅助")
    # 设置窗口的大小
    width = 400
    height = 550
    # 设置窗口的位置
    window.geometry("%dx%d+%d+%d" % (width, height, 0, 0))
    window.configure(bg="white")
    # 创建画布
    canvas = tk.Canvas(window, width=width, height=height, bg="white")
    canvas.pack()

    ##############################################################################
    # 预定义推荐装备的显示函数，用于鼠标事件
    global high_weapons
    high_weapons = []
    weapon_x1 = width / 10
    weapon_y = height / 2 + 100
    weapon_x2 = width / 10 * 3
    weapon_x3 = width / 10 * 5
    weapon_x4 = width / 10 * 7
    weapon_positions = [(weapon_x1, weapon_y), (weapon_x2, weapon_y), (weapon_x3, weapon_y), (weapon_x4, weapon_y)]
    
    def show_equips(hero_sample, path=r"C:\Users\王坤明\Desktop\l_equip\%d.png"):
        high_weapons = statistics.get_high(hero_sample)
        weapon_width = int(width / 6)
        weapon_height = int(weapon_width)
        for weapon in range(len(high_weapons)):
            weapon_x, weapon_y = weapon_positions[weapon]
            weapon_img = PIL.Image.open(path % high_weapons[weapon])
            weapon_img = weapon_img.resize((weapon_width, weapon_height))
            tk_image = ImageTk.PhotoImage(weapon_img)
            name = "weapon%d" % weapon
            canvas.create_image(weapon_x, weapon_y, image=tk_image, anchor=tk.CENTER, tags=name)
            high_weapons.append(tk_image)
    ##############################################################################
    """第一板块"""
    # 用截图函数更新现有阵容
    # 创建一个标签对象
    label1 = tk.Label(window, text="推荐阵容", font=("Arial", 10), bg="white")
    label1.place(x=width / 2, y=15, anchor=tk.CENTER)
    # 放置现有阵容8个角色图片的坐标
    x1 = width / 16
    y = x1 * 1.7
    x2 = x1 * 3
    x3 = x1 * 5
    x4 = x1 * 7
    x5 = x1 * 9
    x6 = x1 * 11
    x7 = x1 * 13
    x8 = x1 * 15
    positions = [(x1, y), (x2, y), (x3, y), (x4, y), (x5, y), (x6, y), (x7, y), (x8, y)]
    # 用于存储图片对象
    global images
    images = []
    # 设置8张图片大小
    image_width = int(width / 8)
    image_height = int(image_width)
    # 现有各角色星级以及手动操作售卖与购买按钮的坐标
    buttons_minus = []
    button_minus_x = width / 16 + 15
    button_y = y + image_height / 2 + 20

    """labels = []
    label_x = width / 16 - 10
    label_y = y + image_height / 2 + 20"""
    # 查看现有阵容
    now_team = con.get_current()  # 61个数字包括所有英雄
    global cards
    cards = []
    for i in range(len(now_team)):
        if now_team[i] != 0:
            cards.append(i+1)
    # 遍历现有阵容，放置图片以及星级标签和售卖按钮
    for i in range(len(cards)):
        x, y = positions[i]
        hero= cards[i]
        img = PIL.Image.open(path % hero)
        img = img.resize((image_width, image_height))
        image = ImageTk.PhotoImage(img)
        image_name = "card%d" % i
        canvas.create_image(x, y, image=image, anchor=tk.CENTER, tags=image_name)
        canvas.tag_bind(image_name, "<Enter>", lambda event, hero_sample=hero: show_equips(hero_sample))
        images.append(image)
        images.append(image)
        button = tk.Button(window, text="-", font=("Arial", 10), bg="white")
        button.command=con.sell_hero(cards[i])
        button["width"] = 1
        button["height"] = 1
        button.place(x=button_minus_x, y=button_y, anchor=tk.CENTER)
        button_minus_x += width / 8
        buttons_minus.append(button)
        """label = tk.Label(window, text="%d" % extent, font=("Arial", 10), bg="white")
        label.place(x=label_x, y=label_y, anchor=tk.CENTER)
        labels.append(label)
        label_x += width / 8"""



    # 一二板块间的分割线
    canvas.create_line(0, button_y + 20, width, button_y + 20, fill="black", width=3)

    """第二板块，推荐决策"""
    options = con.sort_best(x)
    for i in range(len(options)):
        if options[i] == 1:
            con.add_buyed_hero(x[i])

    x1 = int(width / 10)
    y = int(height / 2 - 50)
    x2 = x1 * 3
    x3 = x1 * 5
    x4 = x1 * 7
    x5 = x1 * 9
    positions2 = [(x1, y), (x2, y), (x3, y), (x4, y), (x5, y)]

    image_width2 = int(width / 6)
    image_height2 = int(image_width2)

    global images2
    images2 = []

    for i in range(len(options)):
        x, y = positions2[i]
        img = PIL.Image.open(path % options[i])
        img = img.resize((image_width2, image_height2))
        image = ImageTk.PhotoImage(img)
        image_name = "card%d" % i
        canvas.create_image(x, y, image=image, anchor=tk.CENTER, tags=image_name)
        canvas.tag_bind(image_name, "<Enter>")
        images2.append(image)

    for i in range(len(options)):
        if options[i] != 0:
            label3_x = width / 10 * (2 * i + 1)
            label3_y = height / 2 + 20
            label3 = tk.Label(window, text="choose", font=("Arial", 15), bg="red")
            label3.place(x=label3_x, y=label3_y, anchor=tk.CENTER)


    # upgrade图标
    label_strategy = tk.Label(window, text="推荐决策", font=("Arial", 10), bg="white")
    label_strategy.place(x=width / 2, y=button_y + 40, anchor=tk.CENTER)
    label_upgrade = tk.Label(window, text="upgrade", font=("Arial", 12), bg="white")
    label_upgrade.place(x=width / 2, y=height / 2 + 50, anchor=tk.CENTER)
    if upgrade == True:
        label_upgrade["borderwidth"] = 1
        label_upgrade["relief"] = "solid"
        label_upgrade["bg"] = "red"
        label_upgrade["fg"] = "black"
    else:
        label_upgrade["borderwidth"] = 1
        label_upgrade["relief"] = "solid"
        label_upgrade["bg"] = "white"
        label_upgrade["fg"] = "black"

    # 二三板块间的分割线
    canvas.create_line(0, height / 2 + 65, width, height / 2 + 65, fill="black", width=3)

    # 第三板块，推荐装备
    label3 = tk.Label(window, text="推荐装备", font=("Arial", 10), bg="white")
    label3.place(x=width / 2, y=height / 2 + 80, anchor=tk.CENTER)




    # 用于更新整个窗口
    button = tk.Button(window, text="更新截图", font=("Arial", 12), bg="white",
                       command=lambda: update_window(window))
    button["width"] = 10
    button["height"] = 2
    button.place(x=width / 2, y=height - 50, anchor=tk.CENTER)

    return window


def update_window(old_window):
    old_window.destroy()
    new_window = show_images()
    return new_window

"""window_gui = show_images()
window_gui.mainloop()"""
