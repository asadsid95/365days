# Find unique element from a given list

def unqElement(plist):

    count = {}
    for i in plist:
        print(count.setdefault(i, 1))
        print(count.values())

        if(i == count):  # Since i is integer value, using that as dict's index
            count[i] += 1

    print(count)

    # if(count[i] == [1]):
    # print(sum(count[i]))
    return 0


unqElement([0, 0, 5, 0, 8, 8, 8, 5, 5, 8])
