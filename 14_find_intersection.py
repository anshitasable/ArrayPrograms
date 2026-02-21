class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        result=set()

        for element in nums2:
            if element in set1:
                result.add(element)
        return list(result)
        

