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

| Field | What to check | Red flag |
|---|---|---|
| **load average** (1, 5, 15 min) | Compare to the core count (`nproc`). A 1-min value above the 15-min value means it's getting worse *right now* | Load well above cores. Linux load also counts processes stuck on disk I/O, so **high load ≠ high CPU** |
| **us** | CPU time in application code | High → an app is CPU-bound. Sort by CPU |
| **sy** | CPU time in the kernel | High → syscall storm, context switching, lots of small I/O |
| **wa** (iowait) | CPU idle while waiting on disk | Above ~10–20% → storage bottleneck. On EC2, often EBS throughput or IOPS limits |
| **st** (steal) | CPU time taken by the hypervisor | Sustained steal on AWS burstable instances (t2/t3) usually means CPU credits are exhausted |
| **si** | Software interrupts | High → network packet processing load |
| **avail Mem** | The real free-memory number | Low with swap in use → memory pressure. Ignore "free": Linux uses spare memory as page cache on purpose |
| **zombie** | Dead child processes | A few are harmless. A growing count means a parent process has a bug |

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

## 3. Pattern → next tool

`top` gives you the direction; a specialist tool gives you the answer.

| What `top` shows | Likely cause | Next command |
|---|---|---|
| High `us`, one process on top | Hot code path or runaway loop | `top -H -p <pid>`, then `perf top -p <pid>` or a profiler |
| High `wa`, processes in `D` state | Disk saturated | `iostat -xz 1` (check `%util`, `await`), `iotop` |
| High `st` | Noisy host or out of burst credits | CloudWatch `CPUCreditBalance`. Consider a non-burstable instance type |
| High `sy` | Syscall or context-switch storm | `vmstat 1` (the `cs` column), `pidstat -w 1`, `strace -c -p <pid>` |
| Low avail memory, swap growing | Memory leak or undersized instance | `free -m`, `dmesg -T \| grep -i oom`, watch which process's `RES` keeps growing |
| High `si` | Network load | `sar -n DEV 1`, `ss -s` |
| Everything looks fine but the app is slow | Problem is outside this host (DB, upstream, DNS, locks) | App metrics and logs, `ss -tnp`, trace the dependencies |

---

## 4. Capture evidence during an incident

`top` is live and gone once you close it. Snapshot it for the postmortem:

```bash
# One snapshot, sorted by CPU
top -b -n 1 -o %CPU | head -30

# One minute of 5-second samples
top -b -d 5 -n 12 > top_$(date +%s).log
```

---

## 5. Don't rely on `top` alone

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