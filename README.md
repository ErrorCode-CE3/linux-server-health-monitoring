# Linux Server Health Monitoring


## Objective 
Automate basic Linux server health monitoring using Python.


## Environment
- Ubuntu Server
- VirtualBox
- Python 3
- psutil library


## Metrics Monitored 
- CPU utilization
- RAM utilization
- Disk utilization


## Warning Thresholds
- CPU: Above 80%
- RAM: Above 85%
- Disk: Above 85%

## Testing
Used stress-ng to simulate high CPU workload 
and verified that the monitoring script
detected high CPU usage and produced the warning
