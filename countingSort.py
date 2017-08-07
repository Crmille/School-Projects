"""
CS 4343 Data Structures
October 23, 2014
Chad Miller (rycha@okstate.edu)
Assignment 4§(4)
"""
def sort(A):
    """
    Counting Sort Algorithm
        
    Parameters
    ----------
    A : array
        The array to be sorted.
            
    Returns
    -------
    out : sort of A        
        
    """
    # Find max and min of list A.    
    minx = min(A)
    maxx = max(A)
    
    # Empty bucket creation.        
    C = [0]*(maxx-minx+1)
    
    # Preliminary Counting
    for j in A:
        C[j-minx] += 1
    
    # New List and Appending Sort
    sort = []
    for i in range(minx, maxx+1):
        if C[i-minx] > 0:
            for j in range(C[i-minx]):
                sort.append(i)
    
    return sort

