# 4. Median of Two Sorted Arrays  QuestionEditorial Solution  My Submissions
# Total Accepted: 118446
# Total Submissions: 590268
# Difficulty: Hard
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp = []
        temp.extend(nums1)
        temp.extend(nums2)
        temp = sorted(temp)
        size =  len(temp)
        if size % 2 == 0:
            return (temp[size/2-1] + temp[size/2] )/ 2.0
        else:
            return temp[size/2]

if __name__ == "__main__":
    a = Solution()
    print a.findMedianSortedArrays([1],[2])
