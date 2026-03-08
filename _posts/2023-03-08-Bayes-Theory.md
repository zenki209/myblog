# Bayes' Theorem --- Quick Cheat Sheet

## Core Idea

Bayes helps answer:

> If we observe **evidence B**, what is the probability that **cause A**
> is true?

Notation:

P(A\|B) = Probability of A **given** B.

------------------------------------------------------------------------

# Bayes Formula

P(A\|B) = ( P(B\|A) \* P(A) ) / P(B)

  Term   Meaning
  ------ ------------------------------------
  P(A)   Prior probability of A
  P(B    A\)
  P(B)   Evidence: probability of B overall
  P(A    B\)

------------------------------------------------------------------------

# Intuitive Visualization

Bayes is basically **filtering a group**.

1.  Start with a large population.
2.  Observe evidence **B**.
3.  Only look at cases where **B occurs**.
4.  Inside that group, measure how many are **A**.

Simplified formula:

P(A\|B) = P(A ∩ B) / P(B)

Meaning:

> Among all cases where **B happens**, how many also have **A**?

------------------------------------------------------------------------

# Example (Medical Test)

Suppose we test 1000 people.

  Condition    Test +   Test -   Total
  ------------ -------- -------- -------
  Disease      9        1        10
  No disease   99       891      990
  Total        108      892      1000

Question:

What is the probability someone **actually has the disease given a
positive test**?

P(disease \| positive)

Only look at the **positive tests (108)**.

-   9 actually have the disease

P(disease \| positive) = 9 / 108

------------------------------------------------------------------------

# How to Solve Bayes Problems

Step 1: Identify events

-   A = cause
-   B = evidence

Step 2: Find

-   P(A)
-   P(B\|A)
-   P(B)

Step 3: Apply Bayes

P(A\|B) = (P(B\|A) \* P(A)) / P(B)

------------------------------------------------------------------------

# Common Mistake

People confuse:

P(A\|B) vs P(B\|A)

Example:

  Expression   Meaning
  ------------ -----------
  P(positive   disease)
  P(disease    positive)

These are **not the same**.

------------------------------------------------------------------------

# Memory Trick

**Given B → only look at cases where B occurs.**

Then calculate the fraction that are A.

------------------------------------------------------------------------

# One-Line Summary

Posterior = (Likelihood × Prior) / Evidence