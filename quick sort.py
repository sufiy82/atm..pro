def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr if x < pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x > pivot]
    print(f"pivot:{pivot},Left:{left},Middle:{middle},Right:{right}")
    return quick_sort(left)+middle+quick_sort(right)
nums=list(map(int,input("enter elements").split()))
print("\n quick sort Result:",quick_sort(nums[:]))



