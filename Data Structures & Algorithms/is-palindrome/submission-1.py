class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphastring = ""
        for i in s:
            if i.isalnum():
                alphastring += i.lower()
        n = len(alphastring)
        l = 0
        r = n-1
        flag = True
        while l<r:
            if alphastring[l] != alphastring[r]:
                flag = False
                break
            l += 1
            r-=1
        return True if flag==True else False