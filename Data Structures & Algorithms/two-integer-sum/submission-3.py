from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = []
        for i in range(len(nums)):
            need = target - nums[i]
            if need in my_list:
                return [min(i, my_list.index(need)), max(i, my_list.index(need))]
            else:
                my_list.append(nums[i])
        print(my_list)