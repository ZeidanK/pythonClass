
from random import randint
from timeit import repeat
import time

def measure_sort_time(arr, sort_function):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()

    print(f"Time taken by {sort_function.__name__}: {end_time - start_time} seconds")

# Python3 program for Bubble Sort Algorithm Implementation
def bubbleSort(arr):
    """
    Bubble Sort algorithm implementation in Python.

    Time complexity analysis:
    - Best case: O(n) when the input is already sorted. This is because the algorithm will make one pass through the array to confirm it's sorted and then stop.
    - Average case: O(n^2) for randomly ordered input. This is because for each element, the algorithm goes through the rest of the array to find its correct position.
    - Worst case: O(n^2) when the input is sorted in reverse order. This is because the algorithm has to move each element from one end of the array to the other.
    """    
    n = len(arr)
    # For loop to traverse through all 
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):  
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_count(arr):
    n = len(arr)
    num_operations = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            num_operations += 1  # Count comparison
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                num_operations += 1  # Count swap
    return num_operations

def check_case(arr, sort_function):
    if arr == sorted(arr):
        print(f"For {sort_function.__name__}, this is the best case scenario.")
    elif arr == sorted(arr, reverse=True):
        print(f"For {sort_function.__name__}, this is the worst case scenario.")
    else:
        print(f"For {sort_function.__name__}, this is likely an average case scenario.")

# Selection Sort algorithm in Python
def selectionSort(array, size):
     
    for s in range(size):
        min_idx = s
         
        for i in range(s + 1, size):
             
            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
 
        # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])
 

# Creating a function for insertion sort algorithm
def insertion_sort(list1):  
   
        # Outer loop to traverse on len(list1)  
        for i in range(1, len(list1)):  
   
            a = list1[i]  
   
            # Move elements of list1[0 to i-1], 
            # which are greater to one position
            # ahead of their current position  
            j = i - 1 
           
            while j >= 0 and a < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1 
                 
            list1[j + 1] = a  
             
        return list1  
            
# constanct time complexity - O(1):

def get_first_element(arr):
    """
    This function returns the first element of the given list.
    Since it always takes the same amount of time regardless of the list size, 
    its time complexity is O(1), also known as constant time complexity.
    """
    return arr[0]


# linear time complexity - O(n):
def find_element(arr, target):
    """
    This function checks if a target element exists in the given list.
    In the worst case, it has to check each element once, so its time complexity is O(n),
    also known as linear time complexity.
    """
    for element in arr:
        if element == target:
            return True
    return False

# quadratic time complexity - O(n^2):

def find_element_quadratic(arr, target):
    """
    This function checks if a target element exists in the given list.
    In the worst case, it has to check each element once, so its time complexity is O(n^2),
    also known as quadratic time complexity.
    """
    """
    Bubble Sort algorithm implementation in Python.

    Time complexity analysis:
    - Best case: O(n) when the input is already sorted. This is because the algorithm will make one pass through the array to confirm it's sorted and then stop.
    - Average case: O(n^2) for randomly ordered input. This is because for each element, the algorithm goes through the rest of the array to find its correct position.
    - Worst case: O(n^2) when the input is sorted in reverse order. This is because the algorithm has to move each element from one end of the array to the other.
    """    
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#logarithmic time complexity -O(log n):

def binary_search(arr, target):
    """
    This function implements the binary search algorithm.
    It repeatedly divides the list in half until the target element is found or the list is empty.
    Since it divides the list in half each time, its time complexity is O(log n),
    also known as logarithmic time complexity.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1               

#exponential time complexity - O(2^n):

def fibonacci(n):
    """
    This function calculates the nth Fibonacci number using a naive recursive approach.
    Since each function call branches into two new calls, its time complexity is O(2^n),
    also known as exponential time complexity.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#factorial time complexity - O(n!):
def permutations(arr):
    """
    This function generates all permutations of a given list.
    Since there are n! permutations of a list of length n, and the function generates each one once,
    its time complexity is O(n!), also known as factorial time complexity.
    """
    # Base case: if arr is empty, there are no permutations
    if len(arr) == 0:
        return []

    # Base case: if arr has one element, there is one permutation
    if len(arr) == 1:
        return [arr]

    # Recursive case: get all permutations for length of arr
    l = [] # empty list that will store current permutation

    for i in range(len(arr)):
        m = arr[i]

        # Remaining list
        remList = arr[:i] + arr[i+1:]

        # Generating permutation for the remaining list
        for p in permutations(remList):
            l.append([m] + p)
    return l


