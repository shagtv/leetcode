nums = [10, 2, 1, 12, 43, 23, 13, 12]
print(nums)


def qsort(nums):
    def internal_sort(nums, lo, hi):
        if lo >= hi:
            return
        pivot = partition(nums, lo, hi)
        internal_sort(nums, lo, pivot - 1)
        internal_sort(nums, pivot + 1, hi)

    def partition(nums, lo, hi):
        pivot = lo
        for i in range(lo + 1, hi + 1):
            if nums[i] < nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot = i
        return pivot

    internal_sort(nums, 0, len(nums) - 1)


qsort(nums)
print(nums)
