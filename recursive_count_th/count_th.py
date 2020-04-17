'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0

def count_th(word):
  # This is the exit case, and if there is only 1 or 0 letters, you can't have 'th'
  global count
  if len(word) <= 1:
    # These variables are because I couldn't figure out how to reset counter between function initialization :(
        ## (but it wooorrkkksss)
    final = count
    count = 0
    # print('final')
    # print(final)
    return final

  # Going to begin at the end of the string, and move towards the front checking each pairs of letters for th.
  # For each set of letters checked, remove the last letter, and move back through count_th until exit case is met
  # ex. "checkers" check 'rs', remove s, check 'er', remove r, check 'ek', etc etc until len(c) <= 1
  if word[-2:] == 'th':
    count += 1
    # the following two lines need to be refactored :(
    word = word[:-2:]
    return count_th(word)
  else:
    word = word[:-1:]
    return count_th(word)