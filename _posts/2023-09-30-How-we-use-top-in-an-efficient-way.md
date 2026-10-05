---
title: "How SREs Actually Use top to Troubleshoot Linux Systems"
date: 2026-09-30
tags: [sre, linux, troubleshooting, performance, aws, ec2]
description: "Read the header first, sort the process list second, and let top point you to the next tool."
---

# How SREs Actually Use `top` to Troubleshoot Linux Systems

Most people open `top` and stare at the process list. Experienced SREs spend the first 30 seconds on the **summary header** instead. The header tells you *what kind* of problem you have. That tells you which process column to sort by and which tool to open next.

Here's the workflow.

---

## 1. Read the header first

```text
top - 10:42:01 up 12 days,  load average: 7.85, 6.10, 3.02
Tasks: 213 total,   3 running, 210 sleeping,   0 stopped,   1 zombie
%Cpu(s): 22.1 us, 4.3 sy, 0.0 ni, 38.0 id, 30.2 wa, 0.0 hi, 1.1 si, 4.3 st
MiB Mem :  7820 total,   210 free,  6100 used,  1510 buff/cache
MiB Swap:     0 total,     0 free,     0 used.   1180 avail Mem
```

| Red flag in `top` | What it suggests | Next action |
|---|---|---|
| Load above the core count (`nproc`), especially if the 1-min value is rising | CPU contention or tasks blocked on I/O; Linux load includes processes in uninterruptible sleep, so **high load ≠ high CPU** | Compare `us`, `wa`, and `%id`; if CPU is idle while load is high, look for processes in `D` state |
| High `us`, or one process dominates CPU | Application code is CPU-bound, possibly in one hot thread | Sort by CPU (`P`); inspect threads with `top -H -p <pid>`, then profile with `perf top -p <pid>` |
| High `sy` | Kernel work, syscall volume, or context switching | Check `vmstat 1` (`cs`), `pidstat -w 1`, then `strace -c -p <pid>` on a suspect process |
| Sustained `wa` above ~10–20%, especially with processes in `D` state | Storage bottleneck; on EC2, check EBS throughput or IOPS limits | Run `iostat -xz 1` (`%util`, `await`) and `iotop` |
| Sustained high `st` | Hypervisor contention; on burstable EC2, CPU credits may be exhausted | Check CloudWatch `CPUCreditBalance`; consider a non-burstable instance if credits are depleted |
| High `si` | Software-interrupt load, often network packet processing | Check interface traffic with `sar -n DEV 1` and socket counts with `ss -s` |
| Low `avail Mem` with swap in use or growing | Memory pressure or a leak; ignore `free`, since Linux uses spare memory as page cache | Sort by memory (`M`), watch process `RES`, and check `free -m` plus `dmesg -T \| grep -i oom` |
| Growing zombie count | A parent process may not be reaping child processes; a few zombies are harmless | Find a zombie's parent PID with `ps -o ppid= -p <zombie-pid>`, then inspect that parent |
| Host signals look normal but the app is slow | The bottleneck may be outside this machine (DB, upstream, DNS, or locks) | Check app metrics and logs, inspect connections with `ss -tnp`, and trace dependencies |

> **Example:** In the header above, load is high but the CPU is 38% idle, and `wa` is 30%. That's a **disk** problem, not a CPU problem. You can make that call before looking at a single process.

---

## 2. Then work the process list with the right sort

### Interactive keys worth memorizing

| Key | Action |
|---|---|
| `1` | Show each CPU core. Finds one core pinned at 100% by a single-threaded process while the average looks fine |
| `P` / `M` / `T` | Sort by CPU / memory / total CPU time |
| `c` | Show the full command line (which Java or Python process is it?) |
| `H` | Show threads, to find the one runaway thread |
| `u` | Filter by user |
| `o` | Filter, e.g. `COMMAND=nginx` or `%CPU>5` |
| `k` | Kill a PID (be careful) |
| `W` | Save your layout to `~/.toprc` |

### Columns that matter

- **S (state):** `R` = running, `S` = sleeping, `D` = uninterruptible sleep, usually stuck on I/O. Many `D` processes explain high load with an idle CPU.
- **RES vs VIRT:** `RES` is real physical memory. `VIRT` is usually misleading, especially for Java and Go.
- **%CPU over 100%** is normal for a multi-threaded process (400% = 4 cores busy).

---

## 3. Capture evidence during an incident

`top` is live and gone once you close it. Snapshot it for the postmortem:

```bash
# One snapshot, sorted by CPU
top -b -n 1 -o %CPU | head -30

# One minute of 5-second samples
top -b -d 5 -n 12 > top_$(date +%s).log
```

---

## 4. Don't rely on `top` alone

`top` only shows the present, on one box. The same signals can be collected and kept over time with any Prometheus-compatible stack (for example Grafana Alloy → VictoriaMetrics/Prometheus → Grafana). These node exporter metrics match the header:

| `top` field | Node exporter metric |
|---|---|
| load average | `node_load1`, `node_load5`, `node_load15` |
| wa | `node_cpu_seconds_total{mode="iowait"}` |
| st | `node_cpu_seconds_total{mode="steal"}` |
| avail Mem | `node_memory_MemAvailable_bytes` |

Put these on a dashboard and alert on them, especially **steal** and **iowait** on cloud VMs. Then you usually know it's a disk problem before you even SSH in, and `top` just confirms which process is responsible.

**On Windows?** The equivalents are Resource Monitor or `Get-Counter` with `\Processor(_Total)\% Processor Time`, `\PhysicalDisk(*)\Avg. Disk sec/Read`, and `\Memory\Available MBytes`.

---

## TIPS

1. **Header first:** load vs cores, then the CPU breakdown (`us`/`sy`/`wa`/`st`), then `avail Mem`.
2. **Classify the problem:** CPU, disk, memory, kernel, network, or "not this box".
3. **Sort the process list** to match the problem (`P`, `M`, `1`, `H`).
4. **Switch to the specialist tool** (`iostat`, `perf`, `vmstat`, `ss`).
5. **Snapshot with `top -b`** for the postmortem, and **graph the same metrics** so next time you see it coming.