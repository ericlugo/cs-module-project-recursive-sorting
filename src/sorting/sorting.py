"""
merge(LHS, RHS):
    initiate a list to store values in sorted order
    while both lists have values comparison will be necessary
        append smallest value to sorted list and remove from comparison
    append any values left behind after comparisons
    only one of these cases should be valid after the prior step
    return the merged sorted values
"""

def merge(LHS, RHS):
    merged_list = []
    while (len(LHS) > 0) and (len(RHS) > 0):
        if LHS[0] < RHS[0]:
            merged_list.append(LHS[0])
            LHS.pop(0)
        else:
            merged_list.append(RHS[0])
            RHS.pop(0)
    for each_value in LHS:
        merged_list.append(each_value)
    for each_value in RHS:
        merged_list.append(each_value)
    return merged_list

"""
merge_sort(arr):
    multi-element list is case for recursion
        split the list into halves
        recursively split the list until base case is reached
        return a sorted list using the merge helper to join the two halves 
    single element list, which --by definition-- cannot be unsorted, is base case
"""
def merge_sort(arr):
    if len( arr ) > 1:
        LHS = arr[:len(arr)//2]
        RHS = arr[len(arr)//2:]
        LHS = merge_sort(LHS)
        RHS = merge_sort(RHS)
        return merge(LHS, RHS)
    return arr


"""
merge_in_place(arr, start_index, middle_index, end_index):
    if already sorted simply return
    while each sublist still has elements in it
        if arr[start_index] is already in right position simply move the left pointer
        otherwise:
            store value and index for current start of second list
            shift all elements between the start of the first and second sublists to the right by 1
            insert the stored value in the correct position
            update all pointers
"""
def merge_in_place(arr, start_index, middle_index, end_index):
    start_index_2 = middle_index+1
    if arr[middle_index] <= arr[start_index_2]:
        return
    while (start_index <= middle_index) and (start_index_2 <= end_index):
        if arr[start_index] <= arr[start_index_2]:
            start_index += 1
        else:
            temporary_value = arr[start_index_2]
            temporary_index = start_index_2
            while temporary_index != start_index:
                arr[temporary_index] = arr[temporary_index-1]
                temporary_index -= 1
            arr[start_index] = temporary_value
            start_index += 1
            middle_index += 1
            start_index_2 += 1

"""
merge_sort_in_place(arr, left_index, right_index):
    multi-element list is the case for recursion. if base case evaluate as False and begin the merging process
        prevents overflow for large left or right index values
        create more pointers to mark each subsegment of the array before beginning the merge
        sort the sublists using the created markers
"""
def merge_sort_in_place(arr, left_index, right_index):
    if left_index < right_index:
        middle_index = left_index + (right_index-left_index) // 2
        merge_sort_in_place(arr, left_index, middle_index)
        merge_sort_in_place(arr, middle_index+1, right_index)
        merge_in_place(arr, left_index, middle_index, right_index)
