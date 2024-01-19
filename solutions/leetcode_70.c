int helper(int n, int cache[45])
{
    if (n < 0) {
        return 0;
    }
    if (n == 0) {
        return 1;
    }
    if (cache[n]) return cache[n];
    cache[n] = helper(n - 1, cache) + helper(n - 2, cache);
    return cache[n];
}

int climbStairs(int n) {
    int cache[46] = {0};
    return helper(n, cache);
}
