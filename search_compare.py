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


if __name__ == "__main__":
    """Main entry point"""
    the_size = 500
    target_item = 99999999  # This item won't be in the list for worst-case scenario

    # Initialize variables for total time
    total_sequential_time = 0
    total_ordered_sequential_time = 0
    total_binary_iterative_time = 0
    total_binary_recursive_time = 0

    for i in range(100):
        mylist = get_me_random_list(the_size)
        # Sorting the list for ordered sequential search and binary search
        mylist_sorted = sorted(mylist)

        # Sequential Search
        start = time.time()
        sequential_search(mylist, target_item)
        time_spent = time.time() - start
        total_sequential_time += time_spent

        # Ordered Sequential Search
        start = time.time()
        ordered_sequential_search(mylist_sorted, target_item)
        time_spent = time.time() - start
        total_ordered_sequential_time += time_spent

        # Binary Search Iterative
        start = time.time()
        binary_search_iterative(mylist_sorted, target_item)
        time_spent = time.time() - start
        total_binary_iterative_time += time_spent

        # Binary Search Recursive
        start = time.time()
        binary_search_recursive(mylist_sorted, target_item)
        time_spent = time.time() - start
        total_binary_recursive_time += time_spent

    # Average times
    avg_sequential_time = total_sequential_time / 100
    avg_ordered_sequential_time = total_ordered_sequential_time / 100
    avg_binary_iterative_time = total_binary_iterative_time / 100
    avg_binary_recursive_time = total_binary_recursive_time / 100

    # Print 
    print(f"Sequential Search took {avg_sequential_time:10.7f} seconds to run, on average for a list of {the_size} elements")
    print(f"Ordered Sequential Search took {avg_ordered_sequential_time:10.7f} seconds to run, on average for a list of {the_size} elements")
    print(f"Binary Search Iterative took {avg_binary_iterative_time:10.7f} seconds to run, on average for a list of {the_size} elements")
    print(f"Binary Search Recursive took {avg_binary_recursive_time:10.7f} seconds to run, on average for a list of {the_size} elements")
