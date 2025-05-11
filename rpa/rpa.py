# -*- coding: utf-8 -*-
import yaml
import pyperclip
import pyautogui
import time
import os
import sys
import requests

def loveword():
    apiname = '情话api接口'
    try:
        print(f'正在调用{apiname}...')
        result = requests.get(url='https://api.pearktrue.cn/api/jdyl/qinghua.php', timeout=30).text
        if result:
            print(f'{apiname}调用成功!\n{result}\n')
            return result
        return None
    except Exception as e:
        print(f'{apiname}出现错误, 错误信息: {e}')
        return None

# 定义版权信息全局变量 count
count = 0
projectcopyright = f'\nauthor:cheraljun\naddress:https://github.com/cheraljun/rpa.git'

# 鼠标操作函数
def mouse_operation(action, click_times, lOrR, img=None, x=None, y=None, retry=1, image_path=None):
    if action == 'hover':
        if img:
            img_path = os.path.join(image_path, img)
            if not os.path.exists(img_path):
                print(f"图片文件 {img_path} 不存在")
                return False
            attempts = 0
            while attempts < retry or retry == -1:
                print(f"尝试查找图片: {img_path}")
                try:
                    location = pyautogui.locateCenterOnScreen(img_path, confidence=0.9)
                    if location is not None:
                        x, y = location
                        pyautogui.moveTo(x, y)
                        return True
                    else:
                        print(f"未找到图片: {img_path}，继续尝试...")
                except pyautogui.ImageNotFoundException:
                    print(f"未找到图片: {img_path}，继续尝试...")
                attempts += 1
            return False
    elif action == 'click':
        if img:
            img_path = os.path.join(image_path, img)
            if not os.path.exists(img_path):
                print(f"图片文件 {img_path} 不存在")
                return False
            attempts = 0
            while attempts < retry or retry == -1:
                print(f"尝试查找图片: {img_path}")
                try:
                    location = pyautogui.locateCenterOnScreen(img_path, confidence=0.9)
                    if location is not None:
                        x, y = location
                        if lOrR == 'left':
                            pyautogui.click(x, y, clicks=click_times)
                        elif lOrR == 'right':
                            pyautogui.rightClick(x, y, clicks=click_times)
                        return True
                    else:
                        print(f"未找到图片: {img_path}，继续尝试...")
                except pyautogui.ImageNotFoundException:
                    print(f"未找到图片: {img_path}，继续尝试...")
                attempts += 1
            return False
        elif x is not None and y is not None:
            if lOrR == 'left':
                pyautogui.click(x, y, clicks=click_times)
            elif lOrR == 'right':
                pyautogui.rightClick(x, y, clicks=click_times)
            return True
        else:
            if lOrR == 'left':
                pyautogui.click(clicks=click_times)
            elif lOrR == 'right':
                pyautogui.rightClick(clicks=click_times)
            return True

# 滚轮操作函数
def scroll_operation(distance):
    try:
        print(f"开始执行滚轮滚动操作，滚动距离为 {distance}")
        pyautogui.scroll(int(distance))
        time.sleep(0.2)
        print(f"滚轮滚动操作执行完毕，滚动距离为 {distance}")
        return True
    except Exception as e:
        print(f"滚轮操作失败: {e}，终止程序")
        return False

# 停留操作函数
def wait_operation(duration):
    try:
        print(f"开始等待 {duration} 秒")
        time.sleep(duration)
        print(f"等待 {duration} 秒操作执行完毕")
        return True
    except Exception as e:
        print(f"等待操作失败: {e}，终止程序")
        return False

# 输入操作函数，开放调用外部api的接口
def input_operation(content, use_api=False):
    print("开始执行输入操作")
    try:
        if use_api:
            # 这里调用外部api获取内容
            input_content = f'''Hi，这里专业代写商业计划书（BP），个人代写不是机构，无中间价，有需要请私信[握手R]～{loveword()}[doge]'''  # 假设getanswer是外部api函数
        else:
            input_content = content
        if input_content:
            pyperclip.copy(input_content)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.2)
            print("输入操作执行完毕")
            return True
        else:
            print("未获取到有效输入内容，终止程序")
            return False
    except Exception as e:
        print(f"输入操作失败: {e}，终止程序")
        return False

