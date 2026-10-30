import psutil
import socket

cpu_usage = psutil.cpu_percent(interval=1)
print("CPU Usage:", cpu_usage, "%:")

if cpu_usage > 80:
	print("WARNING: High Cpu Usage!")



memory = psutil.virtual_memory()
ram_usage = memory.percent
print("RAM Usage:", ram_usage, "%")

if ram_usage > 85:
	print("WARNING: High Ram Usage")



disk = psutil.disk_usage('/')
disk_usage = disk.percent
print("Disk_Usage", disk_usage, "%")

if disk_usage > 85:
	print("WARNING: High Disk Usage!")




hostname = socket.gethostname()
print("Hostname", hostname)



print("\n===== 	SERVER HEALTH REPORT =====")
print("Hostname:", hostname)
print("CPU Usage:", cpu_usage, "%")
print("RAM Usage:", ram_usage, "%")
print("Disk_Usage", disk_usage, "%")
