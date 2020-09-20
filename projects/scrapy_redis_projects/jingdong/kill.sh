if [ ! -f "$1" ];then
  echo "$1文件不存在"
else
  ps -ef|grep "$1"|grep -v grep|awk '{print $2}'|xargs kill -9
fi