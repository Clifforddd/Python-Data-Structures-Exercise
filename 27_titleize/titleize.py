def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()

    return phrase.title()

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))