class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1

        while (l <= r):
            mid = l + (r - l)//2

            if (nums[mid] == target):
                return mid

            #Assuming left half is sorted
            elif (nums[l] <= nums[mid]):
                #left half is the search space
                if(nums[l]<= target < nums[mid]):
                    r = mid - 1
                #else go for right
                else:
                    l = mid + 1
            #Assuming right half is sorted
            else:
                #right is the search space
                if(nums[mid] < target <= nums[r]):
                    l = mid + 1
                #else go left
                else:
                    r = mid - 1

        return -1 