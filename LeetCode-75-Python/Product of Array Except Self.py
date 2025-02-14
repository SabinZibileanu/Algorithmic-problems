from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_products_left = [1]
        arr_products_right = [1]
        left = 1
        right = 1
        res_arr = []

        for i in range(len(nums) - 1):
            left *= nums[i]
            arr_products_left.append(left)
        
        for i in range(len(nums) - 1, 0, -1):
            right *= nums[i]
            arr_products_right.append(right)
        
        arr_products_right = arr_products_right[::-1]

        for nums_left, nums_right in zip(arr_products_left, arr_products_right):
            res_arr.append(nums_left * nums_right)
        
        return res_arr
        
        
        # arr_products = []
        # counter_operations = 0
        # length_arr = len(nums)
        # ok = True

        # while ok: 
        #     if counter_operations == length_arr - 1:
        #         product = prod(nums[:counter_operations])
        #         arr_products.append(product)
        #         ok = False
            
        #     else:
        #         prefix = nums[:counter_operations]
        #         suffix = nums[counter_operations + 1:]
                
        #         product = prod(prefix) * prod(suffix)
        #         arr_products.append(product)
        #         counter_operations += 1

        # return arr_products      
        