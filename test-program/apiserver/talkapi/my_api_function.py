import requests

def getluxuntalk():
    """
    鲁迅语录Api接口
    :return:
    """
    try:
        response = requests.get(url='http://127.0.0.1:49152/luxuntalk', timeout=300)
        # 打印响应内容，用于调试
        print("响应内容:", response.text)
        result = response.json()
        if result:
            return result.get('data')
        return None
    except requests.RequestException as e:
        print(f'网络请求出错, 错误信息: {e}')
        return None
    except ValueError as e:
        print(f'解析JSON出错, 错误信息: {e}')
        return None

def getvocabulary():
    """
    英语单词Api接口
    :return:
    """
    try:
        response = requests.get(url='http://127.0.0.1:49152/vocabulary', timeout=300)
        # 打印响应内容，用于调试
        print("响应内容:", response.text)
        result = response.json()
        if result:
            return result.get('data')
        return None
    except requests.RequestException as e:
        print(f'网络请求出错, 错误信息: {e}')
        return None
    except ValueError as e:
        print(f'解析JSON出错, 错误信息: {e}')
        return None