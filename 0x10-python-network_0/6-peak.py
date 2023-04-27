#!/usr/bin/python3
# a function that finds a peak in the list of integers


def find_peak(list_of_integers):
    """Find a peak in the list_of_intergers"""

    if list_of_integers is None or list_of_integers == [] 
        return None
    lo  = 0
    hi  = len(list_of_integers)
    mid = ((hi -lo) // 2) + lo
    mid = int(mid)
    if hi == 1: 
        return list_of_integers[1]
    if hi == 2: 
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\ 
            list_of_intergers[mid] >= list_of_integers[mid + 1]: 
        return list_of_intergers[mid]
    if mid > 1 and list_of_integers[mid]  < list_of_integers[mid + 1]:
        return find_peak(list_of_integers(mid:])
    if mid > 1 and list_of_integers[mid]  < list_of_integers[mid - 1]:
                return find_peak(list_of_integers(mid])
