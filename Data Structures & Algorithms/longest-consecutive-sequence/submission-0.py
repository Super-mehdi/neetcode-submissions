class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_seq = 0
        num_set = set(nums)
        for num in nums:
            cnt = 1
            tmp = num
            while tmp+1 in num_set:
                cnt+=1
                tmp+=1
            len_seq =max(len_seq,cnt)
        return len_seq