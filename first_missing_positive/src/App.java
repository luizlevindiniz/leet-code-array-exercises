import java.util.Arrays;

class Solution {
    public static int firstMissingPositive(int[] nums) {
        int i = 0;
        int n = nums.length;
        while (i < n) {

            int crt = nums[i] - 1;
            if (nums[i] > 0 && nums[i] < n && nums[i] != nums[crt]) {
                int temp = nums[i];
                nums[i] = nums[crt];
                nums[crt] = temp;
            } else {
                i++;
            }
            System.out.println(i + Arrays.toString(nums));

        }

        return 1;

    }

    public static void main(String[] args) {
        int[] input = new int[] { 4, 3, 5, 2, 1 };
        firstMissingPositive(input);

    }

}