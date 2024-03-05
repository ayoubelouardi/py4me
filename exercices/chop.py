# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None.

# Then write a function called middle that takes a list and returns a
# new list that contains all but the first and last elements.

def chop(thelist):
    del thelist[0]
    del thelist[-1]

    return None

def middle(thelist):
    del thelist[0]
    del thelist[-1]

    return thelist
