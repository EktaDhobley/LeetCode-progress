class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        
       
        
        String str = paragraph.replaceAll("[^a-zA-Z0-9 ]", " ").toLowerCase(); //Convert everything to lowercase
        String words[] = str.split("\\s+"); //Split the string into words
        
        //Create a set, add banned words to it so we can use .contains in it
        Set<String> bannedWords = new HashSet();
        for(String word : banned)
            bannedWords.add(word);
        
        
        HashMap<String,Integer> wordCount = new HashMap<String,Integer>();
        
        for(String word : words){
            if(!bannedWords.contains(word))
                wordCount.put(word, wordCount.getOrDefault(word,0) + 1);
        }
        return Collections.max(wordCount.entrySet(), Map.Entry.comparingByValue()).getKey();
    
    }
}

//Map.Entry<String, Integer> maxEntry =  getMaxEntry(map);