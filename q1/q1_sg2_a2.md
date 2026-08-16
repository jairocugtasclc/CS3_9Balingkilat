## **Annex C** <br> **Code Quality Assessment Form**

| Names | Info |
| ----------- | ----------- |
| #10 - Cugtas, Jairo Vincent M.	     | 08/16/26 |
| #11 - Felera, Nathaniel Philip D.		 | CS3 - ILA |
| #12 - Perez, Lloydrie A.			       | 9 - Balingkilat |
				                                                                      	
---

Instructions:
The problem: Finding the highest (Maximum) number from a given list of numbers.

### 1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?
- The first algorithm is faster for large lists of numbers. This algorithm works by taking the first number as the current max and updating if it finds a larger number until the final maximum is found. For the second algorithm, it compares every number to all other numbers until it finds the biggest one. In the end, the first algorithm is more efficient as it checks all each number just once rather than comparing them to every other.

### 2. Readability
Which algorithm is easier to understand at first glance? What makes it clearer?
- The first algorithm is significantly easier to understand. The logic of updating when you find a bigger number is simple to follow, it only tracks the variable max and one loop counter, and is one straight loop. In contrast, the second algorithm has a complicated “brute force” approach, nested loops, multiple conditional checks, and two loop counters.

### 3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?
- The 1st algorithm is much easier to update. Because it uses a single loop, adding a feature like finding the min value only requires initializing a min variable alongside a max and adding an extra if condition inside the existing loop.

### 4. Testability
Which algorithm is easier to test with different inputs? Why?
- The 1st algorithm is much easier to test because it steps through the list just once,  making its output clear and easy to predict.

### 5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?
- Since both pseudocodes would crash in the case that the user inputs anything that is not a number, either pseudocode should be updated so that only integer and float variables are accepted into the list. Additionally the program should require at least one input, because nothing can be compared in an empty list.

### 6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer
- Even though both algorithms are currently unable to compare letters/unusual characters, the first algorithm would be better to use. The first algorithm checks the largest number in one go, whereas the second would have to check every single number against every other number. Additionally, the first algorithm is slightly easier to update if an error occurs, since it is shorter, and there are less dependent lines of code.




