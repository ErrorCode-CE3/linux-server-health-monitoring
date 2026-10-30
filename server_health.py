import psutil
import socket
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


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
print("Timestamp:", timestamp)
print("Hostname:", hostname)
print("CPU Usage:", cpu_usage, "%")
print("RAM Usage:", ram_usage, "%")
print("Disk_Usage", disk_usage, "%")


with open("logs/server_health.log", "a") as log_file:
    log_file.write("\n===== SERVER HEALTH REPORT =====\n")
    log_file.write(f"Timestamp: {timestamp}\n")
    log_file.write(f"Hostname: {hostname}\n")
    log_file.write(f"CPU Usage: {cpu_usage}%\n")
    log_file.write(f"RAM Usage: {ram_usage}%\n")
    log_file.write(f"Disk Usage: {disk_usage}%\n")


    if cpu_usage > 80:
        log_file.write("WARNING: High CPU Usage!\n")

    if ram_usage > 85:
        log_file.write("WARNING: High RAM Usage!\n")

    if disk_usage > 85:
        log_file.write("WARNING: High Disk Usage!\n")
