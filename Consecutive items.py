"""
7 Kyu
You are given a list of unique integers arr, and two integers a and b. Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).

It is guaranteed that a and b are both present in arr.
"""
def consecutive(arr, a, b):
    return abs(arr.index(a)-arr.index(b))==1 
    
        
    

print(consecutive([1, 3, 5, 7], 3, 7))


