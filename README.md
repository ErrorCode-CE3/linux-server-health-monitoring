# Lab 1 Linux Server Health Monitoring


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


## Lab 2: Linux Server Performance Monitoring & Alerting

### Features
- Automated CPU, RAM, and disk usage monitoring
- Timestamped server health reports
- Persistent logging to `logs/server_health.log`
- CPU alert threshold: 80%
- RAM alert threshold: 85%
- Disk alert threshold: 85%
- Automated execution every 5 minutes using Linux cron

### Testing
- Verified normal server performance reporting
- Simulated high CPU usage using stress-ng
- Confirmed CPU threshold alerts were recorded in the log
- Verified automatic monitoring through cron

### Technologies
- Ubuntu Server
- Python 3
- psutil
- Linux cron
- Git and GitHub
