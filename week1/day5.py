# Two Sum
# return indices of the 2 vlaue that equated target value, in a list

class Solution():

    def __init__(self, nums, target):
        self.listtww = nums
        self.t = target

    def twoSum(self):
        print(self.listtww)

        for n in range(len(self.listtww)):
            print("hello")

        if n in [0, 2, 6]:
            print('in-if conditional worked!', n)


object1 = Solution([1, 6, 2, 5, 6, 6, 9], 7,)

print(object1.twoSum())
