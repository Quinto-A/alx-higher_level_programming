#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list and only integers

    Args:
        my_list (list): list from where x elements are to be printed

    x (int) : The number of element of my_list to print.

    Returns:
        The number of elements printed.
    """
    digits = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            digits += 1
        except (ValueError, TypeError):
            continue
        #except IndexError:
        #    break
    print("")
    return (digits)
