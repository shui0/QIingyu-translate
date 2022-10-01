import requests
import json

#======================================百度api请求token通用块儿=======================================
# 需要的库requests、json（import 进来就好了）
baidu_server = 'https://aip.baidubce.com/oauth/2.0/token?'  #获取token的server
grant_type = 'client_credentials'
client_id = 'zlXShBegxps1THXdG8mfP6nM' #API KEY
client_secret = 'klBQOr4kX3ZcarI4zadWTRik26P226yc' #Secret KEY   这里可以自己去百度注册，这里是我的API KEY 和 Secret KEY

#合成请求token的url
url = baidu_server+'grant_type='+grant_type+'&client_id='+client_id+'&client_secret='+client_secret

#获取token
res = requests.get(url).text
data = json.loads(res)  #将json格式转换为字典格式
token = data['access_token']
print(token)
#=====================================================================================================
