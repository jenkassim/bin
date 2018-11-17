# Unix Networking Commands

# Check Services
- This command references a service by using its init script, which is stored in the `/etc/init.d` directory for Debian-based distributions and the `etc/rc.d/init.d` directory for Red Hat-based distributions.
- Some names vary depending on your distribution, for example, Apache® is httpd on CentOS® and apache2 on Ubuntu®.

```
    $ systemctl
    $ systemctl | more
    $ systemctl | grep httpd
    $ systemctl list-units --type service
    $ systemctl list-units --type mount
```
- To list all services:
```
    $ systemctl list-unit-files
```

## List SysV services only on RedHat
```
    $ chkconfig --list
```

## Find port conflicts
- Checks for active Internet connections, without option, will list out all connections
```
    $ netstat -plnt
```
# System Load checks

## top
The top command displays real time information regarding the server’s resource usage. The first few lines will give you a summary of the resource utilisation on your system and you can sort the list of processes by CPU (P) or memory (M) use which allows you to quickly see where your server is receiving the biggest demands on its resources.

## vmstat
The amount of memory a system has is one of the most common restraining factors. The swap is an area of the hard drive where data is moved to free up physical memory (RAM) for a process to use (not all servers have swap space configured). A system using its swap area does not necessarily mean it is low on memory, but if most of your system’s swap is being consumed it could indicate that your server is trying to do more than its available memory permits.

If swap space is configured and you suspect your server is running out of standard memory, you can use vmstat to show how much swapping is occurring.


# System Log
- `/var/log/cron`
When crondaemon or anacron starts a cron job the information the information about the cron job is stored here.

- `/var/log/dmesg`
Contains Kernel information about hardware and devices detected during the boot process. This file is overwritten when new messages are sent to it. Example: the next boot.

- `/var/log/maillog.log`
Information from the mail server that is running on your system. Example Sendmail logging information.

- `/var/log/messages`
Contains global system messages, including the messages logged during boot. Several things are logged in this file including mail, cron, daemon, kern, auth, etc.

- `/var/log/sa`
Contains daily sar files collected by sysstat package.

- `/var/log/samba/`
 Contains log information stored by samba daemon. Used to connect to windows/linux filesystems.

- `/var/log/setroubleshoot/`
SELinux uses setroubleshootd (SE Trouble Shoot Daemon) to notify about issues in the security context of files, and logs those information in this log file.

- `/var/log/secure`
Information related to Authentication and authorization privileges. Exmample sshd logs all information here including unsuccessful attempts.

- `/var/log/yum.log`
Information that is logged when a package is installed or removed is stored here.




# References
- https://fedoraproject.org/wiki/SysVinit_to_Systemd_Cheatsheet
- https://docs.fedoraproject.org/en-US/quick-docs/understanding-and-administering-systemd/index.html

