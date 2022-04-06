class Solution {
//     public String longestPalindrome(String s) {
//         int x, y = 0;
//         int max_len = -1;
//         for(int i =0; i < s.length(); i++){
//             for(int j = s.length(); j > 0; j--){
//                 while(i < j){
//                     if(s.charAt(i) == s.charAt(j)){
//                         x = i;
//                         y = j;
//                     }
//                     else{
//                         x = x;
//                         y = y;
//                     }
//                 }
//                String curr = s.substring(x,y);
//         max_len = curr.length();
//            }
//         }
        
//         //if(max_len < curr. ){
//          //   max_len = curr.length();
            
//         }  
//      return curr;
//     }
// 
public String longestPalindrome(String s) {
    if (s == null || s.length() < 1) return "";
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    return s.substring(start, end + 1);
}

private int expandAroundCenter(String s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
        L--;
        R++;
    }
    return R - L - 1;
}}