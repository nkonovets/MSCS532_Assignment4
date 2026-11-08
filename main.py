import sys

from file_parser import get_data
from quick_sort_random import quicksort_random_in_place
from merge_sort import merge_sort
from recorder import save_results
from heap_sort import heap_sort_in_place


sys.setrecursionlimit(100_000) 


if __name__ == "__main__":

    algorithm_choice = input("Choose which Algorithm to use: \n Quick Sort (q) \n ------------------ \n Merge Sort (m) \n ------------------ \n Heap Sort (h) \n: ")

    

    if algorithm_choice == "m":
        name = "Merge Sort"
        sort_algorithm = merge_sort

    elif algorithm_choice == "q":
        name = "Quick Sort Random"
        sort_algorithm = quicksort_random_in_place

    elif algorithm_choice == "h":
        name = "Heap Sort"
        sort_algorithm = heap_sort_in_place

    else:
        print("Wrong input, please restart the program and choose option \"q\" , \"m\" or \"h\" ")
        exit()


    filename = input("Select a file to get the data from for sorting: ")

    data = get_data(filename)
    print("Data before sorting: ", data)

    
    sorted_data = data.copy()

    sort_algorithm(sorted_data, 0, len(sorted_data) - 1)

    print("Data after sorting: ", sorted_data)

    save_results(name, sort_algorithm, data, filename)