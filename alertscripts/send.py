#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import sys
import time

mobile = int(sys.argv[1])
content = sys.argv[2].replace(' ','__')
ptime = time.strftime("%Y%m%d%H%M%S",time.localtime())
myfile = open('/tmp/sms.log','w')
myfile.write('value1' + sys.argv[1] + '\n')
myfile.write('value2' + sys.argv[2] + '\n')
myfile.write('value3' + sys.argv[3] + '\n')
#print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')

#####for debug ######
#handler = urllib2.HTTPHandler(debuglevel=1)
#opener = urllib2.build_opener(handler)
#urllib2.install_opener(opener)

sign = u'【科技】'
#enc_sign = unicode(sign, 'gbk' )
#enc_sign = sign.decode('utf-8').encode('gbk')
enc_sign = urllib.quote(sign.decode('utf8').encode('gbk'))
myfile.write(enc_sign + '\n')
url = str("http://mb345.com:999/ws/Send.aspx?CorpID=***DK0001***&Pwd=**00**&Mobile=%d&Content=%s%s&Cell=23&SendTime=%s" %(mobile,content,enc_sign,ptime))
myfile.write(url)

#url = "http://mb345.com:999/LinkWS.asmx?op=Send"
#print post(url)
#myfile.write(urllib2.urlopen(url).read())
urllib2.urlopen(url)

myfile.close()
