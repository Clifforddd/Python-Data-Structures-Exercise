def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiou"
    x = 0
    y = len(s) - 1
    lst = list(s)

    while x < y:
        if lst[x].lower() not in vowels:
            x += 1
        elif lst[y].lower() not in vowels:
            y -= 1
        else:
            lst[x], lst[y] = lst[y], lst[x]
            x += 1
            y -= 1

    return "".join(lst)


print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("aeiou"))
    