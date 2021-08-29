# Tech interview

# Palindrome with string as input & boolean return
# I.M.O.W: check if string is the same spelt backwards

# Input: 'OTTO', 'ADA'
# Output: True, True

# Approach explained: Convert str -> list, create new list via indexing original list backwards && compare both list to yield boolean

def is_palindrome(input):
    str_list = list(input)
    rev_list = str_list[::-1]

    if (str_list == rev_list):   # I first typed '>' due to nervousness and low confidence
        return True
    else:
        return False


print(is_palindrome("OTTO"))

# Next part of assessment: Suggest a test case in which indexing the full string list before output is NOT effective

# I asked about validity of input (is null or empty string allowed? | can the string be part of multi-dim list? )

# Hint received: What if range of input is very large?
# I suggested string to be broken down into sections
# Sol'n: Start on both sides of input, i.e. First and Last element and compare them


def is_palindrome2(input):

    for i in range((len(input)/2)):

        # print(input[i], input[-(i)]);  ###### Since '[-(0)]' =  0, output was ('O', 'O')
        if (input[i] != input[-(i+1)]):
            print('FALSE')
            break

    print('Input is not palindrome. It worked until',input[i],input[-(i+1)])

    return 0


is_palindrome2("OLRbdRLO")
