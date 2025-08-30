---
layout: post
title: "Can you be a detective?"
date: 2025-08-30
---
Pigeonhole Principle

While researching how to determine if a number is "happy," I discovered some interesting mathematical insights.

A **happy number** is defined as a number that, when you repeatedly replace it with the sum of the squares of its digits, eventually reaches 1.

To check if a number is happy, you can use this algorithm:

1. Initialize a set to keep track of numbers you've seen.
2. While the current number is not 1 and hasn't been seen before:
   - Add the current number to the set.
   - Replace the current number with the sum of the squares of its digits.
3. If you reach 1, the number is happy. If you see a repeated number, it's not happy.

**Key observations:**

- For any number `n` with `d` digits, the maximum possible sum of the squares of its digits is `9² × d`.  
  For example, a 32-bit integer (up to ~2 billion, which has 10 digits) has a maximum sum of `81 × 10 = 810`.
- No matter how large the starting number, the sequence will eventually produce a value less than or equal to 810.

This leads to an important realization: the process is deterministic, and the set of possible sums is finite (at most 810 different values). From any number, there is exactly one "next" number in the sequence.

> The Pigeonhole Principle states that if you place more items (pigeons) than available spaces (pigeonholes), at least one space must contain more than one item. Mathematically, if n items are put into m containers, and n > m, then at least one container must hold more than one item. This simple but powerful counting principle is foundational for many mathematical proofs.

In this context, the numbers you encounter are the "pigeons," and the possible sums of squares of digits (maximum 810) are the "pigeonholes." Since there are only 810 possible pigeonholes but potentially many more numbers, you must eventually encounter a repeated sum, which creates a cycle.

Therefore, for any starting number, the process is guaranteed to either reach 1 (making it a happy number 🎉) or fall into a cycle that does


```
  func sumOfSquares(n int) int {
      sum := 0
      for n > 0 {
          digit := n % 10
          sum += digit * digit
          n /= 10
      }
      return sum
  }
  
  func isHappy(n int) bool {
      slow, fast := n, sumOfSquares(n)
      for {
          slow = sumOfSquares(slow)
          fast = sumOfSquares(sumOfSquares(fast))
          if slow == fast {
              break
          }
      }
      return slow == 1
  }

```