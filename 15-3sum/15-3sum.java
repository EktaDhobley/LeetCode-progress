class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
         
        if(nums.length < 3) return new ArrayList<>();
        Arrays.sort(nums);
        Set<List<Integer>> set = new HashSet<>();
        for(int i=0;i<nums.length-2;i++){
            int j=i+1;
            int k= nums.length-1;
            
            while(j<k){
                int sum = nums[i] + nums[j]+ nums[k];
                if(sum==0) set.add(Arrays.asList(nums[i], nums[j++], nums[k--]));
               else if(sum<0) j++;
               else if(sum>0) k--;
            }
        }
        return new ArrayList<>(set);
    }
}


/*        
       for(int i=0;i<nums.length-2;i++){
           for(int j=i+1;j<nums.length-1;j++){
               for(int k=j+1;k<nums.length;k++){
                   if(i+j+k==0){
                       list.add(i);
                           list.add(j);
                           list.add(k);
                   }
               }
           }
       } 
          List<List<Integer>> res= new ArrayList<>();
      for(int i=1;i<list.size(); i++){
    // your logic here make use of Arrays.asList()
    res.add(Arrays.asList(i, i+1));
}
        return res;
        */