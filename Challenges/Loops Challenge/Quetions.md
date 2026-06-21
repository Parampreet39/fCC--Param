## Phase 1: Grid & Number Patterns
Mastering nested loops (for inside for) and formatting.

### 1. The Square Border
* **Goal:** Print an \(n \times n\) square made of stars, but only print the outer border (the inside should be hollow spaces).
* **Example for \(n=4\):**
```text
****
*  *
*  *
****
```

### 2. The Inverted Number Triangle
* **Goal:** Print a descending counting pattern based on rows.
* **Example for \(n=4\):**
```text
4444
333
22
1
```

### 3. Multiplication Table Matrix
* **Goal:** Generate a beautifully formatted multiplication table from \(1 \times 1\) up to \(n \times n\).

---

## Phase 2: String & Array Manipulation
Using loops to transform, filter, and track data.

### 4. Text Compressor
* **Goal:** Take a string with repeating characters and compress it using loops by counting consecutive duplicates.
* **Example:** `"AAABBC"` \(\rightarrow\) `"3A2B1C"`.

### 5. Move Zeros to the End
* **Goal:** Given a list of numbers, use a loop to move all zeros to the end of the list while maintaining the relative order of non-zero elements.
* **Example:** `[0, 1, 0, 3, 12]` \(\rightarrow\) `[1, 3, 12, 0, 0]`.

### 6. Find the Missing Number
* **Goal:** You are given a list containing \(n-1\) distinct numbers in the range from \(1\) to \(n\). Use a loop to find the one missing number.
* **Example:** `[1, 2, 4, 5, 6]` \(\rightarrow\) Missing is 3.

---

## Phase 3: Logic & Simulation
Using conditional checks inside loops to simulate rules.

### 7. FizzBuzz Custom Range
* **Goal:** Loop from 1 to \(n\). Print "Fizz" if divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if both, and the number itself if neither.

### 8. The "Collatz Conjecture" Sequence
* **Goal:** Start with a number \(n\). If it's even, divide it by 2. If it's odd, multiply by 3 and add 1. Repeat this loop until \(n\) becomes 1, and print the total number of steps it took.

---

## Phase 4: Heavy Nested Logic
The ultimate tests of loop tracking.

### 9. Pascal's Triangle
* **Goal:** Generate the first \(n\) rows of Pascal's Triangle using loops, where each number is the sum of the two directly above it.

### 10. Diamond of Numbers
* **Goal:** Combine an upright triangle and an inverted triangle to print a perfectly centered diamond of increasing and decreasing numbers.
* **Example for \(n=3\):**
```text
  1
 212
32123
 212
  1
```
