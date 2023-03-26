#!/bin/bash
#后台运行Chat_on_webchat执行脚本

cd `dirname $0`/..
export BASE_DIR=`pwd`
echo $BASE_DIR

# check the nohup_wechat.out log output file
if [ ! -f "${BASE_DIR}/nohup.out" ]; then
  touch "${BASE_DIR}/nohup_wechat.out"
echo "create file  ${BASE_DIR}/nohup_wechat.out"  
fi

nohup_wechat python3.7 "${BASE_DIR}/app.py" wx & tail -f "${BASE_DIR}/nohup_wechat.out"

echo "Chat_on_webchat is starting，you can check the ${BASE_DIR}/nohup_wechat.out"
