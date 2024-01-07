class Solution:
    def compress(self, chars: List[str]) -> int:
        read = write = 0

        while read < len(chars):
            chars[write] = chars[read]
            count = 0

            while read < len(chars) and chars[read] == chars[write]:
                read += 1
                count += 1
            
            if count > 1:
                for c in str(count):
                    write += 1
                    chars[write] = c
            
            write += 1
        
        return write