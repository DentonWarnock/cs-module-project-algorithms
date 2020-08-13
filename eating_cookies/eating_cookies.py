'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # base case
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        # make recursive call
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
