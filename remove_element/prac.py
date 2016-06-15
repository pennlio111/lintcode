class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        i = 0   # place-holder
        j = 0
        while j < len(A):
            if A[j] != elem:
                A[i], A[j] = A[j], A[i]
                i += 1
            j += 1
        return i