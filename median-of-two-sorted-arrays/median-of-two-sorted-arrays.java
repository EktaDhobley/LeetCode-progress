 class Solution{
     public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int l1 = nums1.length-1;
        int l2 = nums2.length-1;
        int[] arr = new int[nums1.length+nums2.length];
        double ans=0;
        int i=0,j=0,l=0;
        while(i<=l1 && j<=l2){
            if(nums1[i]<nums2[j]){
                arr[l++] = nums1[i++];
            }else{
                arr[l++]=nums2[j++];
            }
        }
        while(i<=l1){
            arr[l++]=nums1[i++];
        }
        while(j<=l2){
            arr[l++]=nums2[j++];
        }
        int k = (nums1.length+nums2.length)/2;
        if((nums1.length+nums2.length)%2==0){
            double n1 = arr[k-1];
            double n2 = arr[k];
            ans = (n1+n2)/2;
        }else{
            ans = arr[k];
        }
        return ans;
    }
 }