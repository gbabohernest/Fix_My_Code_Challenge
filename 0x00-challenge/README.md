## Debugging

### Synopsis

```Fix my code``` is a type of project where we'll jump into an exisiting code base and fix it!

### Tasks

**0. FizzBuzz**

```15``` should print ```FizzBuzz``` not ```Fizz```
FIZZBUZZ was not being printed on  numbers that are multiple of 3 and 5.


**1. Print square**

```./1-print_square.js 10 should print a square of size 10…```
Using parseInt with base 16, which is a hexadecimal base was the cause of the bug, change it to base 10.


**2. Sort**

Adding the lower numbers at the end of the list instead of the higher number was causing the bug


**3. User password**

When comparing the hashed password, it was being compared with a password that was hashed into uppercase, which effected the comparision. This causes the bug


**4. Double linked list**

When deleteing a node in the delete_dnodeint function, the node was being deleted prematurely and it causes the next and previous node references to get lost.  
