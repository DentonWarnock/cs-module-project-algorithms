#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  options = ['rock', 'paper', 'scissors']
  possibilities = []
  if n == 0:
    return [possibilities]
  elif n == 1:
    return [[options[0]], [options[1]], [options[2]]]
  else:
    # add list with first option n times to possibilites
    # add list with first option n - 1 times, second option 1 time to possibilites
    # add list with first option n - 1 times, third option 1 time to possibilites
    # add list with second option 1 time, first option 1 time
    # add list with second option 1 time, second option 1 time
    #
    #
    #
    
    
    
    return possibilities
  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')