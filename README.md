# mhost
manage host

## 需求：
* 用户注册登录后可添加主机（描述、主机名、所属组（windows、linux、db_servers））
* 用户可对自己的主机增删改查。最主要的功能是，单击主机即可调用系统powershell 进行
* ssh访问linux主机，调用系统RDP service可访问windows主机
* 用户在网页中访问主机时无需再输入被访问主机的账户密码

## 程序环境
* django 1.8.4
* python 3.4.3
* django-bootstrap3==6.2.2


## 待完善功能
* ssh尚未实现