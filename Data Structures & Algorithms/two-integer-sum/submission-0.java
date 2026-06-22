class Solution {
    public int[] twoSum(int[] nums, int target) {
        ArrayList<Integer> temp = new ArrayList<Integer>(); 
         
        for(int i = 0; i < nums.length; i++){
            for(int j = i+1; j < nums.length; j++){
                if(nums[i] + nums[j] == target){
                    temp.add(i); 
                    temp.add(j); 
                }
            }
        }
        int[] solution = new int[temp.size()]; 
        for(int i = 0; i < solution.length; i++)
            solution[i] = temp.get(i); 

        return solution; 
         
    }
}
