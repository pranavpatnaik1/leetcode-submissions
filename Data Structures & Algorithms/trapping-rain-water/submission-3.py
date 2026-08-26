# class Solution:
#     def trap(self, height: List[int]) -> int:
#         # Ignore ends
#         first = 0
#         for j in range(len(height)):
#             if j<len(height)-2 and height[j+1] >= height[j]:
#                 continue
#             else:
#                 first = j
#                 break
        
#         print(first)
#         last = len(height) - 1
#         for k in range(len(height) - 1, -1, -1):
#             if k>0 and height[k-1] >= height[k]:
#                 continue
#             else:
#                 last = k
#                 break
#         print(last)

#         # Detect buckets
#         start = first
#         temp = 0
#         end = 0

#         trapped = 0
#         for i in range(first, last+1):
#             if i<(len(height) - 2) and height[i+1] < height[i]:
#                 continue
#             elif i<(len(height) - 2) and height[i+1] > height[i]:
#                 if height[i+1] < start:
#                     temp = height[i+1]
#                     j = 2
#                     if height[i+j] > temp:
#                         while height[i+j] > temp:
#                             if height[i+j] >= start:
#                                 break
#                             else:
#                                 j += 1
#                         end = height[i+j]
#                     else:
#                         end = height[i+j]
#                 else:
#                     end = height[i+1]
#             if start < end: 
#                 trapped += (min(start, end) * (end - start)) - sum(height[start+1:end])
#                 start = end

#         return trapped
    
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        trapped_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped_water += right_max - height[right]

        return trapped_water
