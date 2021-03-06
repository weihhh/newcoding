class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        #cur[i]为0-i子状态的最大rob，当前轮询到i+2时，pre为i的cur即cur[i](不管最后是取的i还是i-1)
        #pre 代表若不选之前一个的话，最大的rob，cur代表当前最大rob，即选前一个
        #核心思想：当前和之前只能取其一，而且必须取一，因为都为正数
        pre=0
        cur=0
        for i in nums:
            temp=max(cur,pre+i)
            pre=cur
            cur=temp
        return cur