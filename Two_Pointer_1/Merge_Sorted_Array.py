#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m-1     #Initialize first pointer to m-1 which is lenght of nums1 
        second = n-1    #Initialize second pointer to n-1 which is lenght of nums2
        third = m+n-1   #Initialize third pointer to m+n-1 which is addition of lenght of nums1 and nums2
        
        while first >= 0 and second >= 0:   #Continue till the first and second pointers are greater than 0
            if nums1[first] < nums2[second]:    #If the nums1[first] is less than nums2[second] change nums1[third] to nums2[second]
                nums1[third] = nums2[second]
                second -= 1 #Decrement second by 1
            
            else:   #Else change nums1[third] as nums1[first]
                nums1[third] = nums1[first]
                first -= 1  #Decrement first by 1
            third -= 1  #Decrement third by 1

        if second >=0:  #If the second is less than 0
            nums1[:second+1] = nums2[:second+1] #Copy all the remaning elements in nums2 to nums1