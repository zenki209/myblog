---
layout: post
title: "What is SUDO?"
date: 2025-12-21
tags: [linux, security, sudo]
---


# What is SUDO?

The sudo command allows users to perform tasks with higher privileges while logging their actions for security.

## Why Use SUDO?

- **Run commands as another user** (especially root) without logging out
- **Log all activity** to track admin actions for security auditing
- **Control access** through the `/etc/sudoers` file, ensuring users only have the permissions they need

### 1. Run Commands as Another User

Sudo allows users to execute commands with the privileges of another user, typically the root user, without needing to switch users or log out. This is particularly useful for performing administrative tasks.

```bash
sudo -u sample_user whoami
```

### 2. Run Commands as Root

Many system-level tasks require root privileges. Sudo enables users to run these commands safely without giving them full root access.

```bash
sudo cat /etc/shadow
```

## Understanding the /etc/sudoers File

The `/etc/sudoers` file controls who can use sudo and what commands they can run. It is essential to configure this file correctly to maintain system security.

### Default Permission

```bash
-r--r----- 1 root root 440 /etc/sudoers  # Main configuration file of sudo
```

### Default /etc/sudoers File Content

```bash
Defaults    env_reset
Defaults    mail_badpass
Defaults    secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# Allow root to run any commands anywhere
root    ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL

# Allow members of group wheel to execute any command (common on RHEL/CentOS)
%wheel  ALL=(ALL) ALL
```

### Syntax

```bash
user  host=(runas_user) command
```

### Examples

```bash
# Root user with full permissions (any host, any user, any command)
root   ALL=(ALL) ALL

# User infosec allowed to act as armour group (any host, any command)
infosec   ALL=(armour) ALL

# User infosec allowed to run /usr/bin/ls command as armour group (any host)
infosec   ALL=(armour) /usr/bin/ls

# User infosec allowed to run /usr/bin/top as armour group only on HOSTNAME1 (specific host)
infosec   HOSTNAME1=(armour) /usr/bin/top

# User warrior allowed to run /usr/sbin/fdisk as armour group and EMP user (any host)
warrior   ALL=(armour:EMP) /usr/sbin/fdisk
```

## References

- [Understanding sudo in Linux: A Practical Guide](https://medium.com/@Jitendrasinghsisodiyaa/understanding-sudo-in-linux-a-practical-guide-e19b5b767c16)