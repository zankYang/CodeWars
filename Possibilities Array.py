"""
7 Kyu

A non-empty array a of length n is called an array of all possibilities if it contains all numbers between [0,a.length-1].Write a method named isAllPossibilities that accepts an integer array and returns true if the array is an array of all possibilities, else false.
"""

def is_all_possibilities(arr):
    if len(arr) == 0:
        return False
    for number in range(len(arr)):
        if arr.count(number)<=0:
            return False
    return True

print(is_all_possibilities([1,2,3,0]))