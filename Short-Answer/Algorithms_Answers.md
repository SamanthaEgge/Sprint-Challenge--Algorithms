#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

# a)  Time: O(2n) => O(n). Space: O(1). #
    This is because the while loop is only 1 deep, and it only iterates over the value of n. The space is O(1) because no variables are saved, and 'a' overwrites itself.

    `a = 0
    while (a < n * n * n):
      a = a + n * n`

# b)  Time: O(n^2), Space: O(1) #
    This is because for each iteration of the range(n) the while loop must run for each. This causes the n^2.
    Space is O(1) since no values are being saved, and it's getting overwritten each time.

    `sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1`

# c)  Time: O(n), Space: O(n) #
    Space taken by this function is O(n) due to recursion. The function must hold each value as it goes down through the number of bunnies.
    Time is set 

    `def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)`

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

# Proposed Algo #


# Pseudocode #
`def egg_check(building)
  
`

# Runtime Complexity #
Space: O()
Time: O()
