import psutil
# print(psutil.disk_partitions())
# print(psutil.disk_usage('/'))
# print(psutil.disk_io_counters())
# print(psutil.net_io_counters())
# print(psutil.net_if_addrs())
# print(psutil.net_connections())
# pro = psutil.pids()
# for x in pro:
#     p = psutil.Process(x)
#     s = p.status()
#     t= p.cpu_times()
#     # u = p.username()
#     print('进程及状态：%s%s%s' %(p, s, t))
# print(psutil.Process(11416))
print(psutil.test())