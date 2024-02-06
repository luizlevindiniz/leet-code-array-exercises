class Solution {
    public static int getContainerHeight(int x, int y) {
        return Math.min(x, y);
    }

    public static int getContainerLength(int start, int stop) {
        return stop - start;
    }

    public static int getArea(int height, int distance) {
        return height * distance;
    }

    // O(n)
    public int maxArea(int[] height) {

        int i = 0;
        int j = height.length - 1;

        int distance = getContainerLength(i, j);
        int tallness = getContainerHeight(height[i], height[j]);
        int maxSoFar = getArea(tallness, distance);

        while (i < j) {
            if (height[i] <= height[j]) {
                i++;
            } else {
                j--;
            }

            distance = getContainerLength(i, j);
            tallness = getContainerHeight(height[i], height[j]);
            int area = getArea(tallness, distance);

            if (area > maxSoFar) {
                maxSoFar = area;
            }

        }

        return maxSoFar;

        /*
         * // naive approach O(n2)
         * int max_area = 0;
         * 
         * for(int i = 0; i < height.length; i++){
         * int max_so_far = 0;
         * for(int j = height.length - 1; j > i; j--){
         * int distance = getContainerLength(i,j);
         * int tallness = getContainerHeight(height[i],height[j]);
         * 
         * max_so_far = distance * tallness;
         * if(max_so_far > max_area){
         * max_area = max_so_far;
         * }
         * 
         * }
         * }
         * 
         * return max_area;
         */
    }
}