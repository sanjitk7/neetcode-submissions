class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> outerMap = new HashMap<>();
        for (String s: strs) {
            int[] array_alphabets = new int[26];
            for (char c: s.toCharArray()){
                array_alphabets[c - 'a']++;
            }
            String key = Arrays.toString(array_alphabets);
            outerMap.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(outerMap.values());
    }
}
