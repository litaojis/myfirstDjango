#
#
import blog.common as common
from urllib import request
import ssl

class WxUtil(object):

    def __init__(self):
        pass

    def getAccess_Token(self,AppID = None,AppSecret = None):
        url = common.URL_ACCESS_TOKEN
        if AppID == None or AppID == '':
            print('AppID is None')
            return None
        elif AppSecret == None or AppSecret == '':
            print('AppSecret is None')
            return None
        url  = url.replace('{APPID}',AppID).replace('{APPSECRET}',AppSecret)
        # ssl._create_unverified_context()
        response = request.urlopen(url)
        print(response.status)
        print(response.content)
        if response.status == 200:
            return response.content
        return None
    