import tkinter as tk # 导入tkinter模块
import PIL # 导入PIL模块
from PIL import ImageTk, Image # 导入ImageTk模块


def quit_app(window):
    window.destroy()


def show_images(cards, upgrade=False, buy=0, options=None, recommended_positions = None, recommended_heroes=None,window=None, path=r"C:\Users\王坤明\Desktop\card\%d.png") :
    # 创建2个tkinter窗口对象，一个展示推荐阵容和可选决策，一个展示推荐站位
    window = tk.Tk()
    # 设置窗口的标题
    window.title("显示第一行图片")
    # 窗口大小
    width = 600
    height = 550
    window.geometry("%dx%d" % (width, height))
    # 窗口的背景颜色为白色
    window.configure(bg="white")  # 使用configure(bg='')方法git add gui.py

    # 创建一个画布对象
    canvas = tk.Canvas(window, width=800, height=600, bg="white")  # 直接设置bg属性为白色
    # 将画布对象放在窗口上
    canvas.pack()

    # 第一个板块的label：推荐阵容
    label1 = tk.Label(window, text="推荐阵容", font=("Arial", 10), bg="white")
    # 设置label1的位置
    label1.place(x=width / 2, y=15, anchor=tk.CENTER)

    # 计算第一行图片的站位坐标
    x1 = width / 16
    y = x1 * 1.7
    x2 = x1 * 3
    x3 = x1 * 5
    x4 = x1 * 7
    x5 = x1 * 9
    x6 = x1 * 11
    x7 = x1 * 13
    x8 = x1 * 15
    # 定义一个列表，存储第一行图片的站位坐标
    positions = [(x1, y), (x2, y), (x3, y), (x4, y), (x5, y), (x6, y), (x7, y), (x8, y)]

    # 定义一个全局变量，存储所有的图片对象
    images = []

    # 计算每个图片的宽度，使得所有图片能在一行中完整显示且不重叠
    image_width = int(width / 8)
    image_height = int(image_width)

    # 遍历第一行图片的序号
    for i in range(len(cards)):
        # 获取站位的坐标
        x, y = positions[i]
        # 获取第一行的图片序号和图片对象
        img = PIL.Image.open(path % cards[i])
        img = img.resize((image_width, image_height))  # 调整图片的大小
        # 在画布上创建一个图片对象，并绑定鼠标移动事件
        image = ImageTk.PhotoImage(img)  # 创建一个ImageTk.PhotoImage对象
        image_name = "card%d" % i  # 给图片对象一个唯一的名字
        canvas.create_image(x, y, image=image, anchor=tk.CENTER, tags=image_name)
        canvas.tag_bind(image_name, "<Enter>")
        # 将图片对象添加到全局变量中，防止被内存回收
        images.append(image)

    # 在每张图片下面设置一个label显示英雄发育进度，初始值为0，还有一个减号button，点击后英雄发育进度减1
    # 计算label的位置
    label_x = width / 16-20
    label_y = y + image_height / 2 + 20
    # 计算button的位置
    button_x = width / 16 + 20
    button_y = y + image_height / 2 + 20
    # 定义一个列表，存储所有的label和button
    labels = []
    buttons = []
    # 遍历第一行图片的序号

    for i in range(len(cards)):
        # 创建一个label，显示英雄发育进度
        label = tk.Label(window, text="0", font=("Arial", 10), bg="white")
        # 设置label的位置
        label.place(x=label_x, y=label_y, anchor=tk.CENTER)
        # 创建一个button，点击后英雄发育进度减1
        button = tk.Button(window, text="-", font=("Arial", 10), bg="white")
        # 设置button的大小
        button["width"] = 1
        button["height"] = 1
        # 设置button的位置
        button.place(x=button_x, y=button_y, anchor=tk.CENTER)
        # 将label和button添加到对应的列表中
        labels.append(label)
        buttons.append(button)
        # 更新label和button的位置
        label_x += width / 8
        button_x += width / 8

    # 第二个板块的label：一行可选角色options的图片以及一个升级label，当可选时label和图片的边框变为红色，不可选时变为白色
    label2 =tk.Label(window, text="upgrade", font=("Arial", 10), bg="white")
    # 设置label2的位置
    label2.place(x=width / 2, y=height / 2 + 100, anchor=tk.CENTER)


    if upgrade == True:
        label2["borderwidth"] = 1
        label2["relief"] = "solid"
        label2["bg"] = "red"
        label2["fg"] = "black"
    else:
        label2["borderwidth"] = 1
        label2["relief"] = "solid"
        label2["bg"] = "white"
        label2["fg"] = "black"

    # 设置label2的大小
    label2["width"] = 10
    label2["height"] = 2


    # 计算第二行图片的站位坐标
    x1 = width / 10
    y = height / 2 - 50
    x2 = x1 * 3
    x3 = x1 * 5
    x4 = x1 * 7
    x5 = x1 * 9
    # 定义一个列表，存储第二行图片的站位坐标
    positions2 = [(x1, y), (x2, y), (x3, y), (x4, y), (x5, y)]

    # 图片的宽度和高度
    image_width2 = int(width / 6)
    image_height2 = int(image_width2)

    # 定义一个全局变量，存储所有的图片对象
    images2 = []

    # 遍历第二行图片的序号

    for i in range(len(options)):
        # 获取站位的坐标
        x, y = positions2[i]
        # 获取第二行的图片序号和图片对象
        img = PIL.Image.open(path % options[i])
        img = img.resize((image_width2, image_height2))
        # 在画布上创建一个图片对象，并绑定鼠标移动事件
        image = ImageTk.PhotoImage(img)
        image_name = "card%d" % i
        canvas.create_image(x, y, image=image, anchor=tk.CENTER, tags=image_name)
        canvas.tag_bind(image_name, "<Enter>")
        # 将图片对象添加到全局变量中，防止被内存回收
        images2.append(image)

    # 计算label3的位置
    if buy!=0:
        label3_x = width / 10 * (2 * buy - 1)
        label3_y = height / 2 + 20
        # 创建一个label3，显示"recommend"
        label3 = tk.Label(window, text="recommend", font=("Arial", 10), bg="red")
        # 设置label3的位置
        label3.place(x=label3_x, y=label3_y, anchor=tk.CENTER)



    # 放置一个button，点击后退出程序
    button = tk.Button(window, text="退出", font=("Arial", 10), bg="white")
    # 设置button的大小
    button["width"] = 10
    button["height"] = 2
    # 设置button的位置
    button.place(x=width / 2, y=height - 50, anchor=tk.CENTER)
    # 绑定button的点击事件
    button["command"] = lambda: quit_app(window)


    # 显示推荐站位，在4x7的网格中显示
    def show_recommended_positions(cards, recommended_positions, window):
        # 创建一个新的窗口
        new_window = tk.Toplevel(window)
        new_window.title("推荐站位")
        # 窗口大小
        width = 600
        height = 550
        new_window.geometry("%dx%d" % (width, height))
        # 窗口的背景颜色为白色
        new_window.configure(bg="white")

        # 创建一个4x7的网格
        for i in range(4):
            for j in range(7):
                tk.Label(new_window, text=" ", width=11, height=7, bg="white", borderwidth=1, relief="solid").grid(
                    row=i, column=j)

        # 根据recommended_positions和recommended_heroes在网格中显示英雄的图片
        for i in range(len(recommended_positions)):
            position = recommended_positions[i]
            hero = recommended_heroes[i]
            img = PIL.Image.open(path % hero)
            img = img.resize((70, 80))  # 调整图片的大小
            image = ImageTk.PhotoImage(img)  # 创建一个ImageTk.PhotoImage对象
            label = tk.Label(new_window, image=image)
            label.image = image  # keep a reference to the image
            label.grid(row=position[0], column=position[1])

        new_window.mainloop()

    show_recommended_positions(cards, recommended_positions, window)
    # 设计另一个窗口，用来显示推荐站位

    # 进入tkinter的主循环
    return window

"""
#测试
cards = [1, 2, 3, 4, 5, 6, 7, 8]
recommended_positions = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),(0, 5),(0, 6),(1,1)]
recommended_heroes = [1, 2, 3, 4, 5, 6, 7, 8]
options = [1, 2, 3, 4, 5]

show_images(cards,True,1,options,recommended_positions,recommended_heroes).mainloop()
"""

