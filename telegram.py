#!/usr/bin/env python3
class CropRatio:
    
    def __init__(self):
        self._crops = {}
        self._total_weight = 0

    def add(self, name, crop_weight):
        curr_crop_weight = 0

        if not name in self._crops:
            self._crops[name] = curr_crop_weight

        curr_crop_weight = curr_crop_weight + crop_weight
        self._total_weight += crop_weight

    def proportion(self, name):
        if name not in self._crops.keys():
            return None
        return self._crops[name]/self._total_weight

if __name__ == "__main__":
    crop_ratio = CropRatio()
    crop_ratio.add('Wheat', 4)
    crop_ratio.add('Wheat', 5)
    crop_ratio.add('Rice', 1)
    
    print(crop_ratio.proportion('Wheat'))
    print()