#_*_ coding:utf-8 _*_
# filename:weixin_autoreply.py

import hashlib
import blog.receive as receive
import blog.reply as reply

def handle(request):
    if request.method == 'POST':
        xml_msg = request.body
        formatMsg = receive.parse_xml(xml_msg)

        if isinstance(formatMsg,receive.Msg) and formatMsg.MsgType == 'text':
            toUser = formatMsg.FromUserName
            fromUser = formatMsg.ToUserName
            content = formatMsg.Content
            replyMsg = reply.TextMsg(toUser,fromUser,content)
            return replyMsg.send()
        else:
            print('待处理')
            return 'success'
            pass
    else:
        pass
        return 'success'


