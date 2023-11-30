import tkinter as tk # 导入tkinter模块
import PIL # 导入PIL模块
from PIL import ImageTk, Image # 导入ImageTk模块

def show_images(cards, recommended_positions):
    # 创建一个tkinter窗口对象
    window = tk.Tk()
    # 设置窗口的标题
    window.title("显示第一行图片")
    # 设置窗口的大小
    window.geometry("800x600")
    # 设置窗口的背景颜色为白色
    window.configure(bg="white") # 使用configure(bg='')方法git add gui.py

    # 创建一个画布对象
    canvas = tk.Canvas(window, width=800, height=600, bg="white") # 直接设置bg属性为白色
    # 将画布对象放在窗口上
    canvas.pack()

    # 定义一个列表，存储第一行图片的站位坐标
    positions = [(80, 100), (240, 100), (400, 100), (560, 100), (720, 100)]

    # 定义一个全局变量，存储所有的图片对象
    images = []

    # 计算每个图片的宽度，使得所有图片能在一行中完整显示且不重叠
    image_width = 800 // len(cards) # 800是窗口的宽度
    image_height = 600 // 4 # 假设图片的高度为窗口高度的一半

    # 遍历第一行图片的序号
    for i in range(len(cards)):
        # 获取站位的坐标
        x, y = positions[i]
        # 获取第一行的图片序号和图片对象
        img = PIL.Image.open(r"C:\Users\王坤明\Desktop\card\%d.png" % cards[i])
        img = img.resize((image_width, image_height)) # 调整图片的大小
        # 在画布上创建一个图片对象，并绑定鼠标移动事件
        image = ImageTk.PhotoImage(img) # 创建一个ImageTk.PhotoImage对象
        image_name = "card%d" % i # 给图片对象一个唯一的名字
        canvas.create_image(x, y, image=image, anchor=tk.CENTER, tags=image_name)
        canvas.tag_bind(image_name, "<Enter>")
        # 将图片对象添加到全局变量中，防止被内存回收
        images.append(image)

    # 创建一个4x7的棋盘
    board = [[None for _ in range(7)] for _ in range(4)]
    # 计算棋盘上每个格子的大小
    cell_width = 800 // 7
    cell_height = (600 - image_height) // 4

    # 根据推荐站位的二元坐标在棋盘上显示对应的图片
    for i, (x, y) in enumerate(recommended_positions):
        # 获取图片对象
        img = PIL.Image.open(r"C:\Users\王坤明\Desktop\card\%d.png" % cards[i])
        img = img.resize((cell_width, cell_height)) # 调整图片的大小
        # 在画布上创建一个图片对象，并绑定鼠标移动事件
        image = ImageTk.PhotoImage(img) # 创建一个ImageTk.PhotoImage对象
        image_name = "board%d" % i # 给图片对象一个唯一的名字
        canvas.create_image(x * cell_width + cell_width // 2, y * cell_height + cell_height // 2 + image_height, image=image, anchor=tk.CENTER, tags=image_name)
        canvas.tag_bind(image_name, "<Enter>")
        # 将图片对象添加到全局变量中，防止被内存回收
        images.append(image)

    # 进入tkinter的主循环
    window.mainloop()

"""
这里是测试样例
cards = [1, 2, 3, 4, 5]
recommended_positions = [(0, 0), (0, 1), (0, 2), (0, 3)]
show_images(cards, recommended_positions)
"""
