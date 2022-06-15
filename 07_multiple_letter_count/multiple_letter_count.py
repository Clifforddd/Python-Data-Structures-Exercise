def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    dict = {}
    lst = list(phrase)

    for x in lst:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1

    print(dict)
    
multiple_letter_count('yay')
multiple_letter_count('Yay')