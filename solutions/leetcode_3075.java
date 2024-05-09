import java.util.Arrays;

class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        int fee = 0;
        long result = 0;
        for (int i = happiness.length - 1; i >= 0; i--) {
            int h = happiness[i];
            h -= fee;
            if (h <= 0) {
                break;
            }
            result += h;
            fee += 1;
            if (fee == k) {
                break;
            }
        }
        return result;
    }
}
