class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
       vector<int> result;
        for(int i=0;i<nums.size();i++)
        {
            for (int j=0;j<nums.size();j++)
                if(nums[i]<nums[j])
                {
                    int temp =nums[i];
                    nums[i]=nums[j];
                    nums[j]=temp;
                }
                    
        }
        for(int i=0;i<nums.size();i++)
        { if (nums[i]==target)
            result.push_back(i);
        }
        
        return result;
            
        
        
        
    }
};
