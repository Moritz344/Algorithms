# Groß --> Klein

def bubble_sort(array):
    swapped = True
    num_of_iterations = 0

    while (swapped):
        swapped = False
        for i in range(len(array) - num_of_iterations - 1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                swapped = True

        num_of_iterations += 1



data = [3,1,4,5,7,9,8]
bubble_sort(data)
print(data)
