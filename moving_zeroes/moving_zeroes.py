'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # iterate through each number in list
    # check if current number equals zero
        # if yes, remove that number and add it to the end of the list
    # return the list
    copy = arr
    print(f'starting arr: {copy}')
    for index, num in enumerate(copy):     
        print(f'index: {index}, num: {num}')   
        if num == 0:            
            popped = copy.pop(index)
            copy.append(popped)
    print(f'ending arr: {copy}')
    return copy


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")