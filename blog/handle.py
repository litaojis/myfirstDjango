#coding=utf-8
import hashlib
import json
from lxml import etree
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpRequest
# from auto_reply.views import auto_reply_main # 修改这里

WEIXIN_TOKEN = 'qrjnA2TwLC9smalN1ceS'


@csrf_exempt
def handle(request):
    if request.method == "GET" :
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get("nonce")
        echostr = request.GET.get("echostr")
        token = WEIXIN_TOKEN #请按照公众平台官网\基本配置中信息填写

        hlist = [signature,nonce,token]
        hlist.sort()
        tmp_str = "%s%s%s" % tuple(hlist)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if (tmp_str == signature):
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin  index")
    else:
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        # response_xml = auto_reply_main(request_xml)
        return HttpResponse(response_xml)
