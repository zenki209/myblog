---
title: "Finding Which Process Is Using Swap on Linux"
date: 2026-08-31
tags: [linux, troubleshooting, oracle, memory]
---

`free -h` will tell you swap is in use, but it won't tell you *who's* using it. This is a quick, dependency-free way to break a system-wide swap number down to the exact PIDs responsible, using nothing but `/proc` and standard shell tools — useful on any box where you can't install `smem` or similar.

## The problem

```
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           508Gi       398Gi       6.9Gi       2.7Gi       102Gi       103Gi
Swap:           63Gi        25Gi        38Gi
```

25Gi of swap is in use. `free` stops there — it has no concept of "by whom."

## The technique

Every process in Linux reports its own swap usage in `/proc/<pid>/status`, on a line called `VmSwap`. The script below walks every PID, pulls that one field out, drops anything with zero swap, and sorts what's left:

```bash
(
printf "%-8s %-12s %-10s %s\n" PID SWAP_MB USER COMMAND

for pid in /proc/[0-9]*; do
    pid=${pid##*/}
    [ -r /proc/$pid/status ] || continue

    swap=$(awk '/^VmSwap:/ {print $2}' /proc/$pid/status)

    if [ -n "$swap" ] && [ "$swap" -gt 0 ]; then
        user=$(ps -o user= -p "$pid" 2>/dev/null)
        cmd=$(tr '\0' ' ' < /proc/$pid/cmdline 2>/dev/null)
        [ -n "$cmd" ] || cmd=$(ps -o comm= -p "$pid" 2>/dev/null)

        printf "%-8s %-12.1f %-10s %.50s\n" \
            "$pid" \
            "$(awk -v s="$swap" 'BEGIN {print s/1024}')" \
            "$user" \
            "$cmd"
    fi
done | sort -k2,2nr | head -10
)
```

Run it as root (or a user with read access to other processes' `/proc/<pid>/status`) so it isn't limited to your own processes.

## How it works

- **`for pid in /proc/[0-9]*`** — every running process gets a numbered directory under `/proc`; the glob picks out just the numeric ones, i.e. every PID on the box.
- **`[ -r /proc/$pid/status ] || continue`** — skips a PID if its status file isn't readable (it may have exited between the glob and the read, or belong to another user), so the script doesn't error out mid-run.
- **`awk '/^VmSwap:/ {print $2}'`** — this is the actual trick. `/proc/<pid>/status` has a line like `VmSwap:  467892 kB`; awk finds it and grabs the number in the second field. No other tool or permission is needed to get per-process swap.
- **`[ "$swap" -gt 0 ]`** — most processes have `VmSwap: 0 kB`; this filters those out so the loop only does the (slightly) expensive `ps` lookups for processes that actually matter.
- **`ps -o user=` / `tr '\0' ' ' < /proc/$pid/cmdline`** — once a process qualifies, look up its owner and reconstruct the full command line. `cmdline` stores arguments separated by null bytes rather than spaces, so `tr` converts them to make it readable; if `cmdline` is empty (common for kernel threads), it falls back to `ps -o comm=` for at least the process name.
- **`done | sort -k2,2nr | head -10`** — the loop only filters and prints; all the actual ranking happens once, after the loop, by piping every printed row through `sort` (numeric, reverse, on the swap-MB column) and keeping the top 10.

## Example output

```
PID      SWAP_MB      USER       COMMAND
7170     467.4        root       /opt/oracle.ahf/jre/bin/java --add-opens java.base
10809    383.6        grid       /u01/19.3.0/grid/jdk/bin/java -server -Xms30M -Xmx...
4765     277.4        root       /var/lib/pcp/pmdas/proc/pmdaproc -d 3
14947    252.6        oracle     ora_p00e_mu
14935    246.2        oracle     ora_p009_mu
14910    241.8        oracle     ora_p001_mu
14941    238.9        oracle     ora_p00c_mu
14939    238.6        oracle     ora_p00b_mu
14945    231.7        oracle     ora_p00d_mu
14933    230.8        oracle     ora_p008_mu
```

On this host, the 25Gi of swap wasn't one runaway process — it was spread across the Oracle AHF/grid Java agents (~850MB combined) plus a large number of Oracle background processes (`ora_p00x_mu`) each holding 200-250MB. That pattern (many medium consumers rather than one huge one) usually points to overall memory pressure on the instance rather than a single leaking process.

## Caveat: shared memory isn't counted here

`VmSwap` only tallies a process's private (anonymous) pages. Shared memory segments — Oracle's SGA in particular — can be swapped too, but that usage isn't attributed to any single PID by this method. That's why the sum of this list can come in a bit under the total shown by `free -h`. If the gap is large, check `ipcs -m` / SGA sizing rather than assuming the script missed a process.

## Related tools

If they're available, `smem -rs swap` or `ps_mem` do the same job with less shell scripting — this version exists for boxes where you can't install anything extra.