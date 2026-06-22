class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexList = []
        for i in range(len(nums)-1): 
            temp = target-nums[i]
            if(temp in nums[(i+1):]):
                indexList.append(i) 
                indexList.append(nums[(i+1):].index(temp)+i+1)
                break

        return indexList


