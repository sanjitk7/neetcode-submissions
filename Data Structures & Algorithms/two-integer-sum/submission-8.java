class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> d = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if (d.containsKey(diff)){
                return new int[] { d.get(diff), i };
            }
            d.put(nums[i], i);
        }
        return new int[0];
    }
}
