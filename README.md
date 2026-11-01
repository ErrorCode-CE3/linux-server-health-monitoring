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

## Lab 3: Linux Server Administration & Security

### Objective

Develop practical Linux system administration skills by managing users, groups, file permissions, SSH security, system services, time synchronization, and automated backups.

### Environment

- Ubuntu Server
- Oracle VirtualBox
- Windows PowerShell (SSH client)
- Git and GitHub

### User and Group Management

- Created administrative group `sysadmins`.
- Added primary administrator `grits` to the group.
- Created secondary account `labuser`.
- Assigned `labuser` to the `sysadmins` group.
- Verified group membership and account permissions.

### File Permissions and ACLs

- Created shared administrative directory: `/opt/sysadmin-share`.
- Configured ownership as `root:sysadmins`.
- Applied directory permissions `2770`.
- Enabled Setgid inheritance.
- Configured default Access Control Lists (ACLs).
- Tested shared file creation and group access.

### SSH Security Hardening

- Configured SSH public-key authentication.
- Disabled password-based SSH authentication.
- Disabled direct root login.
- Validated SSH configuration.
- Tested passwordless authentication from Windows PowerShell.
- Configured a new Ubuntu SSH key for GitHub authentication.

### System Administration

- Updated Ubuntu packages.
- Installed Linux administration utilities.
- Inspected disk partitions and LVM storage.
- Reviewed filesystem mounts.
- Inspected running system services.
- Reviewed system and SSH logs.
- Verified SSH service operation.

### Time Synchronization

- Verified NTP synchronization using `timedatectl`.
- Used `chronyc tracking` to inspect synchronization status.
- Confirmed active NTP service and synchronized system clock.

### Automated Backup and Recovery

- Created Bash backup script: `/usr/local/bin/backup-sysadmin.sh`.
- Configured backup destination: `/var/backups/sysadmin/`.
- Generated timestamped compressed `.tar.gz` archives.
- Executed backup script successfully.
- Tested archive extraction into a temporary recovery directory.

### Logging

- Created `/var/log/sysadmin/lab3.log`.
- Recorded administrative activities and Lab 3 completion details.

### Git and GitHub

- Worked on branch `lab-3-linux-administration`.
- Configured Git identity.
- Created completion commit `08620f0`.
- Generated and registered an Ubuntu SSH key with GitHub.
- Successfully pushed the Lab 3 branch to the remote repository.

### Technologies

- Ubuntu Server
- Bash scripting
- Linux ACLs
- OpenSSH
- systemd
- chrony / NTP
- tar and gzip
- LVM
- Git and GitHub

### Skills Demonstrated

- Linux user and group administration
- File permission management
- SSH security configuration
- System service and log inspection
- Time synchronization
- Backup automation and recovery
- Git version control
- Linux troubleshooting

**Lab Status:** Core administration exercises completed; final verification of the cron schedule and Python monitoring dependency remains.
