from typing import List

class Node:
    val = None
    count = 0
    left = None
    right = None

    def __init__(self, val):
        self.val = val
        self.count = 1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def heapsort(nums: List[int]) -> List[int]:
            root = Node(nums[0])
            for v in nums[1:]:
                p = root
                while p is not None:
                    if p.val == v:
                        p.count += 1
                        break
                    elif p.val < v:
                        r = p.right
                        if r is None:
                            p.right = Node(v)
                            #print(f'r{v}')
                            break
                        else:
                            p = r
                    else:
                        l = p.left
                        if l is None:
                            p.left = Node(v)
                            #print(f'l{v}')
                            break
                        else:
                            p = l
            res = []
            def get_val(n):
                if n is None:
                    return
                else:
                    get_val(n.left)
                    for _ in range(n.count):
                        res.append(n.val)
                    get_val(n.right)

            get_val(root)
            return res
        
        sorted = heapsort(nums)

        res = set()
        for left in range(len(sorted)):
            if sorted[left] > 0 / 3:
                break
            search = left + 1
            right = len(sorted) - 1
            while search < right:
                if sorted[search] + sorted[left] + sorted[right] == 0:
                    res.add(tuple([sorted[left], sorted[search], sorted[right]]))
                    search += 1
                    right -= 1
                elif sorted[search] + sorted[left] + sorted[right] > 0:
                    right -= 1
                else:
                    search += 1
        
        return [[_[0], _[1], _[2]] for _ in res]
if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))