class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sList = s.toCharArray(); 
        char[] tList = t.toCharArray();
        if(sList.length != tList.length) return false;
        
        Arrays.sort(sList); 
        Arrays.sort(tList); 
        return Arrays.equals(sList, tList); 

         
    }
}
