#  https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# [5, 7, 7, 8, 8, 10]
# 8
# 3, 4
# Sorted array

# first search
# start = 0, end = 5, mid = 2 num = 7
# start = 3, end = 5, mid = 4, num = 8
# start = 3, end = 4, mid = 3, num = 8 
# start = 3, end = 3, mid = 3, num = 8

# Next search
# start = 0, end = 5, mid = 2 num = 7
# start = 3, end = 5, mid = 4, num = 8
# start = 4, end = 4, mid = 4, num = 8 

#

def find_num_ind_range(nums, num):
    n = len(nums)
    start = 0
    end = n - 1
    while start < end:
        mid = start + ((end - start) // 2)
        if nums[mid] < num:
            start = mid + 1 
        else: # looking at N
            end = mid
      
    if (nums[end] != num):
        return (-1, -1)
    first_occ = end

    start = 0
    end = n - 1
    while start < end:
        mid = start + ((end - start) // 2)
        if nums[mid] <= num:
            start = mid + 1
        else: # looking at N
            end = mid
            
    start-=1 
    return (first_occ, start) 

t1 = [5, 7, 7, 8, 8, 10]
t2 = [5, 7, 7, 8, 8, 8, 10]
print(find_num_ind_range(t1, 8) == (3,4))
print(find_num_ind_range(t2, 8) == (3,5))
print(find_num_ind_range(t2, 2) == (-1,-1))