---
layout: post
title: "Reset Proxmox Password (GRUB single-user)"
date: 2025-10-18
tags: [proxmox, recovery, sysadmin]
---

Use this procedure to reset a root/user password on a Proxmox (or other Linux) host by booting into a minimal shell from GRUB. Only perform this on systems you own or are authorized to manage.

## Warning
- If GRUB is password-protected you cannot edit the boot entry; use rescue media instead.  
- If the disk is encrypted (LUKS), you will be asked for the passphrase early in boot and this method will not bypass it.  
- Resetting passwords this way gives full system access — treat carefully.

## Steps

1. Reboot the machine and enter the GRUB menu
   - On BIOS systems hold Shift during boot; on UEFI press Esc (or the vendor-specific key).
   - In the GRUB menu, highlight the kernel entry you normally boot and press `e` to edit.

2. Edit the kernel command line
   - Find the line that begins with `linux` (e.g. `linux /boot/vmlinuz-...`).
   - Go to the end of that `linux ...` line, add a single space, then append:
     ```
     init=/bin/bash
     ```
   - Boot the edited entry (usually `Ctrl+X` or `F10`).

3. Remount the root filesystem read/write
   - After the kernel drops you into a shell, remount root rw:
     ```sh
     mount -o remount,rw /
     ```
   - Verify you can write, e.g. `touch /tmp/test && rm /tmp/test`

4. Reset the password
   - To change root:
     ```sh
     passwd root
     ```
     or to change a specific user:
     ```sh
     passwd <username>
     ```
   - Enter and confirm the new password. `passwd` will update /etc/shadow.

5. Finish and reboot cleanly
   - Recommended: re-exec the normal init to continue booting:
     ```sh
     exec /sbin/init
     ```
     If that fails, sync and force a reboot:
     ```sh
     sync
     reboot -f
     ```
   - Optionally remount read-only before reboot:
     ```sh
     mount -o remount,ro /
     sync
     reboot -f
     ```

## Troubleshooting & notes
- If `exec /sbin/init` returns "No such file", try `exec /usr/lib/systemd/systemd` or use the forced reboot commands above.
- If GRUB editing is blocked (GRUB password) or the system uses disk encryption, use a rescue ISO/USB to mount the disk and `chroot` to reset passwords.
- Proxmox web UI typically authenticates as `root` — resetting `root` restores access to the web console.
- After recovery, review `/var/log/auth.log` and consider rotating keys/passwords as needed.

## Security reminder
Resetting passwords this way can bypass normal login controls. After recovery, secure the host (update passwords, audit accounts, consider enabling GRUB password or disk encryption).