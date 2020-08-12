'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # iterate through all nums in the array
    # add items to a dictionary and keep track of the number of times item appears with value += 1 for each time
    dictionary = {} 
    for num in arr:
        if num not in dictionary.keys():
            dictionary[num] = 1
        else: 
            dictionary[num] += 1
    
    # iterate through dictionary, find item with value of 1 (there will only be one)
    # return that item's key(original value)
    for key, value in dictionary.items():
        print(f'key: {key}, value: {value}')
        if value == 1:
            print(f'FOUND!!! key: {key}, value: {value}')
            return key

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")