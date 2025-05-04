import requests
import time

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
    
def dogword():
    apiname = '舔狗api接口'
    try:
        print(f'正在调用{apiname}...')
        result = requests.get(url='https://api.pearktrue.cn/api/jdyl/tiangou.php', timeout=30).text
        if result:
            print(f'{apiname}调用成功!\n{result}')
            return result
        return None
    except Exception as e:
        print(f'{apiname}出现错误, 错误信息: {e}')
        return None

def todaynews():
    apiname = '当日新闻api接口'
    try:
        print(f'正在调用{apiname}...')
        result = requests.get(url='https://api.pearktrue.cn/api/60s/', timeout=30).json()
        if 'data' in result:
            result = result['data']
        if result:
            print(f'{apiname}调用成功!\n{result}\n')
            return result
        return None
    except Exception as e:
        print(f'{apiname}出现错误, 错误信息: {e}')
        return None
    
def historytoday():
    apiname = '历史上的今天api接口'
    try:
        print(f'正在调用{apiname}...')
        result = requests.get(url='https://api.pearktrue.cn/api/lsjt/?type=json', timeout=30).json()
        if 'data' in result:
            result = result['data']
        if result:
            print(f'{apiname}调用成功!\n{result}\n')
            return result
        return None
    except Exception as e:
        print(f'{apiname}出现错误, 错误信息: {e}')
        return None
    
def randomid():
    apiname = '随机外国人身份api接口'
    try:
        print(f'正在调用{apiname}...')
        result = requests.get(url='https://api.pearktrue.cn/api/sfz/usa.php', timeout=30).json()
        if 'data' in result:
            result = result['data']
        if result:
            print(f'{apiname}调用成功!\n{result}\n')
            return result
        return None
    except Exception as e:
        print(f'{apiname}出现错误, 错误信息: {e}')
        return None
    
def stupid():
    apiname = '弱智吧api接口'
    try:
        print(f'正在调用{apiname}...')
        result = requests.get(url='https://api.pearktrue.cn/api/ruozhiba/', timeout=30).json()
        if 'data' in result:
            result = result['data']
        if result:
            print(f'{apiname}调用成功!\n{result}')
            return result
        return None
    except Exception as e:
        print(f'{apiname}出现错误, 错误信息: {e}')
        return None

loveword()
dogword()
todaynews()
historytoday()
randomid()
stupid()