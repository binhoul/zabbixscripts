#!/bin/sh
#sms.sh

to=$1
subject=$2
body=$3

#echo $to > /tmp/sms.log
#echo $subject >> /tmp/sms.log
#echo $body >> /tmp/sms.log

#echo `dirname $0`
/usr/bin/python `dirname $0`/send.py $to "$subject" &> /tmp/sms.log  && echo 'ok' >> /tmp/sms.log || echo 'Nok' >> /tmp/sms.log


