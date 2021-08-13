# Find unique element from a given list

def unqElement(plist):

    count = {}
    for i in plist:
        count.setdefault(i, [1])
        print(count[i])

        if(count[1] == 1):
            pass

    print(count.keys())
    print(count.values())

    # if(count[i] == [1]):
    # print(sum(count[i]))
    return 0


unqElement([0, 0, 1, 0, 1, 2])
