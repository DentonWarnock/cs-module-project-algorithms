#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # create empty sack to add items to and return
    sack = []
    
    # sort items by value
    items.sort(key=lambda x: x.value, reverse=True) # sort by most valuable items first
    
    # put most valueable items in sack until full
    weight = 0
    value = 0
    for item in items:   
      print(f'starting weight: {weight}')    
      print(item)  
      print(item.size)
      # try adding the weight
      weight += item.size
      print(f'ending weight: {weight}')
      # check if the new weight will be too heavy - if so return early
      if weight > capacity:
        return {'Value': value, 'Chosen': sack, "Weight": weight}
      else:
        # add items value and index        
        value += item.value
        sack.append(item.index)
    
    return {'Value': value, 'Chosen': sack}
    
    
    


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')