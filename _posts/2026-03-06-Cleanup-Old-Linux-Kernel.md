In order to check the current active Kernel we can use the **GRUBBY** command line.

First thing first , how to list installed kernel version

```bash
rpm -qa | grep kernel | sort -V
```

However , we can use grubby to get the all kernel available on your machine 

```bash
# grubby --info=ALL | grep ^kernel
kernel="/boot/vmlinuz-4.18.0-193.14.3.el8_2.x86_64"
kernel="/boot/vmlinuz-4.18.0-193.1.2.el8_2.x86_64"
kernel="/boot/vmlinuz-4.18.0-193.el8.x86_64"
kernel="/boot/vmlinuz-0-rescue-d88fa2c7ff574ae782ec8c4288de4e85"
```

Hence, you can get the list active post reboot

```bash
# grubby --default-kernel
/boot/vmlinuz-4.18.0-193.14.3.el8_2.x86_64
```

So sometime you want to change the active list kernel , so you can use the grubby command below to change the configuration

```bash

# grubby --set-default "/boot/vmlinuz-4.18.0-193.1.2.el8_2.x86_64"
The default is /boot/loader/entries/d88fa2c7ff574ae782ec8c4288de4e85-4.18.0-193.1.2.el8_2.x86_64.conf with index 1 and kernel /boot/vmlinuz-4.18.0-193.1.2.el8_2.x86_6
#verify the kernel after the change
# grubby --default-kernel
/boot/vmlinuz-4.18.0-193.1.2.el8_2.x86_64
```

After you verify that you switch to the latest kernel version, you can do 

```bash
# dnf remove --oldinstallonly --setopt installonly_limit=2 kernel
```

All of the information is copied from this website https://www.golinuxcloud.com/remove-old-kernels-rhel-centos-8/#Example-1_When_latest_kernel_is_active for learning purpose only.

All of the information is copied from this [website](https://www.golinuxcloud.com/remove-old-kernels-rhel-centos-8/#Example-1_When_latest_kernel_is_active) for learning purpose only.