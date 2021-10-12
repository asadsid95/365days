# Day 14

# LC # 26 - Remove duplicates from sorted array

# Input: Array (assumed to be sorted; Could verify at the beginning)
# Output: Sorted array w/o duplicates

# Approach: Verify array is sorted; Set up a counter, traverse through array,
#                                      set counter equal to value of each element then check the next element's value with counter's value;
#                                        If equal, remove element at the specific index
#                                         If not, traverse to next element and set counter's value


sorted = [1, 1, 1, 2, 2, 3, 3, 4]

l = 1

for r in range(len(sorted)):
    first = sorted[l]
    second = sorted[r]

    print(first)
    print(second)
    l += 1

    # print(r-1)
