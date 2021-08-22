# Two Sum
# return indices of the 2 vlaue that equated target value, in a list

class Solution():

    def __init__(self, nums, target):
        self.listtww = nums
        self.target = target

    def twoSum(self):

        nums_dict = {}
        for n in range(len(self.listtww)):
            diff = self.target - self.listtww[n]
            # print(diff)
            if diff in nums_dict:
                print(diff)
            else:
                nums_dict[diff] = n
        return (nums_dict[diff], n)


object1 = Solution([1, 6, 2, 5, 9, 10], 15)

print(object1.twoSum())
