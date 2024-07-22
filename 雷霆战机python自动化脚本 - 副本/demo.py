import pyautogui
import time

# 使用鼠标右键拖动来代替滚动
def drag_to_find_stage_49(image_path):
    drag_attempts = 0
    max_drag_attempts = 50  # 最大拖动次数，可以根据需要调整
    initial_position = pyautogui.position()  # 获取初始位置

    while drag_attempts < max_drag_attempts:
        try:
            # 尝试查找第49关按钮的图像
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
            if location:
                return location
        except pyautogui.ImageNotFoundException:
            pass
        
        # 如果没有找到，则右键长按拖动鼠标向上
        pyautogui.mouseDown(button='right')
        pyautogui.moveRel(0, -500, duration=1)  # 向上拖动500像素，持续1秒
        pyautogui.mouseUp(button='right')
        
        # 将鼠标移回初始位置
        pyautogui.moveTo(initial_position)

        print(f"拖动了 {drag_attempts + 1} 次")
        drag_attempts += 1
        time.sleep(1)  # 增加延迟以确保拖动操作能被识别

    raise Exception("未找到第49关按钮")

# 单击按钮
def click_button(image_path, wait_time_after_detection=0.5):
    location = None
    while not location:
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        except pyautogui.ImageNotFoundException:
            pass
    time.sleep(wait_time_after_detection)  # 在识别到按钮后停顿指定时间
    pyautogui.click(location)
    time.sleep(0.5)  # 确保点击后有足够时间响应

# 主函数
def main():
    stage_49_image_path = 'stage_49.png'
    attack_image_path = 'attack.png'
    continue_image_path = 'continue.png'
    
    while True:
        # 给予3秒等待时间
        print("准备开始操作，请把鼠标放到游戏上，2秒后执行...")
        time.sleep(2)

        # 查找并单击第49关按钮
        try:
            stage_49_location = drag_to_find_stage_49(stage_49_image_path)
            pyautogui.click(stage_49_location)
            time.sleep(1)  # 等待1秒
        except Exception as e:
            print(str(e))
            return

        # 查找并单击“出击”按钮
        click_button(attack_image_path)

        # 等待并单击“继续”按钮
        print("等待并单击'继续'按钮...")
        click_button(continue_image_path, wait_time_after_detection=2)

        # 停顿0.001秒钟
        time.sleep(0.001)

if __name__ == "__main__":
    main()