# 数据检查函数，用于检查从配置文件中读取的指令列表是否合法
def dataCheck(cmd_list):
    checkCmd = True
    if not isinstance(cmd_list, list) or len(cmd_list) < 1:
        checkCmd = False
        print("配置文件为空或格式错误（需为列表）")
        return checkCmd

    for idx, cmd in enumerate(cmd_list, 1):
        cmd_type = cmd.get('type')
        if cmd_type not in ['mouse', 'scroll', 'wait', 'input']:
            checkCmd = False
            print(f"第 {idx} 行指令类型错误（需为 'mouse', 'scroll', 'wait', 'input'）")

        cmd_content = cmd.get('content')
        if cmd_type == 'mouse':
            action = cmd_content.get('action')
            if action not in ['hover', 'click']:
                checkCmd = False
                print(f"第 {idx} 行鼠标操作类型错误（需为 'hover' 或 'click'）")
            click_times = cmd_content.get('click_times')
            if not isinstance(click_times, (int, float)):
                checkCmd = False
                print(f"第 {idx} 行鼠标操作点击次数错误（需为数字）")
            lOrR = cmd_content.get('lOrR')
            if lOrR not in ['left', 'right']:
                checkCmd = False
                print(f"第 {idx} 行鼠标操作左右键错误（需为 'left' 或 'right'）")
            img = cmd_content.get('img')
            x = cmd_content.get('x')
            y = cmd_content.get('y')
            # 修改此处逻辑，如果是点击操作且没有提供定位信息，也认为是合法的
            if action == 'click' and not img and (x is None or y is None):
                pass
            elif not img and (x is None or y is None):
                checkCmd = False
                print(f"第 {idx} 行鼠标操作缺少定位信息（需提供图片名或坐标）")
        elif cmd_type == 'scroll':
            if not isinstance(cmd_content, (int, float)):
                checkCmd = False
                print(f"第 {idx} 行滚轮操作内容错误（需为数字）")
        elif cmd_type == 'wait':
            if not isinstance(cmd_content, (int, float)):
                checkCmd = False
                print(f"第 {idx} 行等待操作内容错误（需为数字）")
        elif cmd_type == 'input':
            if not isinstance(cmd_content, dict):
                checkCmd = False
                print(f"第 {idx} 行输入操作内容错误（需为字典）")
            else:
                input_content = cmd_content.get('content')
                if not isinstance(input_content, str):
                    checkCmd = False
                    print(f"第 {idx} 行输入操作内容中的 'content' 错误（需为字符串）")
                use_api = cmd_content.get('use_api')
                if not isinstance(use_api, bool):
                    checkCmd = False
                    print(f"第 {idx} 行输入操作内容中的 'use_api' 错误（需为布尔值）")

        retry = cmd.get('retry', 1)
        if not isinstance(retry, int) or (retry != -1 and retry < 1):
            checkCmd = False
            print(f"第 {idx} 行重复次数错误（需为 1 或 -1）")

    return checkCmd

# 主工作函数，用于执行从配置文件中读取的指令列表
def mainWork(cmd_list, image_path):
    global count
    for cmd in cmd_list:
        try:
            cmd_type = cmd['type']
            cmd_content = cmd['content']
            retry = cmd.get('retry', 1)

            print(f"当前指令：类型 {cmd_type}，内容 {cmd_content}，重复次数 {retry}")

            if cmd_type == 'mouse':
                action = cmd_content.get('action')
                click_times = cmd_content.get('click_times')
                lOrR = cmd_content.get('lOrR')
                img = cmd_content.get('img')
                x = cmd_content.get('x')
                y = cmd_content.get('y')
                success = mouse_operation(action, click_times, lOrR, img, x, y, retry, image_path)
                if not success:
                    print(f"{action} 操作失败，已尝试 {retry} 次，终止程序")
                    sys.exit(1)
            elif cmd_type == 'scroll':
                success = scroll_operation(cmd_content)
                if not success:
                    sys.exit(1)
            elif cmd_type == 'wait':
                success = wait_operation(cmd_content)
                if not success:
                    sys.exit(1)
            elif cmd_type == 'input':
                use_api = cmd_content.get('use_api', False)
                content = cmd_content.get('content')
                success = input_operation(content, use_api)
                if not success:
                    sys.exit(1)

        except Exception as e:
            print(f"执行指令时出错: {e}，终止程序")
            sys.exit(1)

# 封装的 RPA 函数，调用该函数即可直接执行配置文件中的指令
def rpa(selected_scenario):
    global count
    file = r'C:\\Users\\admin\\Desktop\\jun\\rpa\\rpa\\config\\config.yaml'
    print(f"尝试打开配置文件: {file}")

    try:
        with open(file, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        scenario_config = config['scenarios'].get(selected_scenario)
        if not scenario_config:
            print(f"错误：未找到场景 {selected_scenario} 的配置")
            return
        image_path = scenario_config['image_path']
        cmd_list = scenario_config['commands']
    except FileNotFoundError:
        print(f"错误：未找到文件 {file}")
        return
    except yaml.YAMLError as e:
        print(f"错误：解析 YAML 文件时出错 {e}")
        return

    print('欢迎使用 RPA 工具')
    checkCmd = dataCheck(cmd_list)
    if checkCmd:
        mainWork(cmd_list, image_path)
    else:
        print('输入数据有误，请检查！')
    count += 1

if __name__ == "__main__":
    while True:
        scenario_input = input('''请选择操作场景:
wechat
xhs\n选择?''')
        if scenario_input in ['wechat', 'xhs']:
            while True:
                user_input = input("请输入执行次数（整数）或输入 'loop' 进行循环执行: ")
                if user_input == 'loop':
                    count = 0
                    while True:
                        rpa(scenario_input)
                        print(f"已执行 {count} 次")
                try:
                    num_runs = int(user_input)
                    if num_runs > 0:
                        count = 0
                        for i in range(num_runs):
                            rpa(scenario_input)
                            print(f"已执行 {count} 次")
                        break
                    else:
                        print("输入的整数必须大于 0，请重新输入。")
                except ValueError:
                    print("输入无效，请输入一个正整数或 'loop'。")
            break
        else:
            print("输入的场景无效，请输入 'wechat' 或 'xhs'。")