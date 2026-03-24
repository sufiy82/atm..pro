class Sort:
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr

    def quick_sort(self, arr):
        self._quick_sort_helper(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort_helper(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self._quick_sort_helper(arr, low, pi - 1)
            self._quick_sort_helper(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


def main():
    sorter = Sort()

    while True:
        print("\n--- Sorting Menu ---")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 6:
            print("Exiting...")
            break

        arr = list(map(int, input("Enter elements separated by space: ").split()))

        if choice == 1:
            print("Sorted array:", sorter.bubble_sort(arr))
        elif choice == 2:
            print("Sorted array:", sorter.selection_sort(arr))
        elif choice == 3:
            print("Sorted array:", sorter.insertion_sort(arr))
        elif choice == 4:
            print("Sorted array:", sorter.merge_sort(arr))
        elif choice == 5:
            print("Sorted array:", sorter.quick_sort(arr))
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
