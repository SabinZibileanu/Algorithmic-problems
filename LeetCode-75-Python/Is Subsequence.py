# # My Solution (appended 0 to t so it can be looped through if it is empty)
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         result_str = ""
#         counter_current_s_letter = 0
#         if len(s) == 0:
#             s += '0'
        
#         if len(t) == 0:
#             t += '0'
        
#         for letter in t:
#             if letter == s[counter_current_s_letter]:
#                 counter_current_s_letter += 1
#                 result_str += letter

#                 if result_str == s:
#                     return True
        
#         return False

# # Easier to understand solution:
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = right = 0

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            
            right += 1
        
        return left == len(s)
