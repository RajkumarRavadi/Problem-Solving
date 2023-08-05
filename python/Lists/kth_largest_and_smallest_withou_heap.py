def kthSmallestLargest(arr, k):
    # Your code goes here
    # print("ARRAY IS :", arr)
    narr = sorted(arr)
    # print("sorted array is", narr)

    distic_list = [*set(narr)]
    acending_list = sorted(distic_list)
    # print(acending_list)
    small = None
    large = None

    if k <= len(acending_list):
        small = acending_list[k - 1]
        # print(small)

    decending_list = sorted(distic_list, reverse=True)
    # print(decending_list)

    if k <= len(decending_list):
        large = decending_list[k - 1]
        # print(large)

    return small, large


# Driver's code
t = int(input())

while t > 0:
    n, k = map(int, input().split())
    arr = [int(i) for i in input().split()]
    small, large = kthSmallestLargest(arr, k)

    if small is not None and large is not None:
        print(large, small)
    else:
        print("k is out of range")

    t -= 1
