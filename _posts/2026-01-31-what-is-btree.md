---
layout: post
title: "What is B-Tree?"
date: 2026-01-31
tags: [programming, data-structures, btree]
---
# B-Tree

## Overview

A B-Tree is a self-balancing search tree built on nodes and leaves. The fundamental rule is: all values in the left subtree are smaller than the root, and all values in the right subtree are larger. All leaf levels maintain the same height.

## Insert Operation

When inserting a value, we traverse from the root node to find the correct position at the bottom level.

**Node Splitting:**
If a node already contains the maximum number of elements, it splits into two nodes:
- Left node: contains smaller elements (size: max/2)
- Right node: contains larger elements (size: max/2)
- Middle element: promotes to the parent node as a new separator

## Delete Operation

To delete a key, we traverse from the root through all nodes to locate the target value.

**Handling Underflow:**
If deleting a key leaves a node with fewer than the minimum required keys, we must rebalance:
- Borrow a key from a sibling node (left or right)
- Move the separator key from the parent down to the deficient node
- Move the sibling's key up to the parent

This maintains the B-Tree properties and balances.B-Tree

Build base on node and leaf. There is a rule the left value is smaller than the root and the right is bigger Or we can think the right always than the left

## References

- [Understanding B-Trees: The Data Structure Behind Modern Databases](https://www.youtube.com/watch?v=K1a2Bk8NrYQ)