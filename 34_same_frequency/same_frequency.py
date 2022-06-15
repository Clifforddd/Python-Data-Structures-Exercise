def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    counts1 = {}
    counts2 = {}

    for x in str(num1):
        counts1[x] = counts1.get(x, 0) + 1
    #print(counts1)

    for y in str(num2):
        counts2[y] = counts2.get(y, 0) + 1
    #print("2!!",counts2)

    return counts1 == counts2

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
    