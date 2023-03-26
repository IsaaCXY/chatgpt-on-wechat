#!/bin/bash
#后台运行Chat_on_webchat执行脚本

cd `dirname $0`/..
export BASE_DIR=`pwd`
echo $BASE_DIR

# check the nohup.out log output file
if [ ! -f "${BASE_DIR}/nohup_tele.out" ]; then
  touch "${BASE_DIR}/nohup_tele.out"
echo "create file  ${BASE_DIR}/nohup_tele.out"  
fi

nohup python3.7 "${BASE_DIR}/app.py" telegram & tail -f "${BASE_DIR}/nohup_tele.out"

echo "Chat_on_webchat is starting，you can check the ${BASE_DIR}/nohup_tele.out"
