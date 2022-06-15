def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    result = {}

    for num in nums:
        result[num] = result.get(num, 0) + 1

    max_value = max(result.values())

    for (num, x) in result.items():
        if x == max_value:
            return num

