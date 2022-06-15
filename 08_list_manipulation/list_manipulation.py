def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """ 
    if command == "remove" and location == "beginning":
        print(lst[0])
        lst.remove(lst[0])
    elif command == "remove" and location == "end":
        print(lst[-1])
        lst.remove(lst[-1])
        lst.pop()
    elif command == "add" and location == "beginning":
        lst.insert(0, value)
        print(lst)
    elif command == "add" and location == "end":
        lst.append(value)
        print(lst)
    else:
        print("None") 


lst = [1, 2, 3]
list_manipulation(lst, 'remove', 'end')
lst = [1, 2, 3]
list_manipulation(lst, 'remove', 'beginning')
lst = [1, 2, 3]
list_manipulation(lst, 'add', 'beginning', 20)
lst = [20, 1, 2, 3]
list_manipulation(lst, 'add', 'end', 30)
list_manipulation(lst, 'foo', 'end')