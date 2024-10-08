def binary_search(lst,target):
    low = 0 
    high = len(lst) -1
    while low <= high:
        mid = (low + high)//2

        if lst[mid] == target :
            return mid+1
        elif lst[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return -1
    
l = [1,2,3,4,5,6,7]
print(binary_search(l,4))
