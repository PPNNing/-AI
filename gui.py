import tkinter as tk # 导入tkinter模块
import PIL # 导入PIL模块
from PIL import ImageTk, Image # 导入ImageTk模块


def quit_app(window):
    window.destroy()


def show_images(cards, upgrade=False, buy=0, sell=0, options=None, window=None, path=r"C:\Users\王坤明\Desktop\card\%d.png"):
    #第一板块，推荐阵容
    # 创建一个窗口对象
    window = tk.Tk()
    window.title("云顶之弈AI辅助")
    # 设置窗口的大小
    width = 600
    height = 550
    # 设置窗口的位置
    window.geometry("%dx%d+%d+%d" % (width, height, 0, 0))
    window.configure(bg="white")

    canvas = tk.Canvas(window, width=800, height=600, bg="white")
    canvas.pack()
    # 创建一个标签对象
    label1 = tk.Label(window, text="推荐阵容", font=("Arial", 10), bg="white")
    label1.place(x=width / 2, y=15, anchor=tk.CENTER)

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

    global images
    images = []


    image_width = int(width / 8)
    image_height = int(image_width)

    for i in range(len(cards)):
        x, y = positions[i]
        img = PIL.Image.open(path % cards[i])
        img = img.resize((image_width, image_height))
        image = ImageTk.PhotoImage(img)
        image_name = "card%d" % i
        canvas.create_image(x, y, image=image, anchor=tk.CENTER, tags=image_name)
        canvas.tag_bind(image_name, "<Enter>")
        images.append(image)

    label_x = width / 16-20
    label_y = y + image_height / 2 + 20
    button_x = width / 16 + 20
    button_y = y + image_height / 2 + 20
    labels = []
    buttons = []

    for i in range(len(cards)):
        label = tk.Label(window, text="0", font=("Arial", 10), bg="white")
        label.place(x=label_x, y=label_y, anchor=tk.CENTER)
        button = tk.Button(window, text="-", font=("Arial", 10), bg="white")
        button["width"] = 1
        button["height"] = 1
        button.place(x=button_x, y=button_y, anchor=tk.CENTER)
        labels.append(label)
        buttons.append(button)
        label_x += width / 8
        button_x += width / 8

    # 一二板块间的分割线
    canvas.create_line(0, label_y+20, width, label_y+20, fill="black", width=3)

    # 第二板块，推荐决策
    labelupgrade = tk.Label(window, text="推荐决策", font=("Arial", 10), bg="white")
    labelupgrade.place(x=width / 2, y=label_y + 40, anchor=tk.CENTER)

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

    if buy!=0:
        label3_x = width / 10 * (2 * buy - 1)
        label3_y = height / 2 + 20
        label3 = tk.Label(window, text="choose", font=("Arial", 15), bg="red")
        label3.place(x=label3_x, y=label3_y, anchor=tk.CENTER)

    if sell!=0:
        label4_x = width / 10 * (2 * sell - 1)
        label4_y = height / 2 + 20
        label4 = tk.Label(window, text="sell", font=("Arial", 15), bg="red")
        label4.place(x=label4_x, y=label4_y, anchor=tk.CENTER)


    # upgrade图标
    labelupgrade = tk.Label(window, text="upgrade", font=("Arial", 12), bg="white")
    labelupgrade.place(x=width / 2, y=height / 2 + 70, anchor=tk.CENTER)
    if upgrade == True:
        labelupgrade["borderwidth"] = 1
        labelupgrade["relief"] = "solid"
        labelupgrade["bg"] = "red"
        labelupgrade["fg"] = "black"
    else:
        labelupgrade["borderwidth"] = 1
        labelupgrade["relief"] = "solid"
        labelupgrade["bg"] = "white"
        labelupgrade["fg"] = "black"

    # 二三板块间的分割线
    canvas.create_line(0, height / 2 + 90, width, height / 2 + 90, fill="black", width=3)

    # 第三板块，推荐装备
    label3 = tk.Label(window, text="推荐装备", font=("Arial", 10), bg="white")

    button = tk.Button(window, text="更新截图", font=("Arial", 10), bg="white")
    button["width"] = 10
    button["height"] = 2
    button.place(x=width / 2, y=height - 50, anchor=tk.CENTER)
    button["command"] = lambda: quit_app(window)

    return window
"""
cards = [1, 2, 3, 4, 5, 6, 7, 8]
options = [1, 2, 3, 4, 5]

window=show_images(cards,True,1,0,options)
window.mainloop()
"""
