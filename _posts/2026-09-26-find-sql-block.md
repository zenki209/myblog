---
layout: post
title: "The DBA as Detective: Troubleshooting Locking and Blocking in SQL Server"
date: 2026-09-26
categories: [databases, sql-server]
tags: [sql-server, dba, locking, blocking, performance, troubleshooting]
---

![A developer investigating a database issue]({{ '/_images/sql-locking-blocking-header.jpg' | relative_url }})

Locking is not a bug. SQL Server locks rows, pages, and tables constantly so that concurrent transactions don't corrupt each other's data. The problem starts when one session holds a lock long enough that everyone behind it has to wait. That's blocking, and left alone it can freeze an entire application.

Finding the root cause is detective work: follow the clues from "something is slow" down to the one session actually holding the lock, then decide what to do about it.

## Step 1: Find who is blocking whom

`sp_who2` is the fastest way to get a first read on the situation:

```sql
EXEC sp_who2;
```

The column that matters is `BlkBy`. Any non-zero value there means that SPID is waiting on another session. Read `BlkBy` as an arrow pointing at the real culprit — SPID 62 might show `BlkBy = 61`, and SPID 63 might show `BlkBy = 62`. Chains like this are common: killing SPID 61 releases everyone behind it.

![A blocking chain, as sp_who2 would surface it]({{ '/_images/sql-blocking-chain.svg' | relative_url }})

## Step 2: Find out what the blocker is running

Knowing the SPID isn't enough — you need to know what it's actually executing. `DBCC INPUTBUFFER` returns the last statement sent by a given session:

```sql
DBCC INPUTBUFFER(61);
```

The grid output is fine for a quick look, but switch to text output (`Ctrl+T` in SSMS) when the query is long — it's far easier to read a multi-line batch as plain text than squeezed into a grid cell.

## Step 3: Inspect the locks it's holding

Once you know *who*, look at *what*. `sp_lock` lists every lock a session holds, its type, and its mode:

```sql
EXEC sp_lock 61;
```

Two things matter in the output: the resource type and the mode.

**Resource types** — what's being locked:

| Type | Meaning |
|------|---------|
| RID  | A single row |
| KEY  | A key range in an index |
| PAG  | A data or index page |
| EXT  | An extent (a group of pages) |
| TAB  | An entire table |
| DB   | The whole database |

**Lock modes** — how it's being locked:

| Mode | Meaning |
|------|---------|
| S    | Shared (read) |
| U    | Update |
| X    | Exclusive (write) |
| IS / IU / IX | Intent shared / update / exclusive |
| BU   | Bulk update |

A session holding dozens of locks, or an `X` lock at the `TAB` level instead of `RID`, is a strong signal that something is wrong — usually a missing index forcing a scan, or a transaction that never committed.

## Step 4: Decide whether to kill it

If the blocking session is clearly stuck — a forgotten `BEGIN TRAN` left open, or a runaway query — end it:

```sql
KILL 61;
```

A kill isn't instant; SQL Server has to roll back everything the transaction touched. Check progress with:

```sql
KILL 61 WITH STATUSONLY;
```

One trap: if the session called `xp_cmdshell` and is waiting on an external process, `KILL` alone won't free it. You have to terminate the external process first — SQL Server can't roll back work it handed off to the OS.

## Step 5: Automate the detective work

Once you've done this manually a few times, wrap it into one query that shows blockers, what they're blocked by, and what they're running, all at once:

```sql
SELECT
    r.session_id,
    r.blocking_session_id,
    r.wait_type,
    r.wait_time,
    r.status,
    t.text AS running_query
FROM sys.dm_exec_requests r
CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t
WHERE r.blocking_session_id <> 0
   OR r.session_id IN (
        SELECT blocking_session_id
        FROM sys.dm_exec_requests
        WHERE blocking_session_id <> 0
     );
```

This is the modern, DMV-based equivalent of chaining `sp_who2`, `DBCC INPUTBUFFER`, and `sp_lock` by hand. Package it as a stored procedure and you have a single script to drop onto any server when things get slow.

## Warning signs to watch for

- A single SPID holding 50+ locks.
- An `X` lock at the table level held for more than a few seconds.
- A transaction that calls out to an external process (`xp_cmdshell`) before committing.
- A loop that takes explicit locking hints (`WITH (TABLOCKX)`, `HOLDLOCK`) around anything slow.

## Summary

Blocking investigations follow a fixed path: find the blocker (`sp_who2`), find its query (`DBCC INPUTBUFFER`), find its locks (`sp_lock`), then decide whether to wait it out or `KILL` it. Once the pattern is familiar, replace the manual steps with one DMV query and spend the saved time preventing the next incident — usually by adding the index the blocker was missing in the first place.

Reference: [The DBA as Detective: Troubleshooting Locking and Blocking](https://www.red-gate.com/simple-talk/databases/sql-server/database-administration-sql-server/the-dba-as-detective-troubleshooting-locking-and-blocking/)
