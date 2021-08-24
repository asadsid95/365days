# Palindrome Number (LC # 9)


x = 123
x_s = str(123)

listed = list(x_s)
print(listed)

rev = listed[::-1]
new_x = ''
print(new_x.join(rev))


class Solution(object):
    def isPalindrome(self, x):

        self.x = x
        str_x = str(self.x)

        print(str_x)
        """
        :type x: int
        :rtype: bool
        """


trial = Solution.isPalindrome

print(trial(27))

# Reverse Integer (LC # 7 )
