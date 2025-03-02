from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows_with_cameras = []
        total_beams = 0
        product_beams = 1

        for i, floor_plan_representation in enumerate(bank):
            if floor_plan_representation.count('1') != 0:
                rows_with_cameras.append(i)

        if len(rows_with_cameras) == 1:
            return 0
        
        for i in range(len(rows_with_cameras) - 1):
            for j in range(rows_with_cameras[i], rows_with_cameras[i + 1] + 1):
                number_of_cameras_on_row = bank[j].count('1')
                if number_of_cameras_on_row != 0:
                    product_beams *= number_of_cameras_on_row
            total_beams += product_beams
            product_beams = 1
        
        return total_beams