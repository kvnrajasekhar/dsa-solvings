class Solution:

    def encode(self, strs: List[str]) -> str:

        length = 0 
        delimiter = "@"
        encoded_word = ""
        for word in strs:
            length = len(word)
            encoded_word += str(length) + delimiter + word

        return encoded_word

    def decode(self, s: str) -> List[str]:
        i = 0
        j = i 
        length = 0

        result = []
        while i < len(s):

            while s[j] != "@":
                j +=1

            length = int(s[i:j])

            word = s[j+1 : length + j+1]

            result.append(word)

            i = length + j + 1
            j=i

        return result
