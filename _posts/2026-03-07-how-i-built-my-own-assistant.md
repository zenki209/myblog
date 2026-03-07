---
layout: post
title: "How I Built My Own AI Assistant"
date: 2026-03-07
categories: [AI, Personal Assistant, Development]
---

I got an idea while reading this blog post: [Build Your Personal AI Assistant with Claude Code](https://www.ronforbes.com/blog/build-your-personal-ai-assistant-with-claude-code). I decided to build my own AI assistant and share the process of building it, along with how it evolves with Claude in this blog post series.

## Tech Stack

- **Backend**: Obsidian - as the knowledge base, it supports API and GraphQL.
- **Frontend**: Can be whatever I want, but at this stage, I use VSCode and Terminal for support.
- **LLM (Worker)**: Anthropic's Claude - as the assistant, it is a powerful language model that can understand and generate human-like text.

## Project Structure

I created the project repository with the structure shown below:

```
╭─root@LAPTOP-5LUP2IBK ~/REPO/my-Buddy  ‹main*›
╰─➤  tree
.
├── _global_instructions (Skills to import to Claude Skills)
│   └── morning.md
├── _scripts (Any scripts for the worker to use)
├── .claude/commands
├── daily-notes -> [ this is the symbolic link to the tasks folder in the Obsidian vault, where I store all my tasks and to-docs.]
├── meetings -> [ this is the symbolic link to the tasks folder in the Obsidian vault, where I store all my tasks and to-docs.]
├── my-repo
└── tasks -> [ this is the symbolic link to the tasks folder in the Obsidian vault, where I store all my tasks and to-docs.]
```

All of these will be under Git version control. My target for the next couple of days is to track my goals every day by creating tasks every morning, and I will see how much progress I can make.

## Backup and Restore

Since the project is under Git version control, and Obsidian can easily be backed up and restored:

- **Obsidian Vault**: Backed up to OneDrive
- **Repository**: Backed up to GitHub

## Why This Stack?

Obsidian serves as an excellent knowledge base because of its note-linking capabilities and extensibility. Claude provides the intelligence, while VSCode and Terminal allow for seamless development and interaction.

In future posts, I'll dive deeper into the implementation details, challenges faced, and how the assistant learns and adapts.

Stay tuned for updates!

