#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

# a)  Time: O(2n) => O(n). Space: O(1). #
    This is because the while loop is only 1 deep, and it only iterates over the value of n. The space is O(1) because no variables are saved, and 'a' overwrites itself.

    `a = 0
    while (a < n * n * n):
      a = a + n * n`

# b)  Time: O(n), Space: O(1) #
    For each n, the function must run x2 as many times to get through the while loop.
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
  Take a set of n building levels
  Need to check each level starting at 0 and determine if egg is broken
  For floor in floors
  Check egg drop, did egg survive?
  if True, do the algo again, checking counter +1 while counter < Floor

  This checks starting at 0 -> n floors until an egg breaks
  The answer is returned as floor(counter-1)
  

# Pseudocode #
`def egg_check(building)
  counter initalization
  broken floor= None
  #Exit Case
  if Broken_floor:
    return broken_floor
  if counter < building
    drop egg
    if egg survived:
      counter+1
      return building
    else:
      broken floor=counter-1
  else:
    broken_floor = 'no broken floors for this building'
`

# Runtime Complexity #
Space: O(1)
Time: O(n)
(it's of o n, because the if statement checking if counter < building only iterates once)
