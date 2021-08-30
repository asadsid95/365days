# Palindrome Number (LC # 9)

x = 123
x_s = str(123)

listed = list(x_s)
# print(listed)

rev = listed[::-1]
new_x = ''
# print(new_x.join(rev))


class Solution(object):

    def __init__(self, x):
        self.x = x

    def isPalindrome(self):

        str_x = str(self.x)

        listed = list(str_x)

        rev_list = listed[::-1]

        new_str = ''

        rev_str = new_str.join(rev_list)

        rev_int = int(rev_str)

        if (rev_int == self.x):
            return True
        else:
            return False

        """
        :type x: int
        :rtype: bool
        """
        return 0


trial = Solution(92029)

print(trial.isPalindrome())
