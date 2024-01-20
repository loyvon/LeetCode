from typing import List

class Solution:
    def binSearch(self, nums, left, right, val) -> tuple:
        l = nums[left]
        r = nums[right]
        if val >= r:
            return right

        if left + 1 == right or left == right:
            return left

        mid = (left + right) // 2
        m = nums[mid]
        if m < val:
            return self.binSearch(nums, mid, right, val)
        elif m > val:
            return self.binSearch(nums, left, mid, val)
        else:
            return mid


    def minOperations(self, nums: List[int]) -> int:
        w = len(nums)
        nums.sort()
        repeats = 0
        uniq = []
        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                repeats += 1
                continue
            uniq.append(v)
        nums = uniq
        l = len(nums)

        filled = 1
        for i, v in enumerate(nums):
            right = v + w - 1
            j = self.binSearch(nums, i, l - 1, right)
            #print(f'>>>{i},{fr},{to}')
            #j = fr
            if j - i + 1 > filled:
                # print(f'{i},{j},{filled}')
                filled = j - i + 1
                if filled == l:
                    break
        
        return l - filled + repeats


if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([4,2,5,3]))
    print(s.minOperations([1,2,3,5,6]))
    print(s.minOperations([1,10,100,1000]))
    print(s.minOperations([1,1,1,1,1,1,1]))
    print(s.minOperations([100,200,300,400]))
    print(s.minOperations([1,1,2,2,3,3,4,4,5,5]))
    print(s.minOperations([1,1,2,2,3,3,4,4,5,5,6,6]))
    print(s.minOperations([1,1,2,2,3,3,4,4,5,5,6,6,7,7]))
    print(s.minOperations([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]))
    print(s.minOperations([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9]))
    print(s.minOperations([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]))
    print(s.minOperations([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10]))
    print(s.minOperations([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]))
    print(s.minOperations([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11]))
    print(s.minOperations([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11]))