def merge(LHS, RHS):
    # initiate a list to store values in sorted order
    merged_list = []
    # while both lists have values comparison will be necessary
    while (len(LHS) > 0) and (len(RHS) > 0):
        # append smallest value to sorted list and remove from comparison
        if LHS[0] < RHS[0]:
            merged_list.append(LHS[0])
            LHS.pop(0)
        else:
            merged_list.append(RHS[0])
            RHS.pop(0)
    # append any values left behind after comparisons
    # only one of these cases should be valid after the prior step
    for each_value in LHS:
        merged_list.append(each_value)
    for each_value in RHS:
        merged_list.append(each_value)
    # return the merged sorted values
    return merged_list

def merge_sort(arr):
    # multi-element list is case for recursion
    if len( arr ) > 1:
        # split the list into halves
        LHS = arr[:len(arr)//2]
        RHS = arr[len(arr)//2:]
        # recursively split the list until base case is reached
        LHS = merge_sort(LHS)
        RHS = merge_sort(RHS)
        # return a sorted list using the merge helper to join the two halves 
        return merge(LHS, RHS)
    # single element list, which --by definition-- cannot be unsorted, is base case
    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
