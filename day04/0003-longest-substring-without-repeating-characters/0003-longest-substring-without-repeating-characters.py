class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        curr_word = []
        for c in s:
            if c not in curr_word:
                curr_word.append(c)
            else:
                while c in curr_word:
                    del curr_word[0]
                curr_word.append(c)
            max_length = max(max_length, len(curr_word))
        return max_length


# del -> collection.deque.popleft
from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        curr_word = deque()
        for string in s:
            if string not in curr_word:
                curr_word.append(string)
            else:
                while string in curr_word:
                    curr_word.popleft()
                curr_word.append(string)
            max_length = max(max_length, len(curr_word))
        return max_length
    

# 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_set = set()  # 문자를 저장하는 해시 테이블
        left = 0  # 슬라이딩 윈도우의 왼쪽 포인터

        for right in range(len(s)): # O(n)
            while s[right] in char_set: # 최대 O(n)
                char_set.remove(s[left]) # O(1)
                left += 1
            char_set.add(s[right]) # O(1)
            max_length = max(max_length, right - left + 1) # O(1)

        return max_length