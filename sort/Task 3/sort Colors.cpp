class Solution {
public:
    void sortColors(vector<int>& nums) {
    int red=0,white=0,blue=0,j=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==0)
                red++;
            else if (nums[i]==1)
                white++;
            else 
                blue++;
        }
        
        while(red!=0)
        {
            nums[j]=0;
                j++;
            red--;
        }
        while(white!=0)
        {
            nums[j]=1;
                j++;
            white--;
        }
        while(blue!=0)
        {
            nums[j]=2;
                j++;
            blue--;
                
        }
        
        
        
    }
};
