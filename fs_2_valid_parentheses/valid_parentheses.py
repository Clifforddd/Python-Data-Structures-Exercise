def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count = 0
    for i in parens:
        if i == "(":
            count += 1
        if i == ")":
            count -= 1
        if count < 0:
            return False

    return count == 0

print(valid_parentheses("()()"))
print(valid_parentheses(")()("))
print(valid_parentheses("())"))