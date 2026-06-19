## Phase 1: Leveling Up Your Math Intuition
These help you practice the basic pattern: `return current_value + function(n - 1)`.

### 1. Factorial of a Number ($n!$)
* **Goal:** Multiply all numbers from $n$ down to 1.
* **Example:** `factorial(4)` $\rightarrow$ $4 \times 3 \times 2 \times 1 = 24$.

### 2. Sum of Digits
* **Goal:** Take an integer and add its digits together using `% 10` and `// 10`.
* **Example:** `sum_digits(125)` $\rightarrow$ $1 + 2 + 5 = 8$.

### 3. Power of a Number ($x^{n}$)
* **Goal:** Compute $x$ raised to the power of $n$ without using loops or `**`.
* **Example:** `power(2, 3)` $\rightarrow$ $2 \times 2 \times 2 = 8$.

---

## Phase 2: String & Array Manipulation
These teach you how to shrink data structures down by processing one element at a time.

### 4. Reverse a String
* **Goal:** Turn a string backward by taking the first letter and gluing it to the end of the rest of the reversed string.
* **Example:** `reverse("hello")` $\rightarrow$ `"olleh"`.

### 5. Count Occurrences in a List
* **Goal:** Count how many times a target item appears in an array.
* **Example:** `count_target([1, 2, 3, 2], 2)` $\rightarrow$ $2$.

### 6. Check for Palindrome
* **Goal:** Determine if a word reads the same backward and forward.
* **Example:** `is_palindrome("racecar")` $\rightarrow$ `True`.

---

## Phase 3: Multiple Recursive Calls (The "Tree" Shape)
These force your function to branch out into multiple paths, creating a true call stack tree.

### 7. Fibonacci Sequence
* **Goal:** Find the $n$-th Fibonacci number, where each number is the sum of the two preceding ones.
* **Formula:** `fib(n) = fib(n-1) + fib(n-2)`.

### 8. Climbing Stairs
* **Goal:** You are climbing a staircase with $n$ steps. You can climb 1 or 2 steps at a time. In how many distinct ways can you climb to the top?

---

## Phase 4: Head-Scratcher Classics
The ultimate tests of recursion logic.

### 9. Tower of Hanoi
* **Goal:** Move a stack of disks from one rod to another following specific rules, moving only one disk at a time.

### 10. Flatten a Nested List
* **Goal:** Take a deeply nested list and turn it into a single flat list.
* **Example:** `flatten([1, [2, 3], [[4]]])` $\rightarrow$ `[1, 2, 3, 4]`.
