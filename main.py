def highest_even(li):
    high_even = 0
    for a in li:
        if a%2 == 0:
            if a > high_even:
                high_even = a
    return high_even


print(highest_even([10,2,3,4,8,11]))