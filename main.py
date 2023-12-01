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

