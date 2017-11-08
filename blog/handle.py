#coding=utf-8
import hashlib
import json
# from lxml import etree
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpRequest
import blog.weixin_autoreply as wxreply

WEIXIN_TOKEN = 'qrjnA2TwLC9smalN1ceS'
AppId = 'wxcf61a8651b530b1f'
AppSecret = '4182b42f21d069d0d9d3ee93363b1b1d'


@csrf_exempt
def handle(request):
    if request.method == "GET" :
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get("nonce")
        echostr = request.GET.get("echostr")
        token = WEIXIN_TOKEN #请按照公众平台官网\基本配置中信息填写
        print('signatuee:%s,timestamp:%s,notice:%s,echostr:%s'%(signature,timestamp,token,echostr))
        flag = weixinCheck(signature,timestamp,nonce,token)
        if (flag):
            return HttpResponse(echostr)
        else:
            return HttpResponse('sorry')
    else:
        handleResp = wxreply.handle(request)
        return HttpResponse(handleResp)

def weixinCheck(signature,timestamp,nonce,token):
    
    hlist = [nonce,timestamp,token]
    hlist.sort()
    tmp_str = "%s%s%s" % tuple(hlist)
    tmp_str = hashlib.sha1(tmp_str.encode(encoding='UTF-8')).hexdigest()
    
    print(tmp_str== signature)
    print(tmp_str)
    if (tmp_str == signature):
        return True
    else:
        return False
    
