import requests
import time

def getrandomtalk():
    '''
    随机语录api接口
    '''
    try:
        '''jsonData = requests.get(url='https://api.dwo.cc/api/yi?api=yan', timeout=30).json()
        if "data" in jsonData:
            data = jsonData['data']
            zh = data.get("zh")
            en = data.get("en")
            if zh and en:
                result = f"{zh}\n{en}"'''
        result = requests.get(url='https://api.dwo.cc/api/yi?api=yan', timeout=30, verify=False).text
        if result:
            print(result)
            return result
        time.sleep(2)
        return None
    except Exception as e:
        print(f'随机语录api接口出现错误, 错误信息: {e}')
        return None