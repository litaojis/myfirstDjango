#_*_ coding:utf-8 _*_
# filename:weixin_autoreply.py

import hashlib
import receive
import reply
import web


class WeiXinHandle(object):
    
    def  __init__(self):
    
    def handle(self,request):
        if request.method = 'POST':
            xml_msg = request.body
            formatMsg = receive.parse_xml(msg)

            if isinstance(formatMsg,receive.Msg) and formatMs.MsgType == 'text':
                toUser = formatMsg.FromUserName
                fromUser = formatMsg.toUserName
                content = 'test'
                replyMsg = reply.TextMsg(toUser,fromUser,content)
                return replyMsg.send()
            else:
                print('待处理')
                return 'success'
                pass
                

