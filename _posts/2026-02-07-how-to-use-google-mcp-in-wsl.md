---
title: How to Use Google MCP in WSL
author: jkelly blog
date: 2026-02-07
categories: [WSL, MCP, Chrome DevTools]
tags: [tutorial, windows, wsl, claude]
---

# How to Use Google MCP in WSL

By default, Google MCP is not supported in WSL, but with a few tweaks you can get it working. Here's how:

## Installation Steps

### 1. Add Chrome DevTools MCP

Run the following command:

```
claude mcp add-json chrome-devtools '{"type":"stdio","command":"cmd.exe","args":["/c", "npx", "-y", "chrome-devtools-mcp@latest","--isolated", "true", "--chrome-arg=--disable-extensions", "--chrome-arg=--no-first-run"],"env":{}}'
```

### 2. Verify the Installation

Check that the MCP was installed correctly:

```
claude mcp list
```

### 3. Test in Claude Code

Before testing, close all Chrome windows and start Chrome with remote debugging enabled on port 9222:

```
chrome --remote-debugging-port=9222 --user-data-dir=remote-profile
```

Open Claude and try to browse any website. Chrome should be running in the background, and you should be able to see the website content in Claude Code.

---


