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
    
# 풀이 4 zip을 활용하여 가독성 개선
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""

        # zip() 함수를 사용하여 word1과 word2의 각 문자를 순차적으로 결합
        for char1, char2 in zip(word1, word2):  # O(n) n은 두 문자열 중 더 긴 문자열 길이
            merged_string += char1 + char2

        merged_string += word1[len(word2) :] + word2[len(word1) :] # O(k) k는  word1과 word2의 남은 부분의 길이 중 더 긴 길이 최악의 경우 O(n)

        return merged_string