class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left =0
        res =0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            
            charSet.add(s[right])
            res = max(res, right - left+1)
        
        return res


        # char_set=set()
        # left=0
        # max_length=0
        
        # for right in range(len(s)):
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left+=1
            
        #     char_set.add(s[right])
        #     max_length= max(max_length, right-left+1)

        # return max_length






