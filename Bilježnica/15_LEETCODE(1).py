P2 - Osnovne kategorije algoritama, nizovi
 Traženje / pretraživanje
 704. Binary Search — Easy, direktna primjena
 35. Search Insert Position — Easy, varijanta binary search-a
▪ Maksimum / minimum
 53. Maximum Subarray — Medium, nadogradnja na find_max
 121. Best Time to Buy and Sell Stock — Easy, traženje max. razlike – možemo zajedno za vježbu!
▪ Sortiranje i nizovi
 26. Remove Duplicates from Sorted Array — Easy, kombinira sort + remove
 88. Merge Sorted Arrays — Easy, prirodan nastavak na sort zadatak
▪ Neki od ovih zadataka se mogu riješiti na vremenski učinkovit ili manje učinkovit način, ovisno o
implementaciji, ali više o tome na predavanju vezanom uz složenost algoritama
 Primjerice, pokušajte zadatak 121. riješiti korištenjem samo jedne for petlje!


704. Binary Search
Attempted
Easy
Topics
premium lock icon
Companies
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left +=1
            else:
                right -=1
        return -1


35. Search Insert Position
Easy
Topics
premium lock icon
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid + 1
            else:
                right= mid - 1
        return left


53. Maximum Subarray
Medium
Topics
premium lock icon
Companies
Given an integer array nums, find the subarray with the largest sum, and return its sum.
  
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

class Solution(object):
    def maxSubArray(self, nums):
        curr=nums[0]
        best=nums[0]
        for i in nums[1:]:
            curr= max(i, curr + i)
            best= max( best, curr)
        return best
