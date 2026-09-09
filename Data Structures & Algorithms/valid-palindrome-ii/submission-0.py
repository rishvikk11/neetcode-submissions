class Solution:
    def validPalindrome(self, s: str) -> bool:
        # point of this problem is that once you have found a mismatch, then removing one character or another should get you a valid palindrome, otherwise not
        left, right = 0, len(s)-1

        while left < right:
            # mismatch found, immediately judge here for palindrome
            if s[left] != s[right]:
                skip_l = s[left + 1: right + 1]
                skip_r = s[left: right]
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            left += 1
            right -= 1
        # if no mismatches at all, then we had palindrome by default
        return True            