import requests
from bs4 import BeautifulSoup
import re

### 数据获取与距离计算
def get_page_content(request_url): # 获取网页内容
    header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    html = requests.get(request_url, headers=header, timeout=10)
    content = html.text
#     print(content)
    # 通过content创建BS对象
    soup = BeautifulSoup(content, 'html.parser',from_encoding='utf-8')
    return soup

def get_location(place, city): # 获取指定城市地点的经纬度
    # 获取查询
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    request_url = 'https://restapi.amap.com/v3/geocode/geo?key=1eb751daa6e3fd63fbc3737a9433fdd7&address=' + place + '&city=' + city
    data = requests.get(request_url, headers=header)
    #     data.endoding= 'utf-8'
    #     print(request_url)
    data = data.text
    #     print(data)

    # 匹配经纬度
    pattern = 'location":"(.*?),(.*?)"'
    result = re.findall(pattern, data)  # 形如[('121.513870', '31.303558')]
    return result[0][0], result[0][1]

def compute_distance(longitude1, latitude1, longitude2, latitude2): #计算两经纬度之间的距离
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    start = str(longitude1) + ',' + str(latitude1)
    end = str(longitude2) + ',' + str(latitude2)
    request_url = 'https://restapi.amap.com/v3/distance?origins=' + start + '&destination=' + end + '&key=1eb751daa6e3fd63fbc3737a9433fdd7'
    data = requests.get(request_url, headers=header)
    # data.encoding='utf-8'
    data = data.text
    # print(data)
    pattern = 'distance":"(.*?)","duration":"(.*?)"'
    result = re.findall(pattern, data)
    return result[0][0]