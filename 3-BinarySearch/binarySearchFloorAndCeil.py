"""
Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].
Return an array of integers denoting the [floor, ceil]. Return -1 for floor or ceiling if the floor or ceiling is not present.

Examples:

Input: x = 7 , arr[] = [5, 6, 8, 9, 6, 5, 5, 6]
Output: 6, 8
Explanation: Floor of 7 is 6 and ceil of 7 is 8.
Input: x = 10 , arr[] = [5, 6, 8, 8, 6, 5, 5, 6]
Output: 8, -1
Explanation: Floor of 10 is 8 but ceil of 10 is not possible.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints :
1 ≤ arr.size ≤ 105
1 ≤ arr[i], x ≤ 106

link - https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=ceil-the-floor

"""

class Solution:
    def getCeil(self,x,arr):
        ceil = -1
        i = 0
        j = len(arr) - 1
        
        while i <= j:
            middle = (i+j)//2
            if arr[middle] >= x:
                ceil = arr[middle]
                j = middle - 1
            else:
                i = middle + 1
        return ceil
                
    def getFloor(self,x,arr):
        floor = -1
        i = 0
        j = len(arr) - 1
        
        while i <= j:
            middle = (i+j)//2
            if arr[middle] <= x:
                floor = arr[middle]
                i = middle + 1
            else:
                j = middle - 1
        return floor
        
    def getFloorAndCeil(self, x: int, arr: list) -> list:
       arr = sorted(arr)
       ceil = self.getCeil(x,arr)
       floor = self.getFloor(x,arr)
       
       return [floor,ceil]

bs = Solution()
print(bs.getFloorAndCeil(7,[5, 6, 8, 9, 6, 5, 5, 6]))