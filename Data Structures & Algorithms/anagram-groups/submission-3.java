class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> ans = new HashMap<>(); 
        for(String s : strs){
            char[] array = s.toCharArray(); 
            Arrays.sort(array); 
            String sorted = new String(array); 
            ans.putIfAbsent(sorted, new ArrayList<String>()); 
            ans.get(sorted).add(s); 
        }
        return new ArrayList<>(ans.values()); 
    }
}
