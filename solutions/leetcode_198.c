int helper(int* nums, int numsSize, int16_t cache[101])
{
    if (numsSize <= 0) return 0;
    if (cache[numsSize] != -1) return cache[numsSize];

    cache[numsSize] = nums[numsSize - 1] + helper(nums, numsSize - 2, cache);
    int a = helper(nums, numsSize - 1, cache);
    if (a > cache[numsSize])
        cache[numsSize] = a;

    return cache[numsSize];
}

int rob(int* nums, int numsSize)
{
    int16_t cache[101];
    memset(cache, -1, 101 * sizeof(int16_t));
    return helper(nums, numsSize, cache);
}
