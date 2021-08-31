# Reverse Integer (LC # 9)

# Input: integer (range of [-2^31, (2^31)-1])
# Output: REVERSED integer || 0 if reversed's binary form > 32-bit

# Approach:
# reverse input, get and compare 32-bit form for input & reversed
#

def compare(x):

    x_string=str(x)
    x_rev = int(x_string[::-1])

    if (x_rev == 0):
        print('Input = 0')
    elif (x_rev > ((2**31) -1)):
        print(0)
    else:
        print(x_rev, x)

compare(10111)
