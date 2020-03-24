#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Android调试日志服务器
# 
# 需要安装web.py库，easy_install web.py 或者pip install web.py
# 
# 服务端，运行python uconsole.py 启动日志控制台服务器
# 默认端口是8080，启动之后，可以浏览器中访问http://localhost:8080
# 后面的日志就可以在网页中来查看了，网页会自动刷新
#
# 客户端中需要配置日志打印相关参数，
# 需要在AndroidManifest.xml中配置对应的参数和控制台的地址
# 使用 python uconsole.py 8082 更改端口
#
#
# 使用方法：
# 1.服务端使用 python uconsole.py 8082启动服务
# 2.compile 'com.onwardsmediagroup:LogToy:1.0.0'
# 3.application配置
# <meta-data android:name="ulog.enable" android:value="true" />  <!--是否开启日志，关闭之后，不会输出到logcat也不会输出到远程-->
# <meta-data android:name="ulog.level" android:value="DEBUG" />   <!--日志级别(DEBUG|INFO|WARNING|ERROR)-->
# <meta-data android:name="ulog.local" android:value="true" />    <!--是否在logcat中打印-->
# <meta-data android:name="ulog.remote" android:value="true" />   <!--是否远程打印-->
# <meta-data android:name="ulog.remote_interval" android:value="500" />   <!--远程打印时，日志上报间隔，单位毫秒-->
# <meta-data android:name="ulog.remote_url" android:value="http://192.168.18.9:8080/" />  <!--远程日志服务器地址，就是uconsole监听的地址-->
# 4.application启动LogToy.init()；
# 5.退出app销毁LogToy.destory();
# 6.日志调用LogToy.d("bigbang", "测试中文");
# 7.打开localhost:8082/  查看日志
#

import sys
import argparse
import stat
import json
import web

web.config.debug = False

urls = (
	'/','index'
)

localLogs = ""


class index:

	def GET(self):

		htmlFormat = "<html><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /><head><title></title></head><body>%s   <script type=\"text/javascript\">function myrefresh(){window.location.reload();window.scrollTo(0,document.body.scrollHeight);}setTimeout('myrefresh()',1000); </script></body></html>"
		global localLogs
		return htmlFormat % localLogs


	def POST(self):

		data = web.data()
		data = data.decode('utf-8', 'ignore')

		logs = json.loads(data).get('log')
		if isinstance(logs, str):
			if(logs.startswith("{")): #App crash Error
				logs = "["+logs+"]"
			logs = json.loads(logs)

		print(logs)
		for log in logs:
			if 'stack' not in log:
				log['stack'] = " "
			color = '#808080'
			if log['level'] == 'INFO':
				color = '#008000'
			elif log['level'] == 'WARNING':
				color = '#FFA500'
			elif log['level'] == 'ERROR':
				color = '#FF0000'

			strLog = '<div style="color:%s">%s  %s: [%s] %s </div>' % (color, log['time'],log['level'], log['tag'], log['msg'])

			stacks = log['stack'].split('\n')
			strLog = strLog + ('<div color="%s">' % color)
			for s in stacks:
				strLog = strLog + ('<div>%s</div>' % (s.strip()))

			strLog = strLog + '</div>'

			global localLogs
			localLogs = localLogs + strLog

		return ""


if __name__ == '__main__':

	app = web.application(urls, globals())
	app.run()


import sys
import argparse
import stat
import json
import web

web.config.debug = False

urls = (
	'/','index'
)

localLogs = ""


class index:

	def GET(self):

		htmlFormat = "<html><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /><head><title></title></head><body>%s   <script type=\"text/javascript\">function myrefresh(){window.location.reload();window.scrollTo(0,document.body.scrollHeight);}setTimeout('myrefresh()',1000); </script></body></html>"
		global localLogs
		return htmlFormat % localLogs


	def POST(self):

		data = web.data()
		data = data.decode('utf-8', 'ignore')

		logs = json.loads(data).get('log')
		if isinstance(logs, str):
			if(logs.startswith("{")): #App crash Error
				logs = "["+logs+"]"
			logs = json.loads(logs)

		print(logs)
		for log in logs:
			if 'stack' not in log:
				log['stack'] = " "
			color = '#808080'
			if log['level'] == 'INFO':
				color = '#008000'
			elif log['level'] == 'WARNING':
				color = '#FFA500'
			elif log['level'] == 'ERROR':
				color = '#FF0000'

			strLog = '<div style="color:%s">%s  %s: [%s] %s </div>' % (color, log['time'],log['level'], log['tag'], log['msg'])

			stacks = log['stack'].split('\n')
			strLog = strLog + ('<div color="%s">' % color)
			for s in stacks:
				strLog = strLog + ('<div>%s</div>' % (s.strip()))

			strLog = strLog + '</div>'

			global localLogs
			localLogs = localLogs + strLog

		return ""


if __name__ == '__main__':

	app = web.application(urls, globals())
	app.run()
