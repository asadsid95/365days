# Two Sum (LC # 1)
# return indices of the 2 vlaue that equated target value, in a list

class Solution():

    def __init__(self, nums, target):
        self.listtww = nums
        self.target = target

    def twoSum(self):

        nums_dict = {}
        for n in range(len(self.listtww)):
            diff = self.target - self.listtww[n]
            # print(n, self.listtww[n], diff)
            #print(nums_dict.keys())

            if diff in nums_dict.keys():
                print(n, self.listtww[n])
                return "done"
            else:
                nums_dict[n] = n
        print(nums_dict)

        # return (nums_dict[diff], n)


object1 = Solution([1, 6, 2, 5, 9, 10], 11)

print(object1.twoSum())
