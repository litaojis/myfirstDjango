#
#
import blog.common as common
from urllib import request
import ssl
import json
from djang.core.cache import cache

class WxUtil(object):

    def __init__(self, AppID=None, AppSecret=None):
        self.AppID = AppID
        self.AppSecret = AppSecret

    def getAccess_Token(self):
        url = common.URL_ACCESS_TOKEN
        if self.AppID == None or self.AppID == '':
            print('self.AppID is None')
            return None
        elif self.AppSecret == None or self.AppSecret == '':
            print('self.AppSecret is None')
            return None
        url = url.format(self.AppID, self.AppSecret)
        # ssl._create_unverified_context()
        response = request.urlopen(url)
        print(response.status)
        print(response.msg)
        if response.status == 200:
            jsonObj = json.loads(str(response.read(),encoding = 'utf-8'))
            access_token = jsonObj['access_token']
            self..access_token = access_token
            return self.access_token
        return None

    def cacheAccessToken(self,timeOut = True,time =7000):
        cache.set('access_token',self.access_token,timeout = time)
        cache.set('access_token_timeout',timeOut)