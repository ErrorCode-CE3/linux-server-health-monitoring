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

## Lab 4: Linux Networking & Troubleshooting

### Objective

Build practical Linux networking troubleshooting skills by inspecting interface configuration, routing, DNS, connectivity, link status, packet counters, system logs, and DHCP behavior. Practice controlled network failure and recovery.

### Environment

- Ubuntu Server running in Oracle VirtualBox
- VirtualBox NAT networking
- Interface: `enp0s3`
- Network manager: `systemd-networkd` (Netplan-generated configuration)
- Virtual NIC: Intel E1000 emulation

### Network Configuration

- IPv4 address: `10.0.2.15/24` (DHCP)
- Default gateway: `10.0.2.2`
- DNS server: `10.0.2.3`
- Local DNS stub resolver: `127.0.0.53`
- MTU: `1500`
- Reported link: `1 Gbps, full duplex`

### Connectivity and Routing

- Inspected interface addresses using `ip`.
- Reviewed the routing table and default gateway using `ip route`.
- Tested gateway and external IP reachability with `ping`.
- Confirmed external HTTPS connectivity using `curl -I`.
- Used `tracepath` to inspect the route toward an external IP; the VirtualBox gateway responded, while later hops did not reply.
- Resolved external hostnames successfully.

### DNS Troubleshooting

- Inspected resolver configuration using `resolvectl` and `/etc/resolv.conf`.
- Verified that `systemd-resolved` was active and using the VirtualBox-provided DNS server.
- Queried DNS with `getent` and `dig`.
- Simulated a DNS outage by temporarily assigning an unreachable test resolver to `enp0s3`.
- Confirmed that DNS lookups stalled while direct IP connectivity remained available.
- Restored the original per-link DNS configuration with `resolvectl revert` and verified name resolution and HTTPS access.

### Interface and Link Diagnostics

- Inspected interface state, MAC address, MTU, and packet counters using `ip -s link`.
- Used `ethtool` to inspect link detection, speed, duplex, and auto-negotiation.
- Confirmed the interface reported `UP` and `LOWER_UP`, with zero RX/TX errors and drops at the time of inspection.
- Reviewed kernel messages with `journalctl -k`.

### DHCP and Recovery

- Identified `systemd-networkd` as the network manager handling the interface.
- Inspected DHCP-provided address, gateway, and DNS settings with `networkctl status`.
- Reviewed network logs and observed a link-down event, carrier loss, DHCP lease loss, and subsequent link recovery with DHCP address reacquisition.
- Renewed the DHCP configuration using `networkctl renew enp0s3`.
- Verified that the interface retained its dynamic IPv4 configuration.

### Troubleshooting and Recovery Lessons

- Disabling the active network interface interrupted the SSH session, demonstrating the need for console or out-of-band access before disruptive remote changes.
- Distinguished DNS resolution failure from loss of IP connectivity.
- Reviewed APIPA (`169.254.0.0/16`) as an indicator that a client may have failed to obtain a DHCPv4 lease.
- Practiced a troubleshooting sequence covering link state, VLAN/L2 connectivity, DHCP service and scope, and DHCP relay where applicable.

### Technologies and Commands

- Ubuntu Server
- Netplan and systemd-networkd
- systemd-resolved
- DHCP, IPv4, IPv6, DNS
- `ip`, `networkctl`, `resolvectl`, `ethtool`
- `ping`, `tracepath`, `dig`, `getent`, `curl`
- `journalctl`
- VirtualBox NAT networking

### Skills Demonstrated

- Linux network configuration inspection
- IP addressing and routing analysis
- DNS troubleshooting and recovery
- DHCP configuration inspection and renewal
- Network interface and link diagnostics
- Packet counter and system log analysis
- Remote-access risk awareness and recovery planning

**Lab Status:** Networking diagnostics, controlled DNS failure/recovery, interface recovery, and DHCP renewal exercises completed. Final connectivity verification passed.
