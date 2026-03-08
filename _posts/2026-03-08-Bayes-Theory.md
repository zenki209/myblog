---
layout: post
title: "Bayes' Theorem — Quick Cheat Sheet"
date: 2026-03-08
categories: [AI, Bayes, Probability]
---

# Bayes' Theorem — Quick Cheat Sheet

## Core Idea

Bayes answers the question:

> If we observe **evidence B**, what is the probability that **cause A** is true?

Notation:

$$
P(A \mid B)
$$

Meaning:

> Probability that **A is true given that B has occurred**.

---

# The Formula

$$
P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}
$$

Or written in plain English:

$$
\text{Posterior} =
\frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}
$$

| Term | Name | Meaning |
|-----|------|--------|
| $P(A)$ | **Prior** | What we believe about A *before* seeing evidence |
| $P(B \mid A)$ | **Likelihood** | Probability of observing B if A is true |
| $P(B)$ | **Evidence** | Overall probability of observing B |
| $P(A \mid B)$ | **Posterior** | Updated belief about A *after* seeing B |

---

# Intuition: Filtering a Population

Bayes is essentially **filtering a population** down to relevant cases.

1. Start with a large population  
2. Observe evidence **B**  
3. Only look at cases where **B occurs**  
4. Inside that filtered group, measure how many are also **A**

Simplified form:

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

> Among all cases where **B happens**, how many also have **A**?

---

# Example 1 — Medical Test (1000 People)

Suppose we test **1000 people**.

| Condition | Positive Test | Negative Test | Total |
|-----------|---------------|---------------|-------|
| Disease | 9 | 1 | 10 |
| No disease | 99 | 891 | 990 |
| **Total** | **108** | **892** | **1000** |

### Question

What is the probability someone **actually has the disease given a positive test**?

Only look at the **108 positive tests**.

Out of those:

- **9 actually have the disease**

$$
P(\text{Disease} \mid \text{Positive}) = \frac{9}{108} \approx 0.083
$$

---

# Example 2 — Rare Disease with False Positives

A rare disease affects **2% of the population**.

Test accuracy:

- If a person **has the disease**, the test is **positive 95%** of the time.
- If a person **does not have the disease**, the test is still **positive 8%** of the time.

A person tests **positive**.

### Define Events

- $D$ = person **has the disease**
- $T$ = test **positive**

We want:

$$
P(D \mid T)
$$

### Known Probabilities

$$
P(D) = 0.02
$$

$$
P(D^c) = 0.98
$$

$$
P(T \mid D) = 0.95
$$

$$
P(T \mid D^c) = 0.08
$$

### Compute Evidence

$$
P(T) =
P(T \mid D)P(D) +
P(T \mid D^c)P(D^c)
$$

$$
P(T) =
0.95 \times 0.02 +
0.08 \times 0.98
$$

$$
P(T) = 0.019 + 0.0784 = 0.0974
$$

### Apply Bayes

$$
P(D \mid T) =
\frac{P(T \mid D)P(D)}{P(T)}
$$

$$
P(D \mid T) =
\frac{0.95 \times 0.02}{0.0974}
=
\frac{0.019}{0.0974}
\approx 0.195
$$

**Final Answer:**

The probability the person actually has the disease is about **19.5%**.
