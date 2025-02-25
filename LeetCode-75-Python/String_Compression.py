from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        counter_occurences = 0
        length_chars = len(chars)
        i = 0
        result = []
        
        while i < length_chars:
            char_to_check = chars[i]

            while i < length_chars and char_to_check == chars[i]:
                counter_occurences += 1
                i += 1
            
            if counter_occurences > 1:
                result.append(char_to_check)
                result.extend(list(str(counter_occurences)))
            
            else:
                result.append(char_to_check)
            counter_occurences = 0
        
        chars[:] = result
        return len(result)