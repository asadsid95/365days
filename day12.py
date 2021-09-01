# Reverse Integer (LC # 7)

# Input: integer (range of [-2^31, (2^31)-1])
# Output: REVERSED integer || 0 if reversed's binary form > 32-bit

# Approach:
# reverse input, get and compare 32-bit form for input & reversed
#

def compare(x):

    upper_bound = (2**31) - 1
    lower_bound = -2**31
    #print(upper_bound, lower_bound)

    if (x < 0):
        x_string=str(abs(x))
        x_rev = int(x_string[::-1])
        x_rev = x_rev * -1
    else:
        x_string=str(x)
        x_rev = int(x_string[::-1])

    if (x_rev == 0):
        print('Input = 0')
    elif (x_rev > upper_bound):
        print(0)
    else:
        print(x_rev, x)

compare(10111)
compare(111111110111111111111111111111)
