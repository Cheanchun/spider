# _*_coding=utf-8 _*


import datetime
import os
import socket
import time

import psutil

arm_host = '99.240.32.141'
file_path = '/home/work/data/tools/%s.txt'
r_file_path = '/home/work/data/tools/node_base_check'
content = u'-----------------------------系统基本信息---------------------------------------\n'
hostname = socket.gethostname()  # 获取本机主机名
# 当前时间
content += 'host name: %s' % hostname
now_time = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
content += 'check time:%s\n' % now_time
# 系统启动时间
content + u"系统启动时间: %s\n" % datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
# 系统用户
users_count = len(psutil.users())
users_list = ",".join([u.name for u in psutil.users()])
content += u"当前有%s个用户，分别是 %s\n" % (users_count, users_list)
content += u'-----------------------------cpu信息---------------------------------------\n'
# 查看cpu物理个数的信息
content += u"物理CPU个数: %s\n" % psutil.cpu_count(logical=False)
content += u"逻辑CPU个数: %s\n" % psutil.cpu_count(logical=True)
content += u"CPU核心总数: %s\n" % psutil.cpu_count()
# CPU的使用率
cpu = (str(psutil.cpu_percent(1))) + '%'
content += u"cup使用率: %s\n" % cpu
content += u'-----------------------------mem信息---------------------------------------\n'
# 查看内存信息,剩余内存.free  总共.total
# round()函数方法为返回浮点数x的四舍五入值。
free = str(round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2))
total = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2))
memory = int(psutil.virtual_memory().total - psutil.virtual_memory().free) / float(psutil.virtual_memory().total)
swap_free = str(round(psutil.swap_memory().free / (1024.0 * 1024.0 * 1024.0), 2))
swap_total = str(round(psutil.swap_memory().total / (1024.0 * 1024.0 * 1024.0), 2))
content += u"物理内存：       %s G\n" % total
content += u"剩余物理内存：   %s G\n" % free
content += u"物理内存使用率： %s %%\n" % int(memory * 100)
content += u"交换内存：       %s G\n" % swap_total
content += u"剩余交换内存：   %s G\n" % swap_free

content += u'-----------------------------磁盘信息---------------------------------------\n'
io = psutil.disk_partitions()
# content +=("系统磁盘信息：" + str(io))
o = psutil.disk_usage(u"/home/work/data")
ioo = psutil.disk_io_counters()
content += u"盘总容量：" + str(int(o.total / (1024.0 * 1024.0 * 1024.0))) + "G\n"
content += u"已用容量：" + str(int(o.used / (1024.0 * 1024.0 * 1024.0))) + "G\n"
content += u"可用容量：" + str(int(o.free / (1024.0 * 1024.0 * 1024.0))) + "G\n"
path = file_path % hostname
with open(path, mode='w') as fp:
    fp.write(content.encode('u8'))
os.system('scp %s work@%s:%s' % (path, arm_host, r_file_path))
