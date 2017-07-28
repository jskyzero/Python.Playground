# 406. Queue Reconstruction by Height  QuestionEditorial Solution  My Submissions
# Total Accepted: 2646
# Total Submissions: 4957
# Difficulty: Medium
# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        temp = sorted(people, key = lambda x : (- x[0], x[1]) )
        print temp
        ans = []
        for x in temp:
            ans.insert(x[1],x)
        return ans     
    # def reconstructQueue(self, people):
    # return reduce(lambda q, p: q.insert(p[1], p) or q, sorted(people, key=lambda (h, t): (-h, t)), []) 
        

if __name__ == "__main__":
    a = Solution()
    print a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])