import logging
import os
import time

# 按天生成log/report
today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())
# print(os.path.dirname(__file__))
# print(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'apps/app-release-ceshi.apk')))
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../apps/app-release-ceshi.apk')))
# 项目路径
prj_path = os.path.dirname(os.path.dirname(__file__))  # 当前文件的上一级目录

# log配置
log_file = os.path.join(prj_path, 'result', 'log', 'log_{}.txt'.format(today))  # 更改路径到log目录下
logging.basicConfig(level=logging.INFO,   # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')   # 追加模式

# android driver配置
path = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
platformName = 'Android'
deviceName = '127.0.0.1:62001'
autoLaunch = 'true'   # 是否自动启动
app = path('../apps/app-release-ceshi.apk')
appPackage = 'com.aitou.risk'
appActivity = 'com.atriskapp.MainActivity'

# 数据库配置
db_host = 'sh-cdb-0auhvizu.sql.tencentcdb.com'
db_port = 62736
db_user = 'root'
db_password = 'db!N70ES65#ac'
db = 'uatlflt'
