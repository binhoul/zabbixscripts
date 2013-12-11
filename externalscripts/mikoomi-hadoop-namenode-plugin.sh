#!/bin/sh
sh -x "`dirname $0`"/mikoomi-hadoop-namenode-plugin-helper.sh $* |tee debug.log
#"`dirname $0`"/mikoomi-hadoop-namenode-plugin-helper.sh $* 1> /dev/null 2> /dev/null && echo "Ok" || echo "NOk"
#nohup "`dirname $0`"/mikoomi-hadoop-namenode-plugin-helper.sh $* 
#echo "Ok"
exit
