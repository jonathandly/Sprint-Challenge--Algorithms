#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(n) -> Because you have a while loop that checks whether a is less than n^3. As the input increases the runtime will grow at the same rate.

b)
O(n^2) -> Since you have a for loop with a while loop nested inside, that loops through every iteration in the for loop. This results in a runtime of O(n^2).

c)
O(n) -> Due to it being recursive and decrementing bunnies by 1 on each call, its runtime is limited to the size of the input n, and so it runs in O(n).

## Exercise II

Use binary search to sort n

1. Start with an interval covering the whole list.
2. If f < middle, narrow the search to the lower half of the list.
3. If f > middle, reduce the search to the upper half of the list.
4. Find the new middle value and repeat steps 2 through 4 until the list is sorted.

The runtime of binary search is O(log n).
