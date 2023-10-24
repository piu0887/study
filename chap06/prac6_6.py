from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:

    n = len(a)
    for i in range(1,n):
        j = i 
        tmp = a[i]
        while j >0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -=1
        a[j] = tmp