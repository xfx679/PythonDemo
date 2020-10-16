import hashlib
import requests


def createSn(secret_key, params={}):
    """获取token"""
    sortedKeys = sorted(params.keys())
    str_value = ""
    for key in sortedKeys:
        tmp = "&" + key + "=" + params[key]
        str_value += tmp
    str_value = str_value.strip("&") + secret_key
    sign = hashlib.md5(str_value.encode()).hexdigest()
    return sign.lower()


#  测试环境物流价格签名key及url
test_key = 'uYqfaA8Bv6yQHJuEn6ueZQBXxJx4bogM'
url_test_tran = 'http://feature1-api-lyprice.fat.xin.com/tpl/getBatchData'
#  正式环境物流价格签名key及url
for_key = 'XHnWtSIgGa80SnrUUww6tYjxXalqeZd6'
url_for_tran = 'http://api-lyprice.xin.com/tpl/getBatchData'

#  物流价格接口参数：城市
params_tran = {"cityList": "201-201", "source": "app"}


def get_re(params):
    """批量获取城市物流时效（正式）"""
    token1 = createSn(for_key, params)
    params.update(token=token1)
    re = requests.post(url_for_tran, params).text
    print(re)


def get_re_test(params):
    """批量获取城市物流时效（测试）"""
    token1 = createSn(test_key, params)
    params.update(token=token1)
    re = requests.post(url_test_tran, params).text
    print(re)


def get_version():
    """获取物流版本号"""
    params = {'source': 'pc'}
    url = 'http://api-lyprice.xin.com/tpl/getDataVerion'
    token1 = createSn(test_key, params)
    params.update(token=token1)
    re = requests.post(url, params).text
    print(re)


def get_big():
    """获取大型车modeid"""
    url = 'http://api-mode.xin.com/cxSync/bigCarModeList'
    re = requests.post(url, {'source': 'ai', 'token': '9b430433f6be6918379ebaecc2ad6db9', 'modeid': '0'}).text
    print(re)


get_re(params_tran)
get_version()
# get_big()
