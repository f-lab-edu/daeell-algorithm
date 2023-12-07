# 풀이 1
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        cursor = 0
        merged_string = ""
        while cursor < len(word1) or cursor < len(word2): # O(n)
            if cursor < len(word1): # O(1)
                merged_string += word1[cursor] # O(1)
            if cursor < len(word2): # O(1)
                merged_string += word2[cursor] # O(1)
            cursor += 1
        return merged_string
    
# 풀이 2
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        for i in range(min(len(word1), len(word2))): # O(n)
            merged_string += word1[i] # O(1)
            merged_string += word2[i] # O(1)

        merged_string += word2[len(word1):] # O(1)
        merged_string += word1[len(word2):] # O(1)
        return merged_string
    
# 풀이 3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_list = []
        for i in range(max(len(word1), len(word2))): # O(n)
            if i < len(word1): # O(1)
                merged_list.append(word1[i]) # O(1)
            if i < len(word2): 
                merged_list.append(word2[i]) # O(1)
        return ''.join(merged_list) # O(n)