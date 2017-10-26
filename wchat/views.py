#coding=utf-8
import hashlib
import json
from lxml import etree
from django.utils.encoding import smart_str
from django.views.decorrators.csrf_exempt
from django.http import HttpResponse
from auto_replay.views import auto_replay_main

WEIXIN_TOKEN = 'write-a-value'
@csrf_exempt
def weixin(request):
    if request.method == 'GET':
        signature = request.GET.get("signature",None)
        timestamp = request.GET.get("timestamp",None)
        nonce = request.GET.get("nonce",None)

        echostr = request.GET.get("echostr",None)
        roken = WEIXIN_TOKEN
        tmp_list = [tokenb,timestamp,nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdgest()
        if tmp_str = signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('weixin index')

    else:
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        response_xml = auto_reply_main(request_xml)
        return HttpResponse(response_xml)