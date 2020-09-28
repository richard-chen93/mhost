#!/bin/sh
#提取壁纸图片URL(支持重定向)
url=$(expr "$(curl  -L -e  '; auto' https://www.bing.com/?mkt=zh-CN |grep g_img=)" : ".*g_img={url:\"\(.*\)\"};.*")
#去除url中的斜杠“\”
url="http://www.bing.com${url//\\/}"
#替换&符号
url=${url/\u0026/&}
echo $url
#提取图片名称
filename=$(expr "$url" : ".*id=\(.*\)&rf=.*")
#本地图片地址-当前用户下缺省图片目录
localpath="/Users/$USER/Pictures/$filename"
#下载图片至本地
curl -o $localpath  $url
#调用Finder应用切换桌面壁纸
osascript -e "tell application \"Finder\" to set desktop picture to POSIX file \"$localpath\""
