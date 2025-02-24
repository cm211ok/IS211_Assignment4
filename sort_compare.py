import argparse
import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value


def shellSort(a_list):
    sublistcount = len(a_list)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(a_list, startposition, sublistcount)

        sublistcount = sublistcount // 2


def gapInsertionSort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    """
    Use Python built-in sorted function

    :param a_list:
    :return: the sorted list
    """
    return sorted(a_list)


# Benchmarking function for sorting algorithms
def measure_time_for_sort_function(sort_function, list_size):
    total_time = 0
    for i in range(100):  # Run 100 times for each list size
        mylist = get_me_random_list(list_size)

        start = time.time()
        sort_function(mylist)  # Sort the list using the provided sorting function
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    return avg_time


def main():
    """Main entry point"""
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        print(f"List size: {the_size}")

        # Measure the time taken for each sorting algorithm
        avg_python_time = measure_time_for_sort_function(python_sort, the_size)
        avg_insertion_time = measure_time_for_sort_function(insertion_sort, the_size)
        avg_shell_time = measure_time_for_sort_function(shellSort, the_size)

        # Print the average times for each sorting algorithm
        print(f"Python Sort took {avg_python_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Insertion Sort took {avg_insertion_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Shell Sort took {avg_shell_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        print("\n")


if __name__ == "__main__":
    main()
