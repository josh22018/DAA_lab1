import random
import heapq
import time
class Lab_1_Part_2:


    def measure_time(self, function):
        start_time = time.time()
        function()
        end_time = time.time()
        return (end_time - start_time) * 1000

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def count_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (arr[i] // exp)
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arr[i] // exp)
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(len(arr)):
            arr[i] = output[i]

    def radix_sort(self, arr):
        max_element = max(arr)
        exp = 1
        while max_element // exp > 0:
            self.count_sort(arr, exp)
            exp *= 10

    def main(self):
        random.seed(42)
        arr = [random.randint(1, 10000) for _ in range(1000)]
        
        # Measure time for Bubble Sort
        bubble_sort_time = self.measure_time(lambda: self.bubble_sort(arr.copy()))
        print("Bubble Sort Time: {:.2f} milliseconds".format(bubble_sort_time))
        
        # Measure time for Selection Sort
        selection_sort_time = self.measure_time(lambda: self.selection_sort(arr.copy()))
        print("Selection Sort Time: {:.2f} milliseconds".format(selection_sort_time))
        
        # Measure time for Insertion Sort
        insertion_sort_time = self.measure_time(lambda: self.insertion_sort(arr.copy()))
        print("Insertion Sort Time: {:.2f} milliseconds".format(insertion_sort_time))
        
        # Measure time for Merge Sort
        merge_sort_time = self.measure_time(lambda: self.merge_sort(arr.copy()))
        print("Merge Sort Time: {:.2f} milliseconds".format(merge_sort_time))
        

        quick_sort_time = self.measure_time(lambda: self.quick_sort(arr.copy(), 0, len(arr) - 1))
        print("Quick Sort Time: {:.2f} milliseconds".format(quick_sort_time))
        

        radix_sort_time = self.measure_time(lambda: self.radix_sort(arr.copy()))
        print("Radix Sort Time: {:.2f} milliseconds".format(radix_sort_time))



    def merge_sorted_lists(self, lists):
        merged_list = []
        for lst in lists:
            merged_list.extend(lst)
        merged_list.sort()
        return merged_list



    def find_k_largest_elements(self, arr, k):
        return heapq.nlargest(k, arr)



    def max_activities(self, activities):
        activities.sort(key=lambda x: x[1])
        max_activities = 1
        current_activity = 0

        for i in range(1, len(activities)):
            if activities[i][0] >= activities[current_activity][1]:
                max_activities += 1
                current_activity = i

        print("Maximum number of activities:", max_activities)

        print("Activities:")
        for activity in activities:
            print("({}, {})".format(activity[0], activity[1]))


    # 5. Given a set of intervals, print all non-overlapping intervals after merging the overlapping intervals.

    def merge_intervals(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged


if __name__ == "__main__":
    lab = Lab_1_Part_2()
    lab.main()
