# Day 13
# LC # 27 - Remove elements

# Problem statement IMOW:
# Getting an array/list AND an integer value as input, all occurrences of that value need to be removed from the list

# Input: nums = [1,2,1,1,3,45]
        # val = 1
# Output: k=0

# Approach:

# Loop 1:
# Compare list's first element to val:
    # - If YES (element matches val), pop()/del() that element + increment k
    # - If NO, go to next element (via count increment; look into len(nums))

# Loop 2 (assuming first element matched val): nums = [2,1,1,3,45] | val = 1 | k = 1)
# Compare first element to val:
    # - If YES (element matches val), pop()/del() that element + increment k
    # - If NO, go to next element (via count increment; look into len(nums))
