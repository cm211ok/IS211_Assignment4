import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found
    
    
def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


def measure_time_for_search_function(search_function, list_size):
    total_time = 0
    for i in range(100):  # Run 100 times for each list size
        mylist = get_me_random_list(list_size)
        mylist_sorted = sorted(mylist)  # Sort for Binary Search and Ordered Search

        start = time.time()
        search_function(mylist_sorted, 99999999)  # Search for a non-existent element (worst case)
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    return avg_time


if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        print(f"List size: {the_size}")
        
        avg_sequential_time = measure_time_for_search_function(sequential_search, the_size)
        avg_binary_iterative_time = measure_time_for_search_function(binary_search_iterative, the_size)
        avg_binary_recursive_time = measure_time_for_search_function(binary_search_recursive, the_size)
        avg_ordered_sequential_time = measure_time_for_search_function(ordered_sequential_search, the_size)
        
        print(f"Sequential Search took {avg_sequential_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Binary Search Iterative took {avg_binary_iterative_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Binary Search Recursive took {avg_binary_recursive_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Ordered Sequential Search took {avg_ordered_sequential_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        print("\n")
