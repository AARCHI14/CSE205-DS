class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for i in range(0,len(word1)):
            for j in range(0,len(word1[i])):
                i+1 and j+1
        for k in range(0,len(word2)):
            for l in range(0,len(word2[k])):
                k+1 and l+1
        if word1[i][j]==word2[k][l]:
            return True
        else:
            return False