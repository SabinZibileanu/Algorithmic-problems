# 2 pointers

class Solution:
    def reverseVowels(self, s: str) -> str:
        list_string_letters = list(s)
        left, right = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while left < right:
            if list_string_letters[left] not in vowels:
                left += 1
            
            elif list_string_letters[right] not in vowels:
                right -= 1

            else:
                list_string_letters[left], list_string_letters[right] = list_string_letters[right], list_string_letters[left]
                left += 1
                right -= 1
    
        return ''.join(list_string_letters)





