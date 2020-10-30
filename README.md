# mhost

## 功能：
* 项目托管网址：http://www.valyriansteel.top  测试账号密码 test test
* 用户注册登录后可管理主机资产清单（主机名、IP地址、账户密码、所属组等），对自己的主机组和主机信息增删改查。
* 选择特定主机后一键登录。windows组的主机使用rdp，linux或其他组的主机使用ssh。暂不支持选则3389和22之外的端口。如需要请改源码:mhost\mhosts\templates\win_group.html 和 linux_group.html


## 使用方法：
* windows服务器RDP连接功能需要通过IE浏览器的Active X控件实现，设置IE浏览器，将地址加入受信任站点，启用与Active控件相关的所有选项。
```
1、打开IE浏览器。
2、在IE浏览器中找到工具按钮，单击即可。
3、选择下面的“INTERNET选项”，并单击。
4、然后点击“安全”这个选项，下面会出现相应的菜单。
5、在接下来的页面中，选择“可信任站点”。
6、接下来选择下方的“自定义级别”这个按钮。
7、找到activex控件和插件，启用所有子项就可以啦。
```
* linux服务器的SSH连接功能需要客户端安装winSCP软件和putty软件（下载并设置环境变量），修改注册表使系统识别ssh链接的打开方式，如 ssh://10.0.0.1。(通过winSCP调用putty打开。可参考此项目源代码中other目录下的putty.bat和putty.reg。putty.reg用于修改注册表，putty.bat用于调用putty，根据情况修改)。

## 程序环境
* django 1.8.4
* python 3.4.3
* django-bootstrap3==6.2.2

## 部署时：
* pip install gunicorn==19.3.0 -i http://mirrors.aliyun.com/pypi/simple --trusted-host=mirrors.aliyun.com

* pip install django-bootstrap3==6.2.2 -i http://mirrors.aliyun.com/pypi/simple --trusted-host=mirrors.aliyun.com

vim /root/mhost/gunicorn.conf.py

import multiprocessing
bind = "0.0.0.0:80"
#绑定的ip与端口

workers = 2
#核心数

errorlog = '/root/gunicorn/gunicorn.error.log'
#发生错误时log的路径

accesslog = '/root/gunicorn/gunicorn.access.log'
#正常时的log路径
#loglevel = 'debug'   #日志等级

proc_name = 'gunicorn_mhost'
#进程名

* 配置完毕运行gunicorn，可写成启动脚本。执行此命令需要进入项目根目录mhost

gunicorn mhost.wsgi:application -D -c /root/mhost/gunicorn.conf.py


## 待完善功能
侧边导航栏
