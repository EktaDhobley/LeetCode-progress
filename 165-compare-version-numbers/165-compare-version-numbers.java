class Solution {
    public int compareVersion(String version1, String version2) {
        String[] c1 = version1.split("\\.");
        String[] c2 = version2.split("\\.");
        
        int n1 = c1.length, n2 = c2.length;
        
          int i1, i2; 
        
            for(int k = 0; k < Math.max(n1,n2) ; k++){
          i1 = k < n1 ? Integer.parseInt(c1[k]):0;
          i2 = k < n2? Integer.parseInt(c2[k]):0;
          
          if(i1 != i2){
              return i1> i2 ? 1 : -1;
          }
      }
        
      
            
        return 0;
    }
}