# Python program to find second largest

def findLargest(arr):
    """
    :param arr:  array of list
    :return: second largest number from the list
    """
    secondLargest = arr[0]
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(len(arr)):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]

    return secondLargest


if __name__ == "__main__":
    print(findLargest([10, 20, 4, 45, 99]))

