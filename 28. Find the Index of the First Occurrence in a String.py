class Solution:
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        
haystack = "devang"
needle = "ango"

ret = Solution().strStr(haystack,needle)
print(ret)
