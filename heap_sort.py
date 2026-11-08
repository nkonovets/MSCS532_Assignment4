
def swap(data, i, j):   #swap fuction to swap numbers in the heap
    data[i], data[j] = data[j], data[i]

def siftDOwn(data, i, upper):

    while (True):
        l, r = i*2+1, i*2+2         #left and right children

        if max(l,r) < upper:        #check if there are chidren to the parent element in the heap
            if data[i] >= max(data[l], data[r]): 
                break
            elif data[l] > data[r]: #swap left children with parent 
                swap(data, i, l)
                i = l
            else:
                swap(data, i, r)    #swap right children with parent
                i = r

        elif l < upper:             # only the left child exists
            if data[l] > data[i]:
                swap(data, i, l)
                i = l
            else: 
                break

        elif r < upper:             # extra safety check, this case does not happen in a heap
            if data[r] > data[i]:
                swap(data, i, r)
                i = r
            else:
                break

        else:                       #break if no children left
            break



def heapsort(data):

    for j in range((len(data)-2)//2, -1, -1):   #heapify the data
        siftDOwn(data, j, len(data))

    for end in range(len(data)-1, 0, -1):
        swap(data, 0, end)
        siftDOwn(data, 0, end)


def heap_sort_in_place(numbers_list, left, right):  #function for the recorder to properly work with the recorder

    sorted_part = numbers_list[left:right + 1]
    heapsort(sorted_part)
    numbers_list[left:right + 1] = sorted_part