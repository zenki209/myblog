---
layout: post
title: "Bayes' Theorem --- Quick Cheat Sheet"
date: 2026-03-08
tags: [programming, search, data engineer, bayes, probability]
---
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

  
| Condition | Positive Test | Negative Test | Total |  
|---------------|---------------|---------------|-------|  
| Disease | 9 | 1 | 10 |  
| No disease | 99 | 891 | 990 |  
| **Total** | **108** | **892** | **1000** |

Question:

What is the probability someone **actually has the disease given a
positive test**?

P(disease \| positive)

Only look at the **positive tests (108)**.

-   9 actually have the disease

$$  
P(\text{disease}|\text{positive}) = \frac{9}{108}  
$$
------------------------------------------------------------------------

# How to Solve This Problems

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

##  What is Bayes ?

$$
\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}
$$

Bayes updates what we believe about a **cause** after seeing some **evidence**.

---

### Using the Medical Test Example

| Condition | Positive Test | Negative Test | Total |
|---|---|---|---|
| Disease | 9 | 1 | 10 |
| No disease | 99 | 891 | 990 |
| **Total** | **108** | **892** | **1000** |

We want to compute:

$$
P(\text{Disease}|\text{Positive})
$$

---

## Prior

**Prior** = what we believe *before seeing the test result*.

In the population:

- 10 people out of 1000 have the disease

$$
P(\text{Disease}) = \frac{10}{1000} = 0.01
$$

Meaning: before testing, there is a **1% chance** someone has the disease.

---

## Likelihood

**Likelihood** = how likely the evidence is **if the cause is true**.

Among the 10 people who actually have the disease:

- 9 test positive

$$
P(\text{Positive}|\text{Disease}) = \frac{9}{10} = 0.9
$$

Meaning: if someone **really has the disease**, the test detects it **90% of the time**.

---

## Evidence

**Evidence** = how often the evidence appears overall.

In the entire population:

- 108 people test positive

$$
P(\text{Positive}) = \frac{108}{1000} = 0.108
$$

This includes:

- 9 true positives
- 99 false positives

---

## Posterior

**Posterior** = the updated probability **after seeing the evidence**.

Among all **108 positive tests**:

- only 9 actually have the disease

$$
P(\text{Disease}|\text{Positive}) = \frac{9}{108} \approx 0.083
$$

Meaning:

> If someone tests positive, the probability they actually have the disease is about **8.3%**.

---

## Intuition

Even though the test is **90% accurate**, the disease is **very rare (1%)**.

So most positive results come from **false positives**, not real cases.

This is why:

$$
P(\text{Disease}|\text{Positive}) \neq P(\text{Positive}|\text{Disease})
$$
