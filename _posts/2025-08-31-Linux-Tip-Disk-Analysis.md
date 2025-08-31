---
layout: post
title: "Linux Tip: Disk Analysis"
date: 2025-08-31
---

One of the most common things when working with the OS is disk analysis. Understanding disk usage can help you manage your system more effectively.

Below is a step-by-step guide to disk analysis:

- **Analyze all mount points:**  
  Run the following command to see disk usage for all mount points in human-readable format, sorted by size:
  ```
  df -h | sort -h
  ```

- **Analyze disk usage with limited depth:**  
  To see disk usage for directories under `/` up to two levels deep:
  ```
  du -xh --max-depth=2 /
  ```

- **Drill down into specific directories:**  
  Focus your analysis on a particular directory to find large files or subdirectories:
  ```
  du -xh --max-depth=2 /path/to/directory
  ```

- **Take action:**  
  Once you identify which directories are using the most space, you can:
  - Delete unnecessary files
  - Move files to another location
  - Archive old data

Disk analysis is an essential part of system maintenance and can help prevent issues related to disk space exhaustion. Regularly performing disk analysis ensures that your system remains healthy, efficient, and responsive.