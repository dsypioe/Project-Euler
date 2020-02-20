# problem122

# returns true if the given list is in aascending order
def isAscending(lst):

    if len(lst) in [0,1]:
        return True
    if lst[0] <= lst[1]:
        return isAscending(lst[1:])
    return False

# returns true if the given list is in decending order
def isDescending(lst):
    if len(lst) in [0,1]:
        return True
    if lst[0] >= lst[1]:
        return isDescending(lst[1:])
    return False