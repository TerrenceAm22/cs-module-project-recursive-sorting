# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    """
    recursive implementation
    """
    # Checking base case
    if end >= start:
        mid = (start + end) // 2

        # if the target us present at the middle 
        if arr[mid] == target:
            return mid
        
        # if the target is smaller than the mid
        # then it is only present in the left part 
        # of the list
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid -1)
        # The target can be only in the right side of the array
        else:
            return binary_search(arr, target, mid+1, end)

    
    else:
        # target is not in the array
        return -1
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

