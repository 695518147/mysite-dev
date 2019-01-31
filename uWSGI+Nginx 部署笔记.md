#### 安装Nginx
```
sudo yum install nginx
配置Nginx
vim etc/nginx/nginx.conf
修改如下

server {
 　　　　 listen  80;
  　　　　server_name XXX.XXX.XXX; #公网地址

　　　　  location / {
　　　　include      uwsgi_params;
　　　　uwsgi_pass   127.0.0.1:8001;  # 指向uwsgi 所应用的内部地址,所有请求将转发给uwsgi 处理
　　　　uwsgi_param UWSGI_PYHOME /root/School/venv; # 指向虚拟环境目录
　　　　uwsgi_param UWSGI_CHDIR  /root/School; # 指向网站根目录
　　　　uwsgi_param UWSGI_SCRIPT manage:app; # 指定启动程序
 　　　　 }
}
Nginx简单指令
启动nginx：
命令行输入nginx或者nginx -c nginx配置文件

关闭nginx：
ps -ef|grep nginx查看nginx 线程ID
kill -QUIT 线程ID

Nginx出现413 Request Entity Too Large错误解决方法
打开nginx主配置文件nginx.conf,找到http{}段，修改或者添加

client_max_body_size 4m;
```

### 安装uWSGI

```
需安装三个库:

1.sudo yum install libxml2
2.sudo yum install gcc
3.sudo yum install python-devel
然后:

pip  install uwsgi 
配置uWSGI
进入flask应用程序目录

vim config.ini
编辑:

[uwsgi]
# uwsgi 启动时所使用的地址与端口
socket = 127.0.0.1:8001 
# 指向网站目录
chdir = /root/School 
# python 启动程序文件
wsgi-file = manage.py 
# python 程序内用以启动的 application 变量名
callable = app 
# 处理器数
processes = 4
# 线程数
threads = 2
#状态检测地址
stats = 127.0.0.1:9191
uWSGI命令
uwsgi 启动 ：虚拟环境下uwsgi config.ini
uwsgi 关闭：虚拟环境下killall -9 uwsgi
```

部署说明
部署图

uWSGI 提高并发访问支持，提高服务运行稳定性
Nginx在这里最基本的一个用处就是转发：当客户访问一个域名或者IP时 Nginx就将访问转发给uwsgi处理
Supervisor可以同时启动多个应用，更重要的是，当某个应用Crash的时候，它可以自动重启该应用，保证可用性
这样uwsgi可以让supervisor帮助启动，而且当uwsgi Crash时会尝试帮重启它，保证uwsgi和网站的可用性

如何理解Nginx, WSGI, Flask之间的关系 ? 这是一篇很好的文章