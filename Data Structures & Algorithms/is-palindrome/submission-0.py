class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_string = "".join(char for char in s if char.isalnum())
        cleaned = "".join(char for char in alpha_string if char != " ")
        cleaned = cleaned.lower()
        return cleaned == cleaned[::-1]
        