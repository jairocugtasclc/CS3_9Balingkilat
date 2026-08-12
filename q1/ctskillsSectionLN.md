## **Annex A** <br> **Computational Thinking Exercise: "Smart School Canteen Queue"**

| Names | Info |
| ----------- | ----------- |
| #10 - Cugtas, Jairo Vincent M.	     | 08/13/26 |
| #11 - Felera, Nathaniel Philip D.		 | CS3 - ILA |
| #12 - Perez, Lloydrie A.			       | 9 - Balingkilat |
				                                                                      	

_____________________________________________________________________________________________________________________________

Scenario
The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

- Some students take too long to decide what to order.
- The cashier has to manually calculate totals and give change.
- There is no system to track which food items are running out.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

_____________________________________________________________________________________________________________________________

### **Step 1: Identify the Big Problem**

Main Problem: Inefficient and slow canteen transaction processes during peak lunch hours, causing severe congestion and long waiting times.

### **Step 2: Identify three to four Sub-Problems**

Please list possible sub-problems:
1. Long waiting times due to students taking too long to decide what to order, which heavily affects the queue.
2. Manual, error-prone checkout process by the cashier, having to calculate totals, process payments, and identifying change.
3. Absence of an automated system to monitor food stock in real time, making it difficult to manage food preparation and anticipate when items will run out. 
4. The lack of pre-ordering or digital management, forcing students to physically wait inside the small canteen space.

### **Step 3: Define Computational Thinking Approaches**
For each sub-problem, apply CT skills: 

| Sub-Problem | CT Skill | Example Solution |
| ----------- | ----------- | ----------- |
| 1 | Pattern Recognition | Make a pre ordering system that shows current and future menus. |
| 2	| Algorithm | Make an automated system that calculates the payments swiftly. |
| 3	| Algorithm | Make a real time inventory management system that deducts used products when pre orders are made and alerts staff when stock is low. |
| 4 | Abstraction | Create an app for pre-ordering. |

### **Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem**

START:
	Makes an empty list
	Asks the user if they will make the menu or will be the one pre-ordering

	If answer is former:
		Asks the user how many non-repeating food items are in the menu
		For i in range(no. of items), asks the user the names of the food items, its prices, and the quantity of it still available then appends it in the empty list
		Prints the current list 
		Asks the user if they would like to make a future menu
		If answer is yes, repeats the process on a new empty list
		If answer is no, ends the program

	If answer is latter:
		Displays the list (menu) made by the menu maker
		Asks the user the number of items they will pre-order
		For i in range(no. of items to pre-order), Asks the user which items they will buy and appends it in an empty list
		If desired no. of a specific item is greater than the current quantity of it in the menu, declines the order and asks the user to change their order
		Reduces the quantity of items by 1 for every time it was pre-ordered
		Calculates and prints the sum of the prices from the items that the user pre-ordered
		Asks the user their way of payment (Cash, Online, etc.)
END
