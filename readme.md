# Programming Assignment 3 — Highest Value Longest Common Subsequence (HVLCS)

- Blake Coppens UFID: 31056260
- Jorge Garcia UFID: 14841166

---

## Problem Summary

Given two strings A and B over a fixed alphabet where each character has a nonnegative integer value, find a common subsequence of A and B that maximizes total value. Output both the maximum value and one optimal subsequence.

---

## Repository Structure

```
Programming-Assignment-3/
    main.py         # Core HVLCS algorithm
    test.py          # generates 10 test cases, times them, plots results
    runtime_graph.png  # Generated runtime graph (from test.py)
    data/
        example.in     # example input from assignment
        example.out    # example output for example
        test01.in      # Generated test inputs (lengths 25-250)
        test01.out
        ...
        test10.in
        test10.out
    README.md
```

---

## Dependencies

- Python 3.8+
- matplotlib (only needed for test.py)


(use "pip install matplotlib" to be able to run test.py)

---

## How to Run
### Run the HVLCS solver

python main.py < data/example.in


Expected output:
9
cb


General usage:

python main.py < data/test01.in

### Run benchmarks and generate the runtime graph

python test.py

This will:
1. Generate 10 test input files (`data/test01.in` through `data/test10.in`) with string lengths 25-250.
2. Run HVLCS on each and save outputs (`data/test01.out` through `data/test10.out`).
3. Print a timing table to the console.
4. Save the runtime plot to `runtime_graph.png`.

---

## Input Format

K
x1 v1
x2 v2
...
xK vK
A
B

- K: number of characters in the alphabet
- Each of the next K lines: a character and its integer value
- A: first string
- B: second string

### Example (data/example.in)

3
a 2
b 4
c 5
aacb
caab

### Example Output (data/example.out)

9
cb

---

## Assumptions

- All characters in A and B appear in the alphabet mapping.
- Character values are nonnegative integers.
- If no common characters exist, the program prints 0 and an empty line.
- Input is read from in; output is written to out.

---

## Written Component

### Question 1: Empirical Comparison

Ten test cases were generated with strings of lengths 25, 50, 75, 100, 125, 150, 175, 200, 225, and 250 over a 6-character alphabet (a,b,c,d,e,f). Runtimes were measured using time.perf_counter() in /test.py and plotted in running_graph.png

The graph shows quadratic growth in runtime, consistent with the O(n^2) complexity of the algorithm when both strings have equal length n.

---

### Question 2: Recurrence Equation

**Definition:** Let dp[i][j] = maximum value of any common subsequence of A[1..i] and B[1..j].

**Base cases:**
dp[0][j] = 0   for all j = 0, 1, ..., |B|
dp[i][0] = 0   for all i = 0, 1, ..., |A|

An empty prefix contributes no characters, so the only common subsequence is empty with value 0.

**Recurrence (for i >= 1, j >= 1):**

There are two cases: 
- If A[i] == B[j]: dp[i][j] = max(dp[i-1][j-1] + v(A[i]), dp[i-1][j], dp[i][j-1] )

- If A[i] != B[j]: dp[i][j] = max( dp[i-1][j], dp[i][j-1] )

**Why this is correct:**

At position (i, j) we choose among three decisions:

1. **Match** A[i] with B[j] (only when A[i] == B[j]): gain v(A[i]) plus the best value over A[1..i-1] and B[1..j-1], giving dp[i-1][j-1] + v(A[i]).
2. **Skip** A[i]: best achievable is dp[i-1][j].
3. **Skip** B[j]: best achievable is dp[i][j-1].

We take the maximum over all applicable options. Every common subsequence of A[1..i] and B[1..j] either ends with a matched pair at positions (i, j) or skips one of the last characters — so the recurrence covers all cases, and is correct by induction on i + j.

---

### Question 3: Big-Oh

**Pseudocode:**

function HVLCS(A, B, values):
    n <- |A|
    m <- |B|

    dp[0..n][0..m] <- 0          // (n+1) x (m+1) table, all zeros

    for i from 1 to n:
        for j from 1 to m:
            if A[i] == B[j]:
                dp[i][j] <- max(dp[i-1][j-1] + values[A[i]],
                                dp[i-1][j],
                                dp[i][j-1])
            else:
                dp[i][j] <- max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]               // maximum value

function Reconstruct(dp, A, B, values):
    i <- |A|,  j <- |B|
    result <- empty list

    while i > 0 and j > 0:
        if A[i] == B[j] and dp[i][j] == dp[i-1][j-1] + values[A[i]]:
            prepend A[i] to result
            i <- i - 1,  j <- j - 1
        else if dp[i][j] == dp[i-1][j]:
            i <- i - 1
        else:
            j <- j - 1

    return result


**Runtime Analysis:**

- HVLCS fills an (n+1) x (m+1) table; each cell takes O(1). Total: **O(n * m)**.
- Reconstruct walks the table in at most n + m steps. Total: **O(n + m)**.
- **Overall: O(n * m)**, where n = |A| and m = |B|.

When both strings have equal length n this is **O(n^2)**.

**Space complexity:** O(n * m) for the DP table.
