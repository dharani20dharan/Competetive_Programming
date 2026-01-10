class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            # We move the pointer pointing to the lower maximum height
            if left_max < right_max:
                left += 1
                # Update left_max if the new bar is taller
                left_max = max(left_max, height[left])
                # Water trapped is the difference between max height and current bar
                water += left_max - height[left]
            else:
                right -= 1
                # Update right_max if the new bar is taller
                right_max = max(right_max, height[right])
                # Water trapped is the difference between max height and current bar
                water += right_max - height[right]
                
        return water