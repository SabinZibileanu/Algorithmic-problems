from typing import List

# without division O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        res = []
        totalProduct = 1

        for num in nums:
            totalProduct *= num
            prefix.append(totalProduct)
        
        totalProduct = 1
        for num in nums[::-1]:
            totalProduct *= num
            postfix.append(totalProduct)
        
        postfix = postfix[::-1]
        
        for idx, _ in enumerate(prefix):
            if idx == 0:
                prefixProd = 1
                postfixProd = postfix[idx + 1]

                res.append(prefixProd * postfixProd)
            
            elif idx == len(prefix) - 1:
                postfixProd = 1
                prefixProd = prefix[idx - 1]
                res.append(prefixProd * postfixProd)
            
            else:
                prefixProd = prefix[idx - 1]
                postfixProd = postfix[idx + 1]
                res.append(prefixProd * postfixProd)

        return res

# with division O(n)
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        qty_zeros = nums.count(0)

        if qty_zeros > 1:
            return [0] * len(nums)
        
        elif qty_zeros == 1:
            productExceptZero = 1
            for num in nums:
                if num != 0:
                    productExceptZero *= num
            
            return [0 if num != 0 else productExceptZero for num in nums]
        
        else:
            totalProduct = 1
            for num in nums:
                totalProduct *= num

            return [totalProduct // num for num in nums]
