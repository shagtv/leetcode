bool uniqueOccurrences(int* arr, int arrSize){
    int nums[2000] = {0};
    int nums1[2000] = {0};
    for (int i = 0; i < arrSize; i++) {
        nums[arr[i] + 1000]++;
    }
    for (int i = 0; i < 2000; i++) {
        if (nums[i] && nums1[nums[i]]) {
            return false;
        }
        nums1[nums[i]] = 1;
    }
    return true;
}
